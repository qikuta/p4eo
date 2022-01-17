"""
Exercise 5: This program records the domain name (instead of the address) where
the message was sent from instead of who the mail came from (i.e., the whole
email address). At the end of the program, print out the contents of your dictionary.
"""

fhand = open("mbox.txt")
domains = dict()
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        try:
            email = words[1]
            domain = email[(email.find('@')+1):]
            domains[domain] = domains.get(domain, 0) + 1
        except:
            print("ERROR")

print(domains)
