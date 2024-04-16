# views/components/led_status_label.py

from PyQt5.QtWidgets import QLabel


class LEDStatusLabel(QLabel):
    def __init__(self):
        super().__init__("LED status: OFF")