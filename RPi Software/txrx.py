import time
import socket
import threading




class TxRx:
    def __init__(self, host, port, buff_size):
        self.port = port
        self.host = host
        self.buff = buff_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        while True:
            try:
                data = client.recv(self.buff)
                if data=='prime':
                    # Set the response to echo back the recieved data
                    response =
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

    def sendToClient(self, client, address, message):
        try:
            client.send(message)
        except OSError:
            
