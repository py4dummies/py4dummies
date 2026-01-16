# group_members.py - Output group members into a file
# (C) Copyright 2026 Ben Daws. BSD-3 License

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

### SCRIPT START
from py4dummies import *
from py4dummies.utils import *

group_id = to_int(args[1], "group_id")
output_filename = args[2] if len(args) > 2 else f"group-{group_id}.txt"

with open(output_filename, "a") as file:
    def output_member(member: FilterableItem[RBXUser]):
        fmt = f"{member.value.display_name} (@{member.value.user_name}) - {member.value.url}"
        print(fmt)
        file.writelines(fmt)

    group = RBXGroup(group_id)
    group.members.pass_through(output_member)
### SCRIPT END