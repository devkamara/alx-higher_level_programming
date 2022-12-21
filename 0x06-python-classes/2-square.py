#!/usr/bin/python3
"""
no module
"""


class Square:
    """
    defines a square by private instance size
    """
    def __init__(self, size=0):
        """
        method that defines properties for object summary

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
