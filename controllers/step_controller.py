# controllers/step_controller.py
import time

class StepController:

    def __init__(self, serial_manager):
        self.serial_manager = serial_manager

    def send_command(self, command_code):
        self.serial_manager.send_command(command_code)

    def step_1(self):
        print("Executing Step 1")
        self.send_command(0x00000001)
        self.send_command(0x00000002)
        self.send_command(0x00000010)
        self.send_command(0x00000080)
        self.send_command(0x00002000)
        self.send_command(0x00000800)
        self.send_command(0x00000200)
        self.send_command(0x00000400)
        time.sleep(120)

    def step_2(self):
        print("Executing Step 2")
        self.send_command(0x00002000)
        self.send_command(0x00000080)
        time.sleep(30)

    def step_3(self):
        print("Executing Step 3")
        self.send_command(0x00000001)
        self.send_command(0x00000002)
        time.sleep(60)
    
    def run_step_1(self, step_index):
        if step_index == 0:
            self.step_1()
        elif step_index == 1:
            self.step_2()
        else:
            print(f"Step {step_index + 1} is not implemented")
        


