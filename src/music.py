#!/usr/bin/env python3
"""
Usage:
    music <command> [<args>...]

Commands:
    music p|play
    music m|me
    music q|queue
    music s|skip
    music a|alias
    music r|rate
    music l|login
    music i|import
    music c|categorize
    music t|tag
    music -q|--quit
    music -o|--options
    music -h|--help
    music -v|--version
"""

import sys, os, signal
from docopt import docopt

from lib.data import save_to_local
from lib.init import init
from lib.monitor import get_monitor_pid

from main.rate import rate
from main.me   import me

def main():
    init()
    arguments = docopt(__doc__, version='DEMO 0.8', options_first=True)
    command = arguments['<command>'].upper()
    if   command ==     'PLAY':
        play()
    elif command ==     'RATE':
        rate()
    elif command ==     'ME':
        me()
    save_to_local()
    os.kill(get_monitor_pid(), signal.SIGUSR1)

if __name__ == '__main__':
    main()