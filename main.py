#Imports
import console_client
from gui_client import start_up

from dearpygui     import core, simple



#Setup server client
HOST = "127.0.0.1"
PORT = 3000

#Setup client | Now you can access client in console_client.client
console_client.client = console_client.Client(HOST, PORT)

#Setup GUI
start_up.start()

#Runtime
core.start_dearpygui()



