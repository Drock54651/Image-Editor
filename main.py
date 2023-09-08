import customtkinter as ctk
from settings import *
from image_widgets import *
from tkinter import filedialog
from PIL import Image

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
        self.image.show()


        #TODO hide the image import widget
        self.image_import.grid_forget()
        



App()