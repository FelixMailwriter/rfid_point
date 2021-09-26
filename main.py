# -*- coding: utf-8 -*-

import scanner as Scanner

if __name__ == '__main__':
    params = {}
    params['port'] = "/dev/ttyUSB0"
    params['baudrate'] = 57600
    params['stopbits'] = 2
    params['dsrdtr'] = 1
    params['startbits'] = 1
    params['parity'] = 'N'

    reader = Scanner.Scanner(params)

    try:
        reader.start(12)
    except KeyboardInterrupt:
        print(' interrupted by user')
        reader.close()
        reader = None
