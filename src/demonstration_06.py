"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""


def compare_xo(txt):
    # Your code here
    return txt.lower().count("x") == txt.lower().count("o")


print(f"XO(\"ooxx\") ➞ True {compare_xo('ooxx')}")
print(f"XO(\"xooxx\") ➞ False {compare_xo('xooxx')}")
print(f"XO(\"ooxXm\") ➞ True (Case insensitive) {compare_xo('ooxXm')}")
print(f"XO(\"zpzpzpp\") ➞ True (Returns True if no x and o) {compare_xo('zpzpzpp')}")
print(f"XO(\"zzoo\") ➞ False {compare_xo('zzoo')}")
