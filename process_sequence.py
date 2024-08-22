from controllers import MainController
import time

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

# Step Functions
def step_1(controller):
    print("Step 1: L1 right close, L2 right close, L5 close; G1 NO, Vac pump off, G5 close, G3 close, G4 close.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L1')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L2')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L5')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G1')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_VAC_PUMP')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G5')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G4')
    time.sleep(120)  # Wait 2 minutes

def step_2(controller):
    print("Step 2: Vac pump on, G1 close.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_VAC_PUMP')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G1')
    time.sleep(30)  # Wait 30 seconds

def step_3(controller):
    print("Step 3: L1 right open, L2 right open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L1')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L2')
    time.sleep(60)  # Wait 1 minute

def step_4(controller):
    print("Step 4: L1 right close, L2 right close, G3 open, heater on up to 95 °C.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L1')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L2')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_HEATER_1')
    time.sleep(120)  # Wait 2 minutes

def step_5(controller):
    print("Step 5: G3 close, L5 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L5')
    time.sleep(30)  # Wait 30 seconds

def step_6(controller):
    print("Step 6: L5 close, G3 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L5')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    time.sleep(120)  # Wait 2 minutes

def step_7(controller):
    print("Step 7: G3 close, L5 open, L6 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L5')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L6')
    time.sleep(30)  # Wait 30 seconds

def step_8(controller):
    print("Step 8: L5 close, G3 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L5')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    time.sleep(90)  # Wait 1.5 minutes

def step_9(controller):
    print("Step 9: G3 close, L5 open, L7 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L5')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L7')
    time.sleep(30)  # Wait 30 seconds

def step_10(controller):
    print("Step 10: L5 close, G3 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L5')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    time.sleep(60)  # Wait 1 minute

def step_11(controller):
    print("Step 11: Heater off, G1 open, vac pump off.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_HEATER_1')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G1')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_VAC_PUMP')
    time.sleep(240)  # Wait 4 minutes

def step_12(controller):
    print("Step 12: G3 close, G4 open, L3 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G4')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L3')
    time.sleep(30)  # Wait 30 seconds

def step_13(controller):
    print("Step 13: G4 close, G3 open.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G4')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    time.sleep(10)  # Wait 10 seconds

def step_14(controller):
    print("Step 14: G3 close, G4 open, L4 open, G2 close.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G3')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G4')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_L4')
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G2')
    time.sleep(20)  # Wait 20 seconds

def step_15(controller):
    print("Step 15: G4 close.")
    controller.toggle_channel('AUTOSYN_CONTROLLER_STATUS_G4')

# Main process execution
def run_process_sequence():
    controller = MainController(SERIAL_PORT, BAUD_RATE)
    
    try:
        controller.run()

        # Execute the process steps in order
        step_1(controller)
        step_2(controller)
        step_3(controller)
        step_4(controller)
        step_5(controller)
        step_6(controller)
        step_7(controller)
        step_8(controller)
        step_9(controller)
        step_10(controller)
        step_11(controller)
        step_12(controller)
        step_13(controller)
        step_14(controller)
        step_15(controller)

    finally:
        controller.close()

if __name__ == '__main__':
    run_process_sequence()
