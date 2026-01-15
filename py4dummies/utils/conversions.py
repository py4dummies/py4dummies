# py4dummies/utils/conversions.py - Handles errorless conversions for user-inputted stuff
# (C) Copyright 2026 Ben Daws. BSD-3 License

def to_int(number: str, friendly_name = "arg") -> int:
    """
    Converts a string into an integer, and if invalid, exits the program.
    This is mostly designed for CLIs where you can't do anything without
    a valid number.

    Arguments:
        `number` (str): The string to convert into an integer.
        `friendly_name` (str): The human friendly name of your variable.
    
    Returns:
        (int): An integer representing the string passed into the function.
    """
    try:
        real_int = int(number)
        return real_int
    except ValueError:
        print(f"Error: could not convert {friendly_name}={number} to int.")
        exit(1)