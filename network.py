import socket
import pickle # serialised objects, turn into bytes 0 and 1, send over network, decompose and turn it back into onjects

serverip = input("Enter the Server's IPv4 address: ")

# makes it easier to reuse the class in the future
class Network:
    def __init__(self): # initialisation function
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # same argument as server socket
        # self.server = "SERVER_IP" # has to be the same as the one in server.py
        self.server = serverip # input server's IPV4 addr
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        # print(self.id)

    def getP(self):
        return self.p

    def connect(self): # define connect function
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    # data parameter as a string
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

# For testing purposes
# Run server.py first!
# n = Network()
# print(n.send("Hello"))
# print(n.send("World!"))
# network sending, receiving and serving working