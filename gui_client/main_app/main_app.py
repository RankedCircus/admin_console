#Import the client for access
import console_client

from .widgets import menu, server_input, server_output

#Use GUI
from dearpygui import core, simple


#TODO: Put this somewhere else
class Dimensions:
    def __init__(self, x, y, width, height):
        self.x = int(x)
        self.y = int(y)
        self.width  = int(width)
        self.height = int(height)


def create_app():
    #Add window
    with simple.window("main_window"):
        #Create Menu
        menu.create_menu()

    #Generalized styling 
    core.set_style_window_rounding(0.0)

    #Setup Styling by finding main_window dimensions
    raw_app_dimensions = core.get_main_window_size("main_window")
    app_dimensions     = Dimensions(0, 20, raw_app_dimensions[0], raw_app_dimensions[1] - 60)

    #Look for a cleaner way to set this up?
    output_dimensions = Dimensions(
        x      = 0, 
        y      = 20, 
        width  = 0.8 * app_dimensions.width, 
        height = 0.8 * app_dimensions.height
    )

    input_dimensions = Dimensions(
        x      = 0, 
        y      = output_dimensions.y + output_dimensions.height, 
        width  = output_dimensions.width, 
        height = app_dimensions.height - output_dimensions.height
    )

    #Add server input
    server_input.create_server_input(input_dimensions)

    #Add server output
    server_output.create_server_output(output_dimensions)

    #Set the main_window to be primary
    core.set_primary_window("main_window", True)
    