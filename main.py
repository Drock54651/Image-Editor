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


    def init_parameters(self):
        self.rotate_float = ctk.DoubleVar(value = ROTATE_DEFAULT)
        self.rotate_float.trace('w', self.manipulate_image)

        self.zoom_float = ctk.DoubleVar(value = ZOOM_DEFAULT)
        self.zoom_float.trace('w', self.manipulate_image)

    def manipulate_image(self, *args):
        self.image = self.original

        #* ROTATE
        self.image = self.image.rotate(self.rotate_float.get())

        #* ZOOM
        self.image = ImageOps.crop(image = self.image, border = self.zoom_float.get())

        self.place_image()

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original #! this is the image that will be manipulated, original will be used to revert
        self.image_tk = ImageTk.PhotoImage(self.image) #! image must be converted to tk for use on tk widgets
        self.image_ratio = self.image.size[0] / self.image.size[1] #! w / h
        
    
        self.image_import.grid_forget() #! hides the open image button
        
        self.image_output = ImageOutput(self, self.resize_image) #! actually shows the image on canvas
        self.close_button = CloseOutput(self, self.close_edit)

        self.menu = Menu(self, self.rotate_float, self.zoom_float) #! left side menu
    
    def close_edit(self):
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

    def place_image(self):

        #* PLACE IMAGE
        self.image_output.delete('all')
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.canvas_width / 2, self.canvas_height / 2, image = self.image_tk ) #! centers image
        



App()