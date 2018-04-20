import socket
import threading


class TxRx:
    """Threaded class to control all serial send and receive between server and client"""

    def __init__(self, host, port, buff_size):
        #Set up the socket and bind to port
        self.port = port
        self.host = host
        self.buff = buff_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self, gpio):
        #Listen for incoming connections
        self.sock.listen(5)
        print("Listening for connections from clients")
        self.client, self.address = self.sock.accept()
        self.client.settimeout(60)
        #Create new thread for each connected client
        threading.Thread(target = self.listenToClient,args = (self.client, self.address, gpio)).start()

    def listenToClient(self, client, address, gpio):
        #Listen to client for incoming message and respond
        print("Connected to client: ", client, " @ IP: ", address)
        self.sendToClient("You've just connected to the Pi Timing Box!")
        while True:
            try:
                data = client.recv(self.buff)
                print("Data received: ", data)
                #Check for priming request from client and send response
                if data==b'pr':
                    # Set the response to echo back the recieved data
                    state = gpio.get_state(gpio.ir_pin)
                    #state = 1
                    if state == 1:
                        response = b'r'
                        print("Sending response: ", response)
                    else:
                        repsonse = b'b'
                        print("Sending response: ", response)
                    self.sendToClient(response)
                else:
                    raise OSError('Client disconnected')
            except OSError as e:
                print("Closing connection due to error: ", e)
                client.close()
                return False

    def sendToClient(self, message):
        try:
            print("Sent ",message, " to client")
            self.client.send(message)
        except OSError as e:
            print("Failed to send to: ", self.client, " due to error: ", e)

    def close_all(self):
        self.client.close()
