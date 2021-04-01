#Import the client for access
import console_client

from datetime import datetime

#Use GUI
from dearpygui  import core, simple



def add_chat(text):
    #Split the text into multiple entries if it's over X length
    TEXT_LENGTH = 30

    text_arr = []
    if len(text) > TEXT_LENGTH:
        current_added = 0
        current_text  = ""


        while len(text) > TEXT_LENGTH:
            #Get the first 40 chars
            text_to_remove = text[:TEXT_LENGTH]

            #Pop out those chars
            for char_indx in range(0, TEXT_LENGTH):
                text.pop(0)


            #Add the text to the list
            text_arr.append("...{}...".format(text_to_remove))


        #Add the final text
        text_arr.append("...{}".format(text))
    
    else:
        text_arr = [text]



    #Remove the last text block's elipse
    if len(text_arr) > 1:
        last_item = text_arr[len(text_arr) - 1]
        text_arr[len(text_arr) - 1] = last_item[0: len(last_item) - 3]

    #Add item
    for items in text_arr:
        core.add_row("server_output_entries", [datetime.now(), "SERVER", items])



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
        core.add_text("Server Output")

        #Table | We really should make a custom widget so we can handle LONG entries
        core.add_table(
            "server_output_entries",
            headers = ["time", "user", "text"],

            width =  dimensions.width,
            height = dimensions.height - 20

        )

        #Add a small row
        core.add_row("server_output_entries", [datetime.now(), "SERVER", "Client init..."])