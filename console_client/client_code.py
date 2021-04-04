import os
import socket
import time
import dearpygui.core
import threading
import traceback

from datetime            import datetime
from collections         import namedtuple
from gui_client.main_app import add_chat


class Client:
    def __init__(self, host, port):
        #Setup host info 
        self.host_list = [
            "johnbender.rankedcircus.com",
            "andrewclark.rankedcircus.com",
            "allisonreynolds.rankedcircus.com",
            "brianjohnson.rankedcircus.com",
            "127.0.0.1"
        ]

        #Save port info
        self.host = host
        self.port = port

        #If host is none, set it to self.host[0]
        if self.host == None:
            self.host = self.host_list[0]

        #Setup client
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Setup Connection info
        self.disconnect_request = False
        self.connected          = False
        self.connection_error   = False
        self.connection_status  = ""
        
        #Token Info
        self.token_path = "./CircusAdmin" #Eventually lets pass this to an env? I know he wants to do %local%/path eventually
        self.auth_token = self.fetch_token()
    
    #---------------- Socket Client Commands ----------------------
    def connect(self):
        #Setup attempt counter
        connection_attempts = 0
 
        #Reset disconnect request 
        self.disconnect_request = False

        #Try and connect while we aren't connected
        while self.connected == False:
            #If there's a disconnect request, exit
            if(self.disconnect_request == True):
                #Leave
                return  

            #Attempt connection
            try:
                self.socket_client.connect((self.host, self.port))
                self.connected = True
                break

            #Connection Failure handler
            except:
                connection_attempts += 1

                self.connection_error  = True
                self.connection_status = "No Server Found | {}:{}".format(self.host, self.port)


                #Update what's the status of the server
                dearpygui.core.set_value("server_status_value", "Not Connected\n(FAILED TO MAKE CONNECTION)")


                #If the client is opened, then just say that we're still waiting for a connection
                if dearpygui.core.does_item_exist("server_output_entries_text0"):
                    add_chat("SERVER", "Still not connected... Try {}, last check said: {}".format(connection_attempts, self.connection_status))


                #Sleep assuming we didn't do anything
                time.sleep(5)

        
        #Say we connected
        dearpygui.core.set_value("server_status_value", "Connected")
        add_chat("SERVER", "Connected to {}:{}".format(self.host, self.port))

        #Assuming we here, start a thread for getting data
        message_thread = threading.Thread(target = self.read_message)
        message_thread.start()

        #TODO: Shit here? yeah idk until I get the server code

    def disconnect(self):
        #If connected, don't be
        if self.connected:
            self.socket_client.close() #Close socket or we can't reconnect
        
        #Reset the sock
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Reset the socket

        #Reset internal values
        self.connected          = False
        self.disconnect_request = True


    #Just send data to the socket
    def send_command(self, string):
        try:
            self.socket_client.send((string + "\r\n").encode())
            return (True, None)


        #Error handling | This should really be in more depth to handle disconnects, etc
        except Exception as Error: 
            #If we were never connected
            if self.connected == True:
                return (False, "Not connected to any server D:, log out and back in")

            #If we are connected
            else:
                self.connection_error = True
                return (False, Error)


    def read_message(self):
        #While true take any incoming data, and pass it off to add chat
        try:
            while(self.disconnect_request != True):
                Data = self.socket_client.recv(1024).decode()

                #if data send
                add_chat("SERVER", Data)
                
        except ConnectionResetError:
            #Reset connection handler
            self.connected = False
            self.socket_client.close() #Close socket or we can't reconnect
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Reset the socket

            #Say we disconnected
            add_chat("SERVER", "Got disconnected, retrying connection now")

            #Restart 
            network_thread = threading.Thread(target = self.connect)
            network_thread.start()

        except ConnectionAbortedError:
            #Reset connection handler
            self.connected = False
            self.socket_client.close() #Close socket or we can't reconnect
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Reset the socket

            #Say we disconnected
            add_chat("SERVER", "User disconnected")


        #TODO: Handle other errors tat show up



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
        #Before we do anything, and anything else, check if it's a string lmao
        if len(token) == 0:
            return return_failure("non_key")

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

    def signout(self):
        #Setup token path
        token_file_path = "{}/.token_file".format(self.token_path)

        #Remove file
        os.remove(token_file_path)

        self.auth_token = None



#-------------- Return Values ------------------
result = namedtuple("result", "success data message")

def return_success(data=None):
    return result(True, data, None)

def return_failure(message):
    return result(False, None, message)

