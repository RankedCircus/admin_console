#Bring in Client
import console_client

#Import GUI components
from gui_client import create_login, create_app

#The initial entry point to the gui
def start():
    #If we don't have an auth token, we need to login
    if console_client.client.auth_token == None:
        create_login()

    #If we have auth token just go
    else:
        create_app()