#!/usr/bin/env python3
"""
Usage:
    music
    music <command> [<args>...]

Commands:
    music p|play
    music r|rate
    music q|queue
    music s|skip
    music i|import
    music m|me
    music b|backlog
    music c|categorize
    music a|alias
    music l|login
    music t|trim
    music -h|--help
    music -o|--options
    music -v|--version
    music -q|--quit
"""

import sys, os, signal
from docopt import docopt

from lib.data import save_to_local
from lib.init import init, alert
from procs.monitor import get_monitor_pid

from main.rate import rate
from main.me   import me

def main():
    init()
    arguments = docopt(__doc__, version='DEMO 0.8', options_first=True)
    command = arguments['<command>'].upper() if arguments['<command>'] != None else None
    if   command ==     'PLAY':
        play()
    elif command ==     'RATE':
        rate()
    elif command ==     'QUEUE':
        queue()
    elif command ==     'SKIP':
        skip()
    elif command ==     'IMPORT':
        imprt()
    elif command ==     'ME':
        me()
    elif command ==     'BACKLOG':
        backlog()
    elif command ==     'CATEGORIZE':
        categorize()
    elif command ==     'ALIAS':
        alias()
    elif command ==     'LOGIN':
        login()
    elif command ==     'TRIM':
        trim()
    else:
        print('This is the Spools Music CLI')
    save_to_local()
    alert()

if __name__ == '__main__':
    main()