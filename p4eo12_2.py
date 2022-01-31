"""
Exercise 2: Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number of
characters and display the count of the number of characters at the end of the
document.

"""
import socket
import requests

try:
    sockInput = input("Enter a URL: ")
    response = requests.get(sockInput)
    if response.status_code == 200:
        sockConnect = sockInput.split('/')
        sockConnectHost = sockConnect[2]
except:
    print("Incorrectly formatted URL. Please ensure form follows https:// and/or exists. Try again.")
    exit()


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((sockConnectHost, 80))
cmd = f'GET {sockInput} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0
dataRecord = ''
while True:
    data = mysock.recv(512)
    count+= len(data)
    if (len(data) < 1):
        break
    dataRecord += data.decode()
mysock.close()

#use the below code to check if 3000 characters actually print
"""
position = 0
for char in dataRecord[:3000]:
    position += 1
    print(char)
    print(position)
"""
print(dataRecord[:3000])
dataLength = len(dataRecord)
print(f"Printed 3000 characters out of {dataLength}")
