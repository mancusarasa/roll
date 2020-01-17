#!/usr/bin/env python3

import sys
import traceback

from game import Game

if __name__ == '__main__':
    try:
        g = Game()
        g.Run()
        sys.exit(0)
    except Exception as e:
        print(str(e))
        sys.exit(1)

