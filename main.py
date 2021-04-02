#Imports
import threading
import console_client

from gui_client import start_up
from dearpygui  import core, simple

#Setup server client | Bring these to env vars later
HOST = "127.0.0.1"
PORT = 6210


def start(HOST, PORT):
    #Create the network
    console_client.client = console_client.Client(HOST, PORT)
    network_thread = threading.Thread(target = console_client.client.connect)
    network_thread.start()

    #Start up gui
    start_up.start()

    #Runtime
    core.start_dearpygui()



start(HOST, PORT)