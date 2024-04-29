# controllers/status.py

import re
import math


class StatusManager:
    def __init__(self):
        with open("./arduino_firmware/autosynth/controller_status.h", 'r') as f:
            content = f.read()

        status_pattern = re.compile(r"#define\s+(AUTOSYN_CONTROLLER_STATUS_\w+)\s+(\w+)")
        self.STATUS_DICT = {}
        for match in status_pattern.finditer(content):
            channel_name = match.group(1)
            if channel_name != "AUTOSYN_CONTROLLER_STATUS_INIT":
                channel_status = int(match.group(2), 0)
                self.STATUS_DICT[channel_name] = channel_status

        self.status = {}
        for channel_name in self.STATUS_DICT.keys():
            self.status[channel_name] = 0

    def encode(self, toggle_channel):
        encoded_value = 0
        for channel, _ in reversed(self.STATUS_DICT.items()):
            encoded_value <<= 1
            if channel == toggle_channel:
                encoded_value |= 1
        print(bin(encoded_value))
        return encoded_value

    def parse(self, status_code):
        # Convert status code to a binary value that has the same length as status_dict,
        # all values are initialized as 0
        status_code_bin = bin(status_code)[2:].zfill(len(self.STATUS_DICT))

        # Convert 
        for channel_name, channel_value in self.STATUS_DICT.items():
            channel_index = len(self.STATUS_DICT) - int(math.log2(channel_value)) - 1
            self.status[channel_name] = status_code_bin[channel_index] == '1'

        print(f"Status code: {status_code_bin}")