# views/main_control_window.py

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget
)
from PyQt5.QtCore import QSize

from .components.toggle_button import ToggleButton

class MainControlWindow(QMainWindow):
    def __init__(self, status_dict):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("AutoSynth")

        self.toggle_buttons = {}

        layout = QVBoxLayout()

        for channel_name in status_dict:
            channel_label = QLabel(channel_name)
            toggle_button = ToggleButton()
            self.toggle_buttons[channel_name] = toggle_button

            channel_layout = QHBoxLayout()
            channel_layout.addWidget(channel_label)
            channel_layout.addWidget(toggle_button)

            layout.addLayout(channel_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
