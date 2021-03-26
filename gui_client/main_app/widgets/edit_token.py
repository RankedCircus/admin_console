#Import the client for access
import console_client

#Use GUI
from dearpygui import core, simple



def edit_request():
    #Get info from login input
    login_key = core.get_value("key_input")

    #Check login key
    login_attempt = console_client.client.save_auth_token(login_key)

    #Delete the current error text if it exists
    if core.does_item_exist("key_error_text"):
        core.delete_item("key_error_text")

    #If the login succeeded
    if login_attempt.success:
        #Add success text
        core.add_text(
            "key_error_text", 
            default_value="Key successfully changed :)", 
            before="edit_button",
            wrap=0
        )

        #Change token display
        core.delete_item("token_display")
        core.add_text(
            "token_display",
            default_value="Current token: {}...".format(console_client.client.auth_token[:10]), 
            before="key_input"
        )

        

    #If login key failed, say something
    else:
        #Setup error text
        error_text = "There was an error checking your key!"

        if login_attempt.message == "file_editing":
            error_text = "There was an error editing the key file on disk"

        if login_attempt.message == "non_key":
            error_text = "The key you entered wasn't a key..."

        #Finally, add error
        core.add_text(
            "key_error_text", 
            default_value=error_text, 
            before="edit_button",
            wrap=0
        )


def create_widget():
    #If this widget exists, kill it
    if core.does_item_exist("edit_token"):
        core.delete_item("edit_token")


    #Create widget
    with simple.window("edit_token"):
        core.add_text("Use dis to edit token")
        core.add_text("token_display", default_value="Current token: {}...".format(console_client.client.auth_token[:10]))

        core.add_input_text("key_input", hint="auth key", password=True, label="")
        core.add_text("key_error_text", default_value=" ", before="edit_button")

        core.add_button("edit_button", label="Edit", callback=edit_request)
