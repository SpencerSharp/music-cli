#!/usr/bin/env python3
"""
Usage:
    music
    music <command> [<args>...]
"""
import sys, os
from clirunner import CLIRunnerDaemon
from monitor import SpotifyMonitorDaemon
from terminal import Terminal
from env import SpoolsBashProfile
import ipc
import spotify


os.system('rm -rf ~/.spools/test/music/*')
spotify.get_spotify_permissions()

runner = CLIRunnerDaemon()
bash_profile = SpoolsBashProfile()
bash_profile.add_cmd('export SPOOLS_RUNNER_DAEMON='+str(ipc.get_process_info(runner)[0]))
terminal = Terminal(bash_profile)
monitor = SpotifyMonitorDaemon()
ipc.send_message_to(runner, ' '.join(sys.argv))
ipc.send_message_to(monitor,'startup')  