import customtkinter as ctk
from settings import *
from image_widgets import *
from tkinter import filedialog
from PIL import Image, ImageTk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800,500)

        #* LAYOUT
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 6, uniform = 'a')

        #* DATA

        #* WIDGETS
        self.image_import = ImageImport(self, self.import_image)

        #* RUN
        self.mainloop()

    def import_image(self, path):
        self.image = Image.open(path)
        self.image_tk = ImageTk.PhotoImage(self.image) #! image must be converted to tk for use on tk widgets
        self.image_ratio = self.image.size[0] / self.image.size[1] #! w / h

    
        self.image_import.grid_forget() #! hides the open image button
        
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
    
    def close_edit(self):
        #TODO: hide image and close the button
        #TODO: recreate the import button
        self.image_output.grid_forget()
        self.close_button.place_forget()
        ImageImport(self, self.image_import)

    def resize_image(self, event): #! called in image_widgets -> ImageOutput

        #* CURRENT CANVAS RATIO
        canvas_ratio = event.width / event.height

        #* RESIZE
        if canvas_ratio > self.image_ratio: #! canvas is wider than image
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)

        else: #! canvas is taller than the image
            image_width = int(event.width)
            image_height = int(event.width / self.image_ratio)


        #* PLACE IMAGE
        self.image_output.delete('all')
        resized_image = self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width / 2, event.height / 2, image = self.image_tk )
        



App()