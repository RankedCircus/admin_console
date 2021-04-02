#Import the client for access
import console_client

#Import this app
from gui_client import main_app

#Use GUI
from dearpygui import core, simple


def create_status(x, y):
    #Setup login window size
    width  = 250
    height = 150


    #Build window size
    with simple.window(
        "status_window", 
        no_title_bar = True,
        no_close = True,
        no_resize=True,
        autosize=False,
        
        width  = width,
        height = height,

        x_pos = x,
        y_pos = y,
    ):
        #Title
        core.add_text("SERVER STATUS")

        #Server information
        core.add_text("server_info", 
            default_value="\nCurrent Server: {}:{}".format(
                console_client.client.host,
                console_client.client.port,
            ),
            wrap=0
        )


        core.add_text("server_status_padding", default_value="\n\n")


        #Login Status
        core.set_value("server_status_value", "Not connected")
        core.add_text("server_status", source="server_status_value", wrap=0)


