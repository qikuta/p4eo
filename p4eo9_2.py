"""
Write a program that categorizes each mail message by which day of the week the
commit was done. To do this look for lines that start with "From", then look for
the third word and keep a running count of each of the days of the week. At the
end of the program print out the contents of your dictionary
(order does not matter).
"""

fhand = open("mbox-short.txt")
days = dict()

for line in fhand:
    if line.startswith('From'):
        words = line.split()
        try:
            day = words[2]
            days[day] = days.get(day, 0) + 1
        except:
            print("invid 'from' line")
            continue

print(days)
