# views/components/led_switch_button.py

from PyQt5.QtWidgets import QPushButton


class LEDSwitchButton(QPushButton):
    def __init__(self):
        super().__init__("Toggle")
        