#Imports
import console_client
import gui_client

from dearpygui     import core



#Setup server client
HOST = "127.0.0.1"
PORT = 3000

#Setup client | Now you can access client in console_client.client
console_client.init(HOST, PORT)



#Setup GUI
gui_client.create_login()



#Runtime
core.start_dearpygui()

