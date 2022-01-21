"""
Write a simple program to simulate the operation of the grep command on Unix.
Ask the user to enter a regular expression and count the number of lines that
matched the regular expression

"""

import re
hand = open('mbox.txt')
regExp = input("Enter a regular expression: ")
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(regExp, line):
        count += 1

print(f"mbox.txt has {count} lines that match {regExp}")
