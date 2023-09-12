import customtkinter as ctk
from settings import *
from image_widgets import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
from menu import Menu


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800,500)
        self.init_parameters()

        #* LAYOUT
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 6, uniform = 'a')

        #* CANVAS DATA
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        #* WIDGETS
        self.image_import = ImageImport(self, self.import_image)


        #* RUN
        self.mainloop()


    def init_parameters(self): #! the variables / datatypes for rotate, zoom, and other effects
        self.pos_vars = {
            'rotate': ctk.DoubleVar(value = ROTATE_DEFAULT),
            'zoom': ctk.DoubleVar(value = ZOOM_DEFAULT),
            'flip': ctk.StringVar(value = FLIP_OPTIONS[0] )
        }

        self.color_vars = {
            'brightness': ctk.DoubleVar(value = BRIGHTNESS_DEFAULT),
            'grayscale': ctk.BooleanVar(value = GRAYSCALE_DEFAULT),
            'invert': ctk.BooleanVar(value = INVERT_DEFAULT),
            'vibrance': ctk.DoubleVar(value = VIBRANCE_DEFAULT)

        }

        self.effect_vars = {
            'blur': ctk.DoubleVar(value = BLUR_DEFAULT),
            'contrast': ctk.IntVar(value = CONTRAST_DEFAULT),
            'effect': ctk.StringVar(value = 'Effects')
        }

        #* TRACING
        
        #TODO: apply trace to all variables using a single for loop
        combined_vars = list(self.pos_vars.values()) + list(self.color_vars.values()) + list(self.effect_vars.values()) #! converting dictionaries into lists and concating the lists into 1
        for var in combined_vars:
            var.trace('w', self.manipulate_image)        

    def manipulate_image(self, *args): #! manipulation changes for the menu panel
        self.image = self.original

        #* ROTATE
        self.image = self.image.rotate(self.pos_vars['rotate'].get())

        #* ZOOM
        self.image = ImageOps.crop(image = self.image, border = self.pos_vars['zoom'].get())

        #* FLIP
        if self.pos_vars['flip'].get() == 'X':
            self.image = ImageOps.mirror(self.image)

        if self.pos_vars['flip'].get() == 'Y':
            pass
        
        if self.pos_vars['flip'].get() == 'Both':
            pass
        

        self.place_image()

    def import_image(self, path): #! imports image, get ratios, and calls the Menu class
        self.original = Image.open(path)
        self.image = self.original #! this is the image that will be manipulated, original will be used to revert
        self.image_tk = ImageTk.PhotoImage(self.image) #! image must be converted to tk for use on tk widgets
        self.image_ratio = self.image.size[0] / self.image.size[1] #! w / h
        
    
        self.image_import.grid_forget() #! hides the open image button
        
        self.image_output = ImageOutput(self, self.resize_image) #! actually shows the image on canvas
        self.close_button = CloseOutput(self, self.close_edit)

        self.menu = Menu(self, self.pos_vars, self.color_vars, self.effect_vars) #! left side menu
    
    def close_edit(self): #! closes everything and adds option to import image again
        #TODO: hide image and close the button
        #TODO: recreate the import button
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.image_import = ImageImport(self, self.import_image)
        self.menu.grid_forget()

    def resize_image(self, event): #! called in image_widgets.py -> ImageOutput

        #* CURRENT CANVAS RATIO
        canvas_ratio = event.width / event.height

        #* CANVAS ATTRIBUTES
        self.canvas_width = event.width
        self.canvas_height = event.height

        #* RESIZE
        if canvas_ratio > self.image_ratio: #! canvas is wider than image
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)

        else: #! canvas is taller than the image
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)

        self.place_image()

    def place_image(self): #! places newly manipulated or resized image

        #* PLACE IMAGE
        self.image_output.delete('all')
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.canvas_width / 2, self.canvas_height / 2, image = self.image_tk ) #! centers image
        



App()