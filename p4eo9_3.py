"""
Write a program to read through a mail log, build a histogram using a
dictionary to count how many messages have come from each email address,
and print the dictionary.
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

#print dictionary in histogram style
for key in emails:
    print(key, emails[key])
