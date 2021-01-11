"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""


def sort_by_length_nested_func(lst):
    # Your code here
    def find_len(string):
        return len(string)

    lst.sort(key=find_len)
    return lst


def sort_by_length_short(lst):
    lst.sort(key=len)
    return lst


def sort_by_length_lambda(lst):
    lst.sort(key=lambda string: len(string))
    return lst


def sort_by_length_immutable(lst):
    return sorted(lst, key=len)


print(sort_by_length_immutable(["a", "ccc", "dddd", "bb"]))
print(sort_by_length_lambda(["apple", "pie", "shortcake"]))
print(sort_by_length_lambda(["may", "april", "september", "august"]))
print(sort_by_length_lambda([]))
