"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters "done". Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum numbers
after the loop completes.
"""

# gather numbers from user until enters 'done', prints out stats about the numbers entered.

print("Enter numbers. Enter 'done' when finished. ")

number = input("enter a number: ")
count = 0
total = 0

if number == 'done':
    quit()

numList = []
while number != 'done':
        try:
            number = float(number)
        except:
            print("bad input. numbers only.")
            quit()
        total += number
        count += 1
        numList.append(number)
        number = input("enter a number: ")

maxNum = max(numList)
minNum = min(numList)

average = (total / count)
print("total:", total, "count:", count, "average:", average, "max number: ", maxNum, "min number", minNum)
