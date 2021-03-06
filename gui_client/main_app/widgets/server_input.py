#Import the client for access
import console_client

#Use GUI
from dearpygui  import core, simple

#Quick hack to add data to chat
from .server_output import add_chat

def enter_button():
    #Get text
    text = core.get_value("input_text_value")

    #Fail out if we're not connected
    if console_client.client.connected != True:
        #Add error | Maybe we don't say shit here?
        add_chat("ERROR", "Can't send messages if not connected")

        return

    #Send it lmao
    success, message = console_client.client.send_command(text)

    if success != True:
        add_chat("ERROR", "Couldn't send: {}, said: \n {} \n".format(text, message))


    #Send it over
    add_chat("YOU", text)

    #Clear text
    core.set_value("input_text_value", "")

def create_server_input(dimensions):
    with simple.window(
        "server_input",
        width  = dimensions.width,
        height = dimensions.height,

        x_pos= dimensions.x, 
        y_pos= dimensions.y,

        no_resize= True,
        no_move = True,
        no_title_bar = True,

    ):
        #DEBUG TEXT
        core.add_text("Server Input")

        #Add input text
        core.add_value("input_text_value", "")

        core.add_input_text("input_text", label="", on_enter=True, callback=enter_button, source="input_text_value")
        core.add_button("input_button", label="Send to Server", callback=enter_button)
