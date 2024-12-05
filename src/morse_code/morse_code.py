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
]
list_morse = [
    "01",
    "1000",
    "1010",
    "100",
    "0",
    "1000",
    "001",
    "0000",
    "00",
    "1000",
    "101",
    "0100",
    "11",
    "10",
    "111",
    "0110",
    "1101",
    "010",
    "000",
    "1",
    "001",
    "0001",
    "011",
    "0110",
    "0100",
    "0011",
]


def translate_text_to_morse(text):
    position = list_text.index(text)
    morse = list_morse[position]
    print(morse)


# translate_text_to_morse("d")
def word_to_morse(word):
    woord = list(f"{word}")
    signaal = []
    for unit in range(0, len(woord)):
        letter_in_morse = translate_text_to_morse(woord[unit])
        signaal.append(letter_in_morse)
    return signaal


word_to_morse("hello")
