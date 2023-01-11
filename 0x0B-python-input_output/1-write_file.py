#!/usr/bin/python3
"""Defines a file writing func."""


def write_file(filename="", text=""):
    """write a string to a UTF-8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)