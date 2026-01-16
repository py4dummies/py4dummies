# user_friends.py - Outputs all friends of a user into a file named friends-(id).txt.
# (C) Copyright 2026 Ben Daws. BSD-3 License

desc = """
Outputs all friends of a user into a file named friends-(id).txt.

Usage:
    user_friends.py [user_id: int] [output_file: str?]
"""

# This snippet returns the description of a script if invoked with no arguments
from sys import argv as args

if len(args) < 2:
    print(desc)
    exit(0)

### SCRIPT START
import asyncio
from py4dummies import *
from py4dummies.utils import *
from py4dummies.classes import *

user_id = to_int(args[1], "user_id")
output_filename = args[2] if len(args) > 2 else f"friends-{user_id}.txt"

with open(output_filename, "a") as file:
    def output_member(user__: FilterableItem[RBXUser]):
        user = user__.value

        fmt = f"https://www.roblox.com/users/profile/{user.id}\n"
        print(fmt)
        file.writelines(fmt)
    
    user = RBXUser.from_id(user_id)

    user.friends.pass_through(output_member)
### SCRIPT END