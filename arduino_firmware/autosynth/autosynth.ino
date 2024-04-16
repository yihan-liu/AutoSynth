#include "controller_status.h"

uint8_t *status = AUTOSYN_CONTROLLER_STATUS_INIT;  // TODO

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        uint32_t command_code = Serial.parseInt();

        if (command_code == 1)
        {
            int digit = 0;
            bool channel_status = (status >> digit) & 1;
            digitalWrite(LED_BUILTIN, !channel_status);
            if (channel_status)
            {
                AUTOSYN_CLR_LED_BUILTIN(status);
            }
            else
            {
                AUTOSYN_SET_LED_BUILTIN(status);
            }
        }
        Serial.write((uint8_t *)&status, sizeof(status));
    }
}