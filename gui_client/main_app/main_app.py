#Import the client for access
import console_client

from .widgets import menu

#Use GUI
from dearpygui import core, simple






def create_app():
    with simple.window("main_window"):
        #Create Menu
        menu.create_menu()
        core.add_text("hi")


    core.set_primary_window("main_window", True)
    

