# views/main_control_window.py

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout
)
from PyQt5.QtCore import QSize
from .components.toggle_button import ToggleButton
from .components.step_button import StepButton

# class MainControlWindow(QMainWindow):
#     def __init__(self, status_dict):
#         super().__init__()
#         self.setMinimumSize(QSize(400, 300))
#         self.setWindowTitle("AutoSynth")

#         self.toggle_buttons = {}

#         layout = QVBoxLayout()

#         for channel_name in status_dict:
#             channel_label = QLabel(channel_name)
#             toggle_button = ToggleButton()
#             self.toggle_buttons[channel_name] = toggle_button

#             channel_layout = QHBoxLayout()
#             channel_layout.addWidget(channel_label)
#             channel_layout.addWidget(toggle_button)

#             layout.addLayout(channel_layout)

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)


class MainControlWindow(QMainWindow):
    def __init__(self, status_dict, run_step_callback):
        super().__init__()
        self.setMinimumSize(QSize(600, 500))
        self.setWindowTitle("AutoSynth Control")

        self.toggle_buttons = {}
        main_layout = QVBoxLayout()

        #3*5 Layout
        steps_layout = QGridLayout()
        self.step_buttons = []
        for i in range(15):
            step_button = StepButton(i)
            self.step_buttons.append(step_button)
            steps_layout.addWidget(step_button, i // 5, i % 5)

        main_layout.addLayout(steps_layout)


        #Channel Toggle Buttons
        channels_layout = QVBoxLayout()
        for channel_name in status_dict:
            channel_label = QLabel(channel_name)
            toggle_button = ToggleButton()
            self.toggle_buttons[channel_name] = toggle_button

            channel_layout = QHBoxLayout()
            channel_layout.addWidget(channel_label)
            channel_layout.addWidget(toggle_button)

            channels_layout.addLayout(channel_layout)

        main_layout.addLayout(channels_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect step buttons to the provided callback function
        self.connect_step_buttons(run_step_callback)

    def connect_step_buttons(self, callback):
        for step_button in self.step_buttons:
            step_button.connect_step(callback)