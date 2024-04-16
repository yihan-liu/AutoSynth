# autosynth.py

import sys

from PyQt5.QtWidgets import QApplication
from controllers import MainController


SERIAL_PORT = 'COM5'
BAUD_RATE = 9600

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = MainController(SERIAL_PORT, BAUD_RATE)
    controller.run()
    app.exec_()
    controller.close()
