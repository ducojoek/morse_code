import time

from morse_code.arduino_controller import ArduinoVISADevice

lamp = ArduinoVISADevice(ports="ASRL12::INSTR")

crucial_value = 970


def word():
    # functie ontvangt lichtsignalen en vertaalt deze naar dots(1), dash(2), en volgende letter(3).
    # en returned een lijst met

    word = str(0)
    word_list = []
    space = 0
    above_crucial_count = 0
    below_crucial_count = 0
    one_three = 0

    dot_len = 10
    dash_len = 30
    let_len = 20
    space_len = 40

    while space == 0:
        U = int(lamp.get_input_value(channel=1)) - int(lamp.get_input_value(channel=2))
        print(U)
        if U < crucial_value:
            above_crucial_count += 1
            below_crucial_count = 0
            one_three = 0

        if U > crucial_value:
            below_crucial_count += 1

            if dot_len <= above_crucial_count <= dash_len:
                word += str(1)
                print("dot")

            if above_crucial_count >= dash_len:
                word += str(2)
                print("dash")

            if below_crucial_count >= let_len and one_three < 1:
                one_three += 1

            if below_crucial_count >= space_len:
                return word

            above_crucial_count = 0

        time.sleep(0.05)


t = 0
let_list = []
while t < 10000:
    if (
        int(lamp.get_input_value(channel=1)) - int(lamp.get_input_value(channel=2))
        < crucial_value
    ):
        let_list.append(word())
        print(let_list)
    time.sleep(0.01)
    t += 1
