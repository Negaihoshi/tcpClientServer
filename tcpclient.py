import socket
import sys
import re
 
HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
 
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
     
    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()
 
print("Sent: {}".format(data))
InputType = data[0]

#InputSplit = data.strip().split(':')
InputSplit = re.split('[\s\:]', data)

InputFirstNumber = int(InputSplit[1])
InputSecondNumber = int(InputSplit[2])

if InputSplit[0] == '1':
	print('{} + {} = {}'.format(InputFirstNumber,InputSecondNumber,(InputFirstNumber+InputSecondNumber)))
elif InputSplit[0] == '2':
	print('{} - {} = {}'.format(InputFirstNumber,InputSecondNumber,(InputFirstNumber-InputSecondNumber)))
elif InputSplit[0] == '3':
	print('{} * {} = {}'.format(InputFirstNumber,InputSecondNumber,(InputFirstNumber*InputSecondNumber)))
elif InputSplit[0] == '4':
	print('{} / {} = {}'.format(InputFirstNumber,InputSecondNumber,(InputFirstNumber/InputSecondNumber)))

print("Received: {}".format(received))
#print("InputSplit[0] = " + InputSplit[0] + " InputSplit[1] = " + InputSplit[1] + " InputSplit[2] = " + InputSplit[2])