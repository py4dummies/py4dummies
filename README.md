# Py4Dummies
This is meant to help expand the efficiency of developing scripts for Moderation For Dummies.
It includes `py4dummies` (which the repository is named after), a util library for interfacing with the Roblox API, fetching internet content, and other utilities to help with Mod4Dummie's daily activities.

The canonical git repository is located at https://git.bendaws.net/py4dummies/py4dummies, with a mirror avaliable at https://github.com/sirkingbinx/py4dummies.

## Scripts
### Usage
Run any utility script (not modules) with zero arguments for a rundown of what it does and how to use it. Argument hints are formatted as such:
```
Args:
    [script_name].py [argument: type (?)]
```
A `?` at the end of an argument type represents that the argument is optional.

### Formatting
Each script is formatted like this for easy indexing:
```py
# script_name - description of what it does
# (C) Copyright 2026 Ben Daws. BSD-3 License

### HEADER START

"""
This contains a header which is shared by all scripts. It prints out
help details if the script is invoked with no arguments.
"""

### HEADER_END
### SCRIPT_START

"""
Actual script code here.
"""

### SCRIPT_END
```