#Encapsulate this code in a function named count, and generalize it so that
#it accepts the string and the letter as arguments.
"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
"""

word = input("Please enter a word: ")
target = input("which letter should I count? ")
count = 0
for letter in word:
    if letter == target:
        count = count + 1
print(count)
