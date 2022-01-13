"""
Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
they add a harmless Easter Egg to their program Modify the program that prompts
the user for the file name so that it prints a funny message when the user types
in the exact file name "na na boo boo". The program should behave normally for
all other files which exist and don't exist.
"""

fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU! YOUVE BEEN PUNKED!')
    quit()
else:
    try:
        fhand = open(fname)
    except:
        print('File can not be found: ', fname)
        quit()

subCount = 0
for line in fhand:
    if line.startswith('Subject:'):
        subCount += 1



print("there are ", subCount, "subject lines in file ", fname)
