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

        # self.image.show()
        


        
        self.image_import.grid_forget() #! hides the open image button
        
        self.image_output = ImageOutput(self, self.resize_image)
        

    def resize_image(self, event):

        #* RESIZE


        #* PLACE IMAGE
        self.image_output.delete('all')
        self.image_output.create_image(event.width / 2, event.height / 2, image = self.image_tk )
        



App()