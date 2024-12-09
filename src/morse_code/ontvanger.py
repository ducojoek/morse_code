import time

from morse_code.arduino_controller import ArduinoVISADevice
from morse_code.morse_cod import morse_to_word

lamp = ArduinoVISADevice(ports="ASRL12::INSTR")

crucial_value = 970


def word():
    # functie ontvangt lichtsignalen en vertaalt deze naar dots(1), dash(2), en volgende letter(3).
    # en returned een lijst met

    word = str(0)
    space = 0
    above_crucial_count = 0
    below_crucial_count = 0

    dot_len = 1
    dash_len = 8
    let_len = 8

    while space == 0:
        U = int(lamp.get_input_value(channel=1)) - int(lamp.get_input_value(channel=2))
        print(U)
        if U < crucial_value:
            above_crucial_count += 1
            below_crucial_count = 0

        if U > crucial_value:
            below_crucial_count += 1

            if dot_len <= above_crucial_count <= dash_len:
                word += str(1)
                print("dot")

            if above_crucial_count >= dash_len:
                word += str(2)
                print("dash")

            if below_crucial_count >= let_len:
                return word

            above_crucial_count = 0

        time.sleep(0.05)


t = 0
space_len = 50
below_count = 0
let_list = []
while t < 1000:
    if (
        int(lamp.get_input_value(channel=1)) - int(lamp.get_input_value(channel=2))
        < crucial_value
    ):
        if below_count > space_len:
            let_list.append(str(3))
        below_count = 0
        let_list.append(word())
        print(let_list)
    time.sleep(0.01)

    if (
        int(lamp.get_input_value(channel=1)) - int(lamp.get_input_value(channel=2))
        > crucial_value
    ):
        below_count += 1

    t += 1

let_list = [int(i) for i in let_list]
let_list = [str(r) for r in let_list]
print(morse_to_word(let_list))
