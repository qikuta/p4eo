"""
Exercise 1: Revise a previous program as follows: Read and parse the "From"
lines and pull out the addresses from the line. Count the number of messages
from each person using a dictionary.

After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the
list in reverse order and print out the person who has the most commits.
"""

fhand = open("mbox.txt")
emails = dict()
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        try:
            email = words[1]
            emails[email] = emails.get(email, 0) + 1
        except:
            print("***INVALID LINE***")
            continue

email_list = list()
for k, v in emails.items():
    revItems = (v, k)
    email_list.append(revItems)

sortedEmailList = sorted(email_list, reverse=True)

for value in sortedEmailList:
    print(value)
