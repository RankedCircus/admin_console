from console_client import Client

def init(host, port):
    global client 
    client = Client(host, port)
