import time

import pyvisa

from morse_code.arduino_controller import ArduinoVISADevice

lamp = ArduinoVISADevice(ports="ASRL12::INSTR")
lamp.set_output_value(value=1023)
t = 0
while t < 10000:
    val = int(lamp.get_input_value(channel=1)) - int(lamp.get_input_value(channel=2))
    print(val)
    t += 1
    time.sleep(0.1)
