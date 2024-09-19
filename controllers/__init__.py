# controllers/__init__.py

from views.main_control_window import MainControlWindow
from models import SerialManager
from .status_manager import StatusManager
from .step_controller import StepController


class MainController:
    def __init__(self, port, baudrate):
        self.serial_manager = SerialManager(port, baudrate)
        self.status_manager = StatusManager()
        self.main_control_window = MainControlWindow(self.status_manager.STATUS_DICT)

        self.connect_toggle_buttons()
        self.connect_step_buttons()

    def connect_toggle_buttons(self):
        # TODO
        for channel_name in self.status_manager.STATUS_DICT:
            self.main_control_window.toggle_buttons[channel_name].clicked.connect(
                lambda _, toggle_channel=channel_name: self.toggle_channel(toggle_channel)
            )

    def connect_step_buttons(self):
        for i, step_button in enumerate(self.main_control_window.step_buttons):
            step_button.clicked.connect(lambda _, step_index=i: self.run_step(step_index))

    def run_step(self, step_index):
        print(f"Running step {step_index + 1}")
        self.step_controller.run_step_1(step_index)

    def toggle_channel(self, toggle_channel):
        encoded_command = self.status_manager.encode(toggle_channel)
        self.serial_manager.write(encoded_command)
        
        # use serial manager to read current system status
        self.serial_manager.read_status()
        self.parse_controller_status(self.serial_manager.status)
        self.update_toggle_buttons()

    def parse_controller_status(self, status_code):
        self.status_manager.parse(status_code)

    def update_toggle_buttons(self):
        for channel_name, channel_status in self.status_manager.status.items():
            self.main_control_window.toggle_buttons[channel_name].setChecked(channel_status)

    def run(self):
        self.serial_manager.connect()
        self.main_control_window.show()

    def close(self):
        self.serial_manager.disconnect()