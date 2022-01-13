# gather numbers from user until enters 'done', prints out stats about the numbers entered.

print("Enter numbers. Enter 'done' when finished. ")

number = input("enter a number: ")
maxnum = float(number)
minnum = float(number)
count = 0
total = 0

while number != 'done':
    if number == 'done':
        quit()
    else:
        number = float(number)
        total += number
        count += 1
        if number > maxnum:
            maxnum = number
        if number < minnum:
            minnum = number

        number = input("enter a number: ")

average = (total / count)
print("total:", total, "count:", count, "average:", average, "max number: ", maxnum, "min number", minnum)
