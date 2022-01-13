fname = input("Enter a file name: ")

try:
    #this handle allows you to get the file, it's like a wrapper 
    fhand = open(fname)
except:
    print("file can not be opened: ", fname)
    exit()

count = 0
subCount = 0

for line in fhand:
    if line.startswith('Subject:'):
        subCount += 1
    count+=1

print("The file ", fname, "contains ", count, "lines of text. Of which", subCount, "begin with 'subject'")
print("That means ", (subCount/count)*100, "% lines begin with 'subject' ")
