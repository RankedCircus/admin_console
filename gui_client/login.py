#Import the client for access
from console_client import setup_client as client

#Use GUI
from dearpygui import core, simple

#Setup the login page
def create_login():
    with simple.window("login_window"):
        core.add_text("hey")

        def test():
            client.client.test()

        core.add_button("click me", callback=test)