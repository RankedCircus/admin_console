#Import the client for access
import console_client

#Use GUI
from dearpygui import core, simple




def create_app():
    with simple.window("main_window"):
        core.add_text("Soemthing idk")

        def test():
            console_client.client.client.test()

        core.add_button("test and shit##main_window", callback=test)


    with simple.window("test"):
        core.add_text("Soemthing idk 2")

        def test():
            console_client.client.client.test()

        core.add_button("test and shit##test", callback=test)
    

