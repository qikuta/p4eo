"""
 Write a program that reads a file and prints the letters in decreasing order of
 frequency. Your program should convert all the input to lower case and only
 count the letters a-z. Your program should not count spaces, digits,
 punctuation, or anything other than the letters a-z. Find text samples from
 several different languages and see how letter frequency varies between
 languages. Compare your results with the tables at
 wikipedia.org/wiki/Letter_frequencies.
"""
from string import ascii_lowercase

fhand = open("mbox-short.txt")
letterCount = dict()
totalLetters = 0
letterList = list()

for line in fhand:
    lowLine = line.lower()
    for word in lowLine:
        for letter in word:
            if letter in ascii_lowercase:
                totalLetters += 1
                letterCount[letter] = letterCount.get(letter, 0) + 1


for k, v in letterCount.items():
    v = round(((v/totalLetters)*100), 2)
    letterVals = (v, k)
    letterList.append(letterVals)

sortedLetterList = sorted(letterList, reverse=True)


print("% Frequency / Letter:")
for value in sortedLetterList:
    print(value)
