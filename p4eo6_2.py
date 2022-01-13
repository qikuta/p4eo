#Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# this will print fruit entirely. fruit[:] just means print the entire string
# if there are numbers in [:] such as [1:2] a print statement will only print
# the character that is equal to the second character and less than the
# third character

fruit = "Banana"
print(fruit[:])

#prints the 2nd character, stops at the third character
print(fruit[1:2])

#stops printing on the 3rd character
print(fruit[:2])

#begins printing on the 3rd character
print(fruit[2:])
