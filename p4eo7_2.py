#Write a program to prompt for a file name, and then read through the file and
#look for lines of the form:
#X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
#the line to extract the floating-point number on the line. Count these lines
#and then compute the total of the spam confidence values from these lines.
#When you reach the end of the file, print out the average spam confidence.

fname = input("Enter a file name: ")
fhand = open(fname)

spamSum = 0
spamCount = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        lineIndex = line.find(':')
        spamSum = spamSum + float(line[lineIndex+1:])
        spamCount += 1

avSpam = spamSum / spamCount
print(spamCount)
print(spamSum)
print("average spam:", avSpam)
