import socket
import threading


class TxRx:
    """Threaded class to control all serial send and receive between server and client"""

    def __init__(self, host, port, buff_size):
        self.port = port
        self.host = host
        self.buff = buff_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self, gpio):
        self.sock.listen(5)
        while True:
            self.client, self.address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address, gpio)).start()

    def listenToClient(self, client, address, gpio):
        while True:
            try:
                data = client.recv(self.buff)
                #Check for priming request from client and send response
                if data=='pr':
                    # Set the response to echo back the recieved data
                    #state = gpio.get_state(gpio.ir_pin)
                    state = 1
                    if state == 1:
                        response = 'r'
                    else:
                        repsonse = 'b'
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

    def sendToClient(self, message):
        try:
            self.client.send(message)
        except OSError:
            print("Failed to send to: ", self.client)

    def close_all(self):
        self.client.close()
