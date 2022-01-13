# rewriting program for pay computation this time with a function 'computepay'


def computepay():
    try:
     hours = float(input("How many hours did you work? "))
     wage = float(input("How much do you make per hour? "))
    except:
        print ("ERROR: Please enter numbers only")
        quit()

    if hours > 40:
        pay = ((40 * wage) + ((hours - 40) * (1.5 * wage)))

    else:
        pay = (hours * wage)

    return pay

print(computepay())
