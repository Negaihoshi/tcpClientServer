import socketserver
import re
 
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
The RequestHandler class for our server.
It is instantiated once per connection to the server, and must
override the handle() method to implement communication to the
client.
"""
     
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        ClientData = str(self.data)
        InputSplit = ClientData.strip('b').strip('\'')
        InputSplit = re.split('[\s\:]', InputSplit)
        print(InputSplit)
        InputFirstNumber = int(InputSplit[1])
        InputSecondNumber = int(InputSplit[2])
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

        if InputSplit[0] == '1':
            OutputResult = InputFirstNumber + InputSecondNumber
            Symbol = '+'
        elif InputSplit[0] == '2':
            OutputResult = InputFirstNumber - InputSecondNumber
            Symbol = '-'
        elif InputSplit[0] == '3':
            OutputResult = InputFirstNumber * InputSecondNumber
            Symbol = '*'
        elif InputSplit[0] == '4':
            OutputResult = InputFirstNumber / InputSecondNumber
            Symbol = '/'
        print('{} {} {} = {}'.format(InputFirstNumber,Symbol,InputSecondNumber,OutputResult))
        #self.request.sendall('{} / {} = {}'.format(InputFirstNumber,InputSecondNumber,OutputResult)
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
     
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
     
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()