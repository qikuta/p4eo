"""
Exercise 4: Add code to the above program to figure out who has the most
messages in the file.

After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section [maximumloop]) to
 find who has the most messages and print how many messages the person has.
"""
import operator

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

message_max = max(emails, key=emails.get)
email_max = max(emails.items(), key=operator.itemgetter(1))[1]

#print dictionary in histogram style
#for key in emails:
#    print(key, emails[key])

print(f"{message_max} has the most emails with a total of {email_max}")
