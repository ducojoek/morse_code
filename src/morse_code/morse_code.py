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


word_to_morse("hello world")
