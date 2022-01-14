"""
Write a function called chop that takes a list and modifies it, removing the
first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list
that contains all but the first and last elements.
"""

fruits = ["apple", "banana", "kiwi", "orange", "mango", "strawberry"]

def chop(list):
    chopList = list[1:(len(list)-1)]
    return None


def middle(list):
    chopList = list[1:(len(list)-1)]
    return chopList

print(middle(fruits))
