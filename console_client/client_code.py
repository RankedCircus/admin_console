import os
import socket

import traceback
from collections import namedtuple


class Client:
    def __init__(self, host, port):
        #Save port info
        self.host = host
        self.port = port

        #Setup client
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Setup auth token
        self.token_path = "./CircusAdmin" #Eventually lets pass this to an env? I know he wants to do %local%/path eventually
        self.auth_token = self.fetch_token()
    
    #---------------- Socket Client Commands ----------------------
    def connect(self):
        #Bind
        self.socket_client.connect((self.host, self.port))
        
        #TODO: Shit here? yeah idk until I get the server code



    #---------------- Misc Shit ----------------------
    def test(self):
        print("test")


    #-------------- Auth File ------------------
    def fetch_token(self):
        #Check to see if the folder exists
        if os.path.exists(self.token_path) == False:
            return None

        #Check to see if the auth file exist
        token_file_path = "{}/.token_file".format(self.token_path)

        if os.path.exists(token_file_path) == False:
            return None

        #Assuming the token file exists, open it and pull token
        token_file = open(token_file_path, "r")

        encoded_token = str(token_file.read())

        #Decode token? idk what exactly his plan is, so for now if there's content in this file
        #Return it
        return encoded_token


    def save_auth_token(self, token):
        #Before we do anything, we should probably validate the token lmao
        try:
            #Check to see if the folder exists
            if os.path.exists(self.token_path) == False:
                #Make it 
                os.mkdir(self.token_path)

            #Check to see if the auth file exist
            token_file_path = "{}/.token_file".format(self.token_path)

            #Create the file, and save it
            token_file = open(token_file_path, "w+")
            token_file.write(token)
            token_file.close()

            #Finally save the new token to our system
            self.auth_token = token

        except: 
            print("Error in saving auth token")
            print(traceback.format_exc())
            return return_failure("file_editing")


        return return_success()





#-------------- Return Values ------------------
result = namedtuple("result", "success data message")

def return_success(data=None):
    return result(True, data, None)

def return_failure(message):
    return result(False, None, message)

