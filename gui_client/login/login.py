#Import the client for access
import console_client

#Import this app
from gui_client import main_app

#Use GUI
from dearpygui import core, simple

#Setup login call back
def request_login():
    #Get info from login input
    login_key = core.get_value("login_input")

    #Check login key
    login_attempt = console_client.client.save_auth_token(login_key)

    #If the login succeeded
    if login_attempt.success:
        login_succeeded()

    #If login key failed, say something
    else:
        #Delete the current error text if it exists
        if core.does_item_exist("login_error_text"):
            core.delete_item("login_error_text")

        #Setup error text
        error_text = "There was an error checking your key!"

        if login_attempt.message == "file_editing":
            error_text = "There was an error editing the key file on disk"

        if login_attempt.message == "non_key":
            error_text = "The key you entered wasn't a key..."

        #Finally, add error
        core.add_text(
            "login_error_text", 
            default_value=error_text, 
            before="login_button",
            wrap=0
        )

        




def login_succeeded():
    #Remove login, and add main window
    core.delete_item("login_window")

    #Create the app
    main_app.create_app()


#Setup the login page
def create_login():
    #get main window size
    window_size = core.get_main_window_size()

    #Setup login window size
    login_width  = 300
    login_height = 100

    login_x = int((window_size[0] / 2) - (login_width  / 2))
    login_y = int((window_size[1] / 2) - (login_height / 2))

    #Build window size
    with simple.window(
        "login_window", 
        no_title_bar = True,
        no_close = True,
        no_resize=True,
        autosize=True,
        x_pos = login_x,
        y_pos = login_y
    ):
        core.add_text("LOGIN")

        core.add_input_text("login_input", hint="auth key", password=True, label="")
        core.add_text("login_error_text", default_value=" ", before="login_button")



        core.add_button("login_button", label="Login Button", callback=request_login)

