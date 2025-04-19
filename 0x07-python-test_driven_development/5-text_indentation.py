#!/usr/bin/python3
"""
This  module defines a function that
prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints text with new lines after each
    of these characters: ., ? and :

    Args:
        text (str): the input text

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    i = 0

    while i < len(text):
        new_text += text[i]

        if text[i] in ['.', '?', ':']:
            new_text += "\n\n"
            i += 1

            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1

    lines = [line.strip() for line in new_text.split("\n")]
    result = "\n".join(lines)
    print(result, end="")
