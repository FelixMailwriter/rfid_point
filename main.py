# -*- coding: utf-8 -*-

import scanner as Scanner

if __name__ == '__main__':

    reader = Scanner.Scanner()

    try:
        reader.start(8)
    except KeyboardInterrupt:
        print(' interrupted by user')
        reader.stop()
        reader = None
