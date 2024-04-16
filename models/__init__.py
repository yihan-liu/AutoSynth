# models/__init__.py

import struct
import serial


class SerialManager:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

        self.ser = None
        self.status = None
    
    def connect(self):
        self.ser = serial.Serial(port='COM5', baudrate=9600)

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

    def write(self, data):
        if self.ser and self.ser.is_open:
            self.ser.write(str(data).encode())

    def read_status(self):
        try:
            data = self.ser.read(4)
            self.status = struct.unpack('<I', data)[0]  # read command in binary
        except Exception as e:
            raise Exception(f"Cannot parse the status in binary format: {e}")