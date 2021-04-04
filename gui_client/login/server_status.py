#Import the client for access
import console_client
import threading

#Use GUI
from dearpygui import core, simple

# ------------------ Call Backs ------------------ 
def connect_to_server():
    #Get port 
    port = console_client.client.port

    #Set the port to whatever input we have
    try:
        port = int(core.get_value("port_input"))

    #Fails when port isn't an int
    except:
        pass

    
    #Get server
    server = core.get_value("server_selection")

    if server == "server_selection":
        server = "0"

    #Reset host and port 
    console_client.client.host = console_client.client.host_list[int(server)]
    console_client.client.port = port

    #Change pages
    hide_server_selection()
    show_server_status()

    #Connect
    network_thread = threading.Thread(target = console_client.client.connect)
    network_thread.start()

def disconnect_from_server():
    #If connected, disconnect
    console_client.client.disconnect()

    #Remove server info, and buttons
    hide_server_status()

    #Now add the server selection info
    show_server_selection()



# ------------------ items Hider ------------------ 
def items_remover(items):
    for item in items:
        if(core.does_item_exist(item) == True):
            core.delete_item(item)

# ------------------ Server Selection ------------------ 
def show_server_selection():
    #Server Selection
    core.add_text("server_selection_title", default_value="Select server", parent="status_window")
    core.add_listbox(
        "server_selection", 
        
        items         = console_client.client.host_list,
        default_value = 0,

        label  = "",
        parent = "status_window",

        width  = 230
    )


    core.add_text("server_selection_padding1", default_value="\n", parent="status_window")
    core.add_text("port_input_title", default_value="Change Port", parent="status_window")


    #Port Selection
    core.add_input_text(
        "port_input",

        parent        = "status_window",
        scientific    = True,
        default_value = str(console_client.client.port),
        label         = ""
    )

    #Padding
    core.add_text("server_selection_padding2", default_value="\n", parent="status_window")

    #Connect button
    core.add_button(
        "server_connect_button", 

        label    = "Connect",
        callback = connect_to_server,
        parent   = "status_window"
    )

def hide_server_selection():
    elems =  [
        "server_selection_title",
        "server_selection",
        "server_connect_button",
        "port_input",
        "port_input_title",

        "server_selection_padding1",
        "server_selection_padding2",
    ]

    #Delete
    items_remover(elems)


# ------------------ Status Creation ------------------ 
def show_server_status():
    #Server information
    core.add_text("server_info", 
        default_value = "\nCurrent Server: {}:{}".format(
            console_client.client.host,
            console_client.client.port,
        ),

        parent = "status_window",
        wrap   = 0
    )

    #Some padding
    core.add_text("server_status_padding1", default_value="\n", parent="status_window")

    #Login Status
    core.set_value("server_status_value", "Not connected")
    core.add_text(
        "server_status", 
        
        source = "server_status_value", 
        default_value = console_client.client.connection_status, 
        
        wrap   = 0, 
        parent = "status_window"
    )

    #More padding
    core.add_text("server_status_padding2", default_value="\n", parent="status_window")

    #Disconnect button
    core.add_button(
        "server_disconnect", 

        label    = "Disconnect",
        parent   = "status_window",
        callback = disconnect_from_server
    )


def hide_server_status():
    #List Items
    elems = [
        "server_info",
        "server_status_padding1",
        "server_status_padding2",
        "server_status",
        "server_disconnect",
    ]

    #Delete
    items_remover(elems)

# ------------------ Window Creation ------------------ 

def create_status(x, y):
    #Setup login window size
    width  = 245
    height = 220


    #Build window size
    with simple.window(
        "status_window",

        no_title_bar = True,
        no_close     = True,
        no_resize    = True,
        no_move      = True,
        autosize     = False,
        
        width  = width,
        height = height,

        x_pos = x,
        y_pos = y,
    ):
        #Title
        core.add_text("== SERVER STATUS ==")

        show_server_status()


