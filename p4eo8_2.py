"""
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])

Exercise 2: Figure out which line of the above program is still not properly
guarded. See if you can construct a text file which causes the program to fail
and then modify the program so that the line is properly guarded and test it to
make sure it handles your new text file.
"""

fhand = open('mbox-short-trick.txt')
count = 0
for line in fhand:
    count += 1
    words = line.split()
    # print 'Debug:', words

    #this skips a blank line
    if len(words) == 0 : continue

    #this skips any line that doesn't start with 'From'
    if words[0] != 'From' : continue

    try:
        print(words[2])
    except:
        print(f"line {count} is less than three words, does not compute")
        continue
