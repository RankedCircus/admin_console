#Import the client for access
from console_client import setup_client as client

#Import this app
from gui_client import main_app

#Use GUI
from dearpygui import core, simple

#Setup login call back
def finish_login():
    #Stop the gui, create the main app
    core.delete_item("login_window")

    #Create the app
    main_app.create_app()


#Setup the login page
def create_login():
    with simple.window("login_window"):
        core.add_text("LOGIN")

        def login_test():
            #Simulate call back
            client.client.test()

            #Now proceed
            finish_login()

        core.add_button("login_button", callback=login_test)

