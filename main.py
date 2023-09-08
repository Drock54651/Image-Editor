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
        self.image_tk = ImageTk.PhotoImage(self.image)
        # self.image.show()


        
        self.image_import.grid_forget() #! hides the open image button
        
        self.image_output = ImageOutput(self)
        self.resize_image()

    def resize_image(self):
        self.image_output.create_image(0, 0, image = self.image_tk )
        



App()