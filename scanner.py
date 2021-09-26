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
        print(f'Start reading')
        self.work = True
        with open("data.txt", "w", encoding='utf-8') as self.file:
            old_tag = None
            while self.work:
                tag = ""
                raw_data = self.connector.read(tag_length + 6)
                if (len(raw_data) < tag_length + 4):
                    continue
                tag = raw_data[4:11]
                if tag != old_tag and len(tag) != 0:
                    old_tag = tag
                    record = f'{datetime.datetime.now()} ---> tag: {tag}'
                    print(f'record= {record}')
                    print(record, file=self.file, end='\n')

    def stop(self):
        self.work = False
        self.closePort()
        self.file.close()

