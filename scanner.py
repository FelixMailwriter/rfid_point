import serial
import time
import datetime

class Scanner(object):

    def __init__(self):
        self.connector = self._init_connector()
        self.work = False

    def _init_connector(self):
        ser = serial.Serial("/dev/ttyUSB0")
        ser.baudrate = 57600
        ser.bytesize = serial.EIGHTBITS
        ser.parity = 'N'
        ser.stopbits = 1
        ser.startbits = 1
        ser.timeout = None
        ser.xonxoff = False
        ser.rtscts = False
        ser.dsrdtr = False
        print('Connector is created')
        print(f'Connection params: {ser}')
        return ser

    def openPort(self):
        self.connector.open()
        print(f'++++++++++ Port is opened ++++++++++')

    def closePort(self):
        self.connector.close()
        print(f'---------- Port is closed ----------')

    def start(self, tag_length):
        self.work = True
        with open("data.txt", "w") as f:
            old_tag = None
            while self.work:
                tag = ""
                raw_data = self.connector.read(tag_length)
                raw_tag = raw_data[4:tag_length+4]
                for i in range(len(raw_tag)):
                    tag = tag + hex(raw_tag[i])
                if tag != old_tag:
                    record = f'{datetime.datetime.now()} ---> tag: {tag}'
                    f.write(record)

    def stop(self):
        self.work = False
        self.closePort()

