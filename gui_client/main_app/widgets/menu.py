#Import the client for access
import console_client

#Use GUI
from dearpygui  import core, simple
from gui_client import login
#Bring in widgets
from .edit_token import *



def signout():
    #Reset Token
    console_client.client.signout()

    #cLEAR WINDOWQ
    core.delete_item("main_window")
    core.delete_item("server_output")
    core.delete_item("server_input")

    #Go to login
    login.create_login()




def create_menu():
    with simple.menu_bar("main_menu_bar", parent="main_window"):
        with simple.menu("token_menu", label="Settings"):
            core.add_menu_item("signout_button", callback=signout, parent="token_menu", label="Sign Out")
            core.add_menu_item("edit_token_menu", callback=create_widget, parent="token_menu", label="Edit Token")
