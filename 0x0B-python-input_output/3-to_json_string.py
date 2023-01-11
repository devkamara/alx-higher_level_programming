#!/usr/bin/python3
""" function returning JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Return JSON representation of a string object."""
    return json.dumps(my_obj)
