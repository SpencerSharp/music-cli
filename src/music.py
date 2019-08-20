#!/usr/bin/env python3
"""
Usage:
    music <command> [<args>...]

Commands:
    music p|play
    music q|queue
    music s|skip
    music a|alias
    music r|rate
    music l|login
    music i|import
    music c|categorize
    music -q|--quit
    music -o|--options
    music -h|--help
    music -v|--version
"""

import sys
from docopt import docopt

from lib.data import save_to_local
from lib.init import init

from main.rate import rate

def main():
    init()
    arguments = docopt(__doc__, version='DEMO 0.8', options_first=True)
    command = arguments['<command>'].upper()
    if   command ==     'PLAY':
        play()
    elif command ==     'RATE':
        rate()
    save_to_local()

if __name__ == '__main__':
    main()