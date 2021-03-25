import socket


class Client:
    def __init__(self, host, port):
        #Save port info
        self.host = host
        self.port = port

        #Setup client
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self):
        #Bind
        self.socket_client.connect((self.host, self.port))
        

    def test(self):
        print("test")




