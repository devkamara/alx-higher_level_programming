#!/usr/bin/python3
"""
Gets the list of available attributes & methods
"""


def lookup(obj):
    """
    Gets the list of attributes and methods
    and returns the list
    """
    return dir(obj)
