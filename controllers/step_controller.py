# controllers/step_controller.py

import time

class StepController:

    def __init__(self, serial_manager):
        self.serial_manager = serial_manager

    def send_command(self, command_code):
        self.serial_manager.send_command(command_code)

    def step_1(self):
        """Step 1: L1 right close, L2 right close, L5 close; G1 NO, Vac pump off, G5 close, G3 Close, G4 close. (~ 2 mins)"""
        print("Executing Step 1...")
        self.send_command(0x00000001)  # AUTOSYN_CONTROLLER_STATUS_L1 (L1 close)
        self.send_command(0x00000002)  # AUTOSYN_CONTROLLER_STATUS_L2 (L2 close)
        self.send_command(0x00000010)  # AUTOSYN_CONTROLLER_STATUS_L5 (L5 close)
        self.send_command(0x00000080)  # AUTOSYN_CONTROLLER_STATUS_G1 (G1 NO)
        self.send_command(0x00002000)  # AUTOSYN_CONTROLLER_STATUS_VAC_PUMP (Vac pump off)
        self.send_command(0x00000800)  # AUTOSYN_CONTROLLER_STATUS_G5 (G5 close)
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 close)
        self.send_command(0x00000400)  # AUTOSYN_CONTROLLER_STATUS_G4 (G4 close)
        time.sleep(120)

    def step_2(self):
        """Step 2: Vac pump on, G1 Close. (~ 30s)"""
        print("Executing Step 2...")
        self.send_command(0x00002000)  # AUTOSYN_CONTROLLER_STATUS_VAC_PUMP (Vac pump on)
        self.send_command(0x00000080)  # AUTOSYN_CONTROLLER_STATUS_G1 (G1 close)
        time.sleep(30)

    def step_3(self):
        """Step 3: L1 right open; L2 right open. (1 min)"""
        print("Executing Step 3...")
        self.send_command(0x00000001)  # AUTOSYN_CONTROLLER_STATUS_L1 (L1 open)
        self.send_command(0x00000002)  # AUTOSYN_CONTROLLER_STATUS_L2 (L2 open)
        time.sleep(60)

    def step_4(self):
        """Step 4: L1 right close, L2 right close, G3 open, heater on up to 95°C. (2 min)"""
        print("Executing Step 4...")
        self.send_command(0x00000001)  # AUTOSYN_CONTROLLER_STATUS_L1 (L1 close)
        self.send_command(0x00000002)  # AUTOSYN_CONTROLLER_STATUS_L2 (L2 close)
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 open)
        self.send_command(0x00001000)  # AUTOSYN_CONTROLLER_STATUS_HEATER_1 (Heater on)
        time.sleep(120)

    def step_5(self):
        """Step 5: G3 close, L5 open. (30s)"""
        print("Executing Step 5...")
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 close)
        self.send_command(0x00000010)  # AUTOSYN_CONTROLLER_STATUS_L5 (L5 open)
        time.sleep(30)

    def step_6(self):
        """Step 6: L5 close, G3 open. (2 min)"""
        print("Executing Step 6...")
        self.send_command(0x00000010)  # AUTOSYN_CONTROLLER_STATUS_L5 (L5 close)
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 open)
        time.sleep(120)

    def step_7(self):
        """Step 7: G3 close, L5 open, L6 open. (30s)"""
        print("Executing Step 7...")
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 close)
        self.send_command(0x00000010)  # AUTOSYN_CONTROLLER_STATUS_L5 (L5 open)
        self.send_command(0x00000020)  # AUTOSYN_CONTROLLER_STATUS_L6 (L6 open)
        time.sleep(30)

    def step_8(self):
        """Step 8: L5 close, G3 open. (1.5 mins)"""
        print("Executing Step 8...")
        self.send_command(0x00000010)  # AUTOSYN_CONTROLLER_STATUS_L5 (L5 close)
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 open)
        time.sleep(90)

    def step_9(self):
        """Step 9: G3 close, L5 open, L7 open. (30s)"""
        print("Executing Step 9...")
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 close)
        self.send_command(0x00000010)  # AUTOSYN_CONTROLLER_STATUS_L5 (L5 open)
        self.send_command(0x00000040)  # AUTOSYN_CONTROLLER_STATUS_L7 (L7 open)
        time.sleep(30)

    def step_10(self):
        """Step 10: L5 close, G3 open. (1 min)"""
        print("Executing Step 10...")
        self.send_command(0x00000010)  # AUTOSYN_CONTROLLER_STATUS_L5 (L5 close)
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 open)
        time.sleep(60)

    def step_11(self):
        """Step 11: Heater off, G1 open, vac pump off. (4 min)"""
        print("Executing Step 11...")
        self.send_command(0x00001000)  # AUTOSYN_CONTROLLER_STATUS_HEATER_1 (Heater off)
        self.send_command(0x00000080)  # AUTOSYN_CONTROLLER_STATUS_G1 (G1 open)
        self.send_command(0x00002000)  # AUTOSYN_CONTROLLER_STATUS_VAC_PUMP (Vac pump off)
        time.sleep(240)

    def step_12(self):
        """Step 12: G3 close, G4 open, L3 open. (30s)"""
        print("Executing Step 12...")
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 close)
        self.send_command(0x00000400)  # AUTOSYN_CONTROLLER_STATUS_G4 (G4 open)
        self.send_command(0x00000004)  # AUTOSYN_CONTROLLER_STATUS_L3 (L3 open)
        time.sleep(30)

    def step_13(self):
        """Step 13: G4 close, G3 open. (10s)"""
        print("Executing Step 13...")
        self.send_command(0x00000400)  # AUTOSYN_CONTROLLER_STATUS_G4 (G4 close)
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 open)
        time.sleep(10)

    def step_14(self):
        """Step 14: G3 close, G4 open, L4 open, G2 close. (20s)"""
        print("Executing Step 14...")
        self.send_command(0x00000200)  # AUTOSYN_CONTROLLER_STATUS_G3 (G3 close)
        self.send_command(0x00000400)  # AUTOSYN_CONTROLLER_STATUS_G4 (G4 open)
        self.send_command(0x00000008)  # AUTOSYN_CONTROLLER_STATUS_L4 (L4 open)
        self.send_command(0x00000100)  # AUTOSYN_CONTROLLER_STATUS_G2 (G2 close)
        time.sleep(20)

    def step_15(self):
        """Step 15: G4 close (optional step)"""
        print("Executing Step 15...")
        self.send_command(0x00000400)  # AUTOSYN_CONTROLLER_STATUS_G4 (G4 close)
        time.sleep(60)

    def run_step(self, step_index):
        """Runs the appropriate step based on the step index."""
        if step_index == 0:
            self.step_1()
        elif step_index == 1:
            self.step_2()
        elif step_index == 2:
            self.step_3()
        elif step_index == 3:
            self.step_4()
        elif step_index == 4:
            self.step_5()
        elif step_index == 5:
            self.step_6()
        elif step_index == 6:
            self.step_7()
        elif step_index == 7:
            self.step_8()
        elif step_index == 8:
            self.step_9()
        elif step_index == 9:
            self.step_10()
        elif step_index == 10:
            self.step_11()
        elif step_index == 11:
            self.step_12()
        elif step_index == 12:
            self.step_13()
        elif step_index == 13:
            self.step_14()
        elif step_index == 14:
            self.step_15()
        else:
            print(f"Undetermined the step")