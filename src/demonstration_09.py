"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""


def mapping(letters):
    # Your code here
    new_dict = {}
    for letter in letters:
        new_dict[letter] = letter.upper()
    return new_dict


def mapping_dict_comprehension(letters):
    return {letter: letter.upper() for letter in letters}


print(mapping(["p", "s"]))
print(mapping_dict_comprehension(["a", "b", "c"]))
print(mapping(["a", "v", "y", "z"]))

"""
the following solutions are wrong
"""
# def mapping_odd(letters):
#     caps = [let.upper() for let in letters.upper()]
#     return letters, caps

# def mapping_odd(letters):
#     caps = letters.upper()
#     return caps

# def mapping_short_2(letters):
#     return dict(letters, letters.upper())
