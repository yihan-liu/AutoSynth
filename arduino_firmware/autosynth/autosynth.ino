#include "controller_status.h"
#include "valve_pin.h"

uint32_t status = 0;

void setup()
{
    pinMode(PIN_L1, OUTPUT);
    pinMode(PIN_L2, OUTPUT);
    pinMode(PIN_L3, OUTPUT);
    pinMode(PIN_L4, OUTPUT);
    pinMode(PIN_L5, OUTPUT);
    pinMode(PIN_L6, OUTPUT);
    pinMode(PIN_L7, OUTPUT);
    pinMode(PIN_G1, OUTPUT);
    pinMode(PIN_G2, OUTPUT);
    pinMode(PIN_G3, OUTPUT);
    pinMode(PIN_G4, OUTPUT);
    pinMode(PIN_G5, OUTPUT);
    pinMode(PIN_HEATER_1, OUTPUT);
    pinMode(PIN_VAC_PUMP, OUTPUT);
    pinMode(PIN_VALVE_15, OUTPUT);
    pinMode(PIN_VALVE_16, OUTPUT);
    pinMode(PIN_VALVE_17, OUTPUT);
    pinMode(PIN_VALVE_18, OUTPUT);
    pinMode(PIN_VALVE_19, OUTPUT);
    pinMode(PIN_VALVE_20, OUTPUT);
    pinMode(PIN_VALVE_21, OUTPUT);
    pinMode(PIN_VALVE_22, OUTPUT);
    pinMode(PIN_VALVE_23, OUTPUT);
    pinMode(PIN_VALVE_24, OUTPUT);
    pinMode(PIN_VALVE_25, OUTPUT);
    pinMode(PIN_VALVE_26, OUTPUT);
    pinMode(PIN_VALVE_27, OUTPUT);
    pinMode(PIN_VALVE_28, OUTPUT);
    pinMode(PIN_VALVE_29, OUTPUT);
    pinMode(PIN_VALVE_30, OUTPUT);
    pinMode(PIN_VALVE_31, OUTPUT);
    pinMode(PIN_VALVE_32, OUTPUT);

    Serial.begin(9600);
    while (!Serial);
}

void loop()
{
    if (Serial.available() >= 4)
    {
        uint32_t command_code;
        Serial.readBytes((char*)&command_code, sizeof(command_code));

        // Toggle the corresponding bit in the status based on the received command code
        status ^= command_code;
        
        for (int i = 0; i < 32; i++)
        {
            uint32_t mask = 1 << i;
            bool pin_status = status & mask;
            int pin_number = PIN_VALVE_1 + i;
            digitalWrite(pin_number, pin_status);
        }

        Serial.write((uint8_t *)&status, sizeof(status));
    }
}