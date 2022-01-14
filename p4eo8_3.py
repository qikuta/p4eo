"""
Exercise 3: Rewrite the guardian code in the above example without two if
statements. Instead, use a compound logical expression using the and logical
operator with a single if statement.
"""

fhand = open('mbox-short-trick.txt')
count = 0
for line in fhand:
    count += 1
    words = line.split()
    # print 'Debug:', words

    #this skips a blank line
    #if len(words) == 0 : continue

    #this skips any line that doesn't start with 'From'
    #if words[0] != 'From' : continue

    if len(words != 0) and words[0] == 'From':
    try:
        print(words[2])
    except:
        print(f"line {count} is less than three words, does not compute")
        continue
    else:
        continue
