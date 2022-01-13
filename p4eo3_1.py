# pay computation that gives employee 1.5 time/hour after 40 hours

hours = float(input("How many hours did you work? "))
wage = float(input("How much do you make per hour? "))

if hours > 40:
    pay = ((40 * wage) + ((hours - 40) * (1.5 * wage)))

else:
    pay = (hours * wage)

print (pay)
