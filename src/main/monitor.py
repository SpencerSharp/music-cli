import signal, time
from dataitem import Song
from daemon import Daemon
from clirunner import CLIRunnerDaemon
import ipc
import spotify
class MonitorDaemon(Daemon):
    def __init__(self, run_message, get_state, state_action):
        self.prev_state = None
        self.cur_state  = None
        self.run_message = run_message
        self.get_state = get_state
        self.state_action = state_action
        super().__init__(signal.SIGUSR1, self.run)

    def run(self, messages):
        for message in messages:
            self.run_message(message)
        self.monitor()

    def monitor(self):
        while self.cur_state == None or self.cur_state.equals(self.prev_state):
            self.cur_state = self.get_state()
            time.sleep(5)
        self.state_action(self.prev_state, self.cur_state)
        self.prev_state = self.cur_state
        self.monitor()

class SpotifyMonitorDaemon(MonitorDaemon):
    def __init__(self):
        super().__init__(self.run_message, self.get_state, self.state_action)

    def run_message(self, message):
        n = 2

    def get_state(self):
        track = spotify.current_track()
        if track == None:
            return None
        if self.cur_state != None and track['id'] == self.cur_state.id:
            return self.cur_state
        return Song(track,'spotify')

    def state_action(self, prev, cur):
        if prev != None and cur != None:
            print('\nPlease rate "{0}" by {1}: '.format(prev.name, prev.artist_name), end='')
            ipc.send_message_to(CLIRunnerDaemon(),'music rate -d {} -r '.format(prev.id),False)
            spotify.pause_player()