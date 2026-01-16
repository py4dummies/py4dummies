# py4dummies/tests/get_user.py
# (C) Copyright 2026 Ben Daws. BSD-3 License

if __name__ != "__main__":
    ImportError("This is not a module. Please run this from the terminal.")

from py4dummies import *

if can_connect():
    print("can reach roblox? True")
else:
    print("can reach roblox: False")
    exit(1)