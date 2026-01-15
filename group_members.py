# group_members.py - Output group members into a file
# (C) Copyright 2026 Ben Daws. BSD-3 License

### HEADER START
desc = """
Outputs all group members into a file named group-(id).txt.

Usage:
    group_members.py [group_id: int] [output_file: str?]
"""

# This snippet returns the description of a script if invoked with no arguments
from sys import argv as args

if len(args) < 2:
    print(desc)
    exit(0)

### HEADER END
### SCRIPT START

import asyncio
from py4dummies import *
from py4dummies.utils import *
from py4dummies.classes import *

group_id = to_int(args[1], "group_id")
output_filename = args[2] if len(args) > 2 else f"group-{group_id}.txt"

with open(output_filename, "a") as file:
    def output_member(member: RBXUser):
        fmt = f"{member.display_name} (@{member.user_name}) - {member.url}"
        print(fmt)
        file.writelines(fmt)

    group = RBXGroup(group_id)

    asyncio.run(group.each_member(output_member, 25))

### SCRIPT END