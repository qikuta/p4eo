#Exercise 1: Write a while loop that starts at the last character in the string
#and works its way backwards to the first character in the string, printing each
#letter on a separate line, except backwards.

name = "Quentin"
nameLength = (len(name) - 1)

while nameLength > -1:
    print (name[nameLength])
    nameLength -= 1
