import socket
from _thread import *
from gamesetup import *
import pickle

server = socket.gethostbyname(socket.gethostname())
print("The Server's IPv4 address is:", server)
# Typical port that is open for use; can change accordingly
port = 5555

# Types of connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind our server and port to the socket
# try because the port might be used already
try:
    s.bind((server, port))
except socket.error as e:
    str(e) # to print the error to the screen so we know why it is not working

# to listen for connections
# s.listen opens up the ports so now we can have multiple clients connecting
# if u leave it blank, it will be unlimited number of clients
s.listen(2)
print("Waiting for a connection, Server Started")

# -------------------- Initialise players --------------------
# 2 tuples to represent the starting position of both players
# (x, y, width, height, color, ballx, bally, balldx, balldy, ballrad, ballcol, score)
players = [Player(40, 250, 20, 100, (255, 0, 0), 400, 300, 3, 3, 10, (255, 255, 0)), Player(740, 250, 20, 100, (0, 0, 255), 400, 300, 0, 0, 0, (0, 0, 0))]

# threaded function
def threaded_client(conn, player):
    # conn.send(str.encode("Connected"))
    conn.send(pickle.dumps(players[player]))
    reply = ""

    # want this to run continuously while the client is connected
    while True:
        try:
            # if you're getting any errors: you can just incr the size of the bits
            # e.g. 2048*8 but NOTE larger bits takes longer to send

            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                # print("Received: ", data)
                # print("Sending : ", reply)

            # conn.sendall(str.encode(reply)) # encode string into a bytes object, send over server, then decode ('Security')
            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()

# initiate player
currentPlayer = 0
# continuously look for connections
while True:
    # connection (object), IP address
    conn, addr = s.accept()
    print("Connected to:", addr)

    # call function
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1 # to keep track of current player

    # we dont want the while loop to be stuck in the threaded function as we want the while loop to keep running
    # for e.g. if the while loop calls the threaded function, it will not exit till the threaded function is successful, we do not want this

    # we have multiple connections running at once
    # so we want to start a thread: another process running in the background
    # process 1: while loop (main)
    # process 2: threaded function
