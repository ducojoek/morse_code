import time

import pyvisa
from arduino_controller import ArduinoVISADevice

list_text = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
    "  ",
]
list_morse = [
    "12",
    "2111",
    "2121",
    "211",
    "1",
    "2111",
    "112",
    "1111",
    "11",
    "2111",
    "212",
    "1211",
    "22",
    "21",
    "222",
    "1221",
    "2212",
    "121",
    "111",
    "2",
    "112",
    "1112",
    "122",
    "1221",
    "1211",
    "1122",
    "3",
    "33",
]


def translate_text_to_morse(text):
    position = list_text.index(text)
    morse = list_morse[position]
    return morse


def translate_morse_to_text(morse):
    position = list_morse.index(morse)
    text = list_text[position]
    return text


# translate_text_to_morse("d")
def word_to_morse(word):
    woord = list(f"{word}")
    signaal = []
    for unit in range(0, len(woord)):
        letter_in_morse = translate_text_to_morse(woord[unit])
        signaal.append(letter_in_morse)
    print(signaal)
    return signaal


def signaal_uitzenden():
    morse = word_to_morse("hallo wereld")
    eind_signaal = []
    # print(morse)
    for a in range(0, len(morse)):
        signaal = list(f"{morse[a]}")
        eind_signaal.append(signaal)
    # print(eind_signaal)
    return eind_signaal


def signal_on_off(tijd):
    experiment = ArduinoVISADevice(ports="ASRL4::INSTR")
    experiment.set_output_value(1023)
    tijd = int(tijd)
    print(tijd)
    time.sleep(int(tijd))
    experiment.set_output_value(0)
    time.sleep(0.25)


# ports = list_resources
# # print(ports)
# rm = pyvisa.ResourceManager("@py")
# ports = rm.list_resources()
# print(ports)
eind_signaal = signaal_uitzenden()
# print(eind_signaal)
for unit in range(0, len(eind_signaal)):
    for a in range(0, len(eind_signaal[unit])):
        signal_on_off(eind_signaal[unit][a])
    time.sleep(2)
    print(0)


# experiment = ArduinoVISADevice(ports="ASRL4::INSTR")
# experiment.set_output_value(1023)
# waarde = experiment.get_output_value()
# print(waarde)
# identificatie = experiment.get_identification()
# print(identificatie)
