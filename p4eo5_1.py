# gather numbers from user until enters 'done', prints out stats about the numbers entered.

print("Enter numbers. Enter 'done' when finished. ")

number = input("enter a number: ")
count = 0
total = 0

if number == 'done':
    quit()

maxnum = float(number)
minnum = float(number)
while number != 'done':
        try:
            number = float(number)
        except:
            print("bad input. numbers only.")
            quit()
        total += number
        count += 1
        if number > maxnum:
            maxnum = number
        if number < minnum:
            minnum = number

        number = input("enter a number: ")

average = (total / count)
print("total:", total, "count:", count, "average:", average, "max number: ", maxnum, "min number", minnum)
