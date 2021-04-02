#Import the client for access
import console_client

from datetime import datetime

#Use GUI
from dearpygui  import core, simple

last_chat_id = 0

def add_chat(user, text):
    #Global
    global last_chat_id

    #append new text
    current_text = "[{}][{}]: {}".format(datetime.now(), user, text)

    #Save
    text_id = "server_output_entries_text{}".format(last_chat_id)
    core.add_text(text_id, default_value=current_text, parent="server_output", wrap=0)

    #Give it colour
    if(user == "SERVER"):
        core.set_item_color("server_output_entries_text{}".format(last_chat_id), 0, [255, 0, 0])
    
    #Update ID
    last_chat_id += 1


    
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
        #core.add_text("server_output_entries", default_value=" ")

        #Table | We really should make a custom widget so we can handle LONG entries
        add_chat("SERVER", "Client init...")