#Import the client for access
import console_client

#Import this app
from gui_client import main_app

#Use GUI
from dearpygui import core, simple

#Setup login call back
def request_login():
    #Simulate a request check
    console_client.client.test()

    #Now finish 
    login_succeeded()


def login_succeeded():
    #Remove login, and add main window
    core.delete_item("login_window")

    #Create the app
    main_app.create_app()


#Setup the login page
def create_login():
    with simple.window("login_window"):
        core.add_text("LOGIN")

        core.add_input_text("login_input", hint="auth key", password=True, label="")

        core.add_button("login_button", callback=request_login)

