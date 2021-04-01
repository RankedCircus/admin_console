#Import the client for access
import console_client

from datetime import datetime

#Use GUI
from dearpygui  import core, simple


"""
def add_chat(text):
    #Split the text into multiple entries if it's over X length
    TEXT_LENGTH = 30

    text_arr = []
    if len(text) > TEXT_LENGTH:

        #While we're over the text length, add it
        while len(text) > TEXT_LENGTH:
            #Get the first 40 chars
            text_to_remove = text[:TEXT_LENGTH]
            text = text[TEXT_LENGTH:]

            #Add the text to the list
            text_arr.append("...{}...".format(text_to_remove))


        #Add the final text
        text_arr.append("...{}".format(text))
    
    else:
        text_arr = [text]


    #Add item
    for items in text_arr:
        core.add_row("server_output_entries", [datetime.now(), "SERVER", items])
"""

def add_chat(user, text):
    #get current text
    current_text = core.get_value("server_output_entries")
    core.delete_item("server_output_entries")

    #If none, add text
    if current_text == "server_output_entries":
        current_text = ""


    #append new text
    current_text += "\n[{}][{}]: {}".format(datetime.now(), user, text)

    #Save
    core.add_text("server_output_entries", default_value=current_text, parent="server_output")



    
def create_server_output(dimensions):
    with simple.window(
        "server_output",
        width  = dimensions.width,
        height = dimensions.height,

        x_pos = dimensions.x, 
        y_pos = dimensions.y,

        no_resize= True,
        no_move = True,
        menubar = False,
        no_title_bar = True,
        #no_background = True
    ):
        #Header
        core.add_text("server_output_entries", default_value="")

        #Table | We really should make a custom widget so we can handle LONG entries
        add_chat("SERVER", "Client init...")
        """
        core.add_table(
            "server_output_entries",
            headers = ["time", "user", "text"],

            width =  dimensions.width,
            height = dimensions.height - 20

        )


        #Add a small row
        core.add_row("server_output_entries", [datetime.now(), "SERVER", "Client init..."])
        """