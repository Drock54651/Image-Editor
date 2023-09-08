import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *
#TODO cover entire window, contain button in middle, button says open image
class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_image_func):
        super().__init__(parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'news')
        self.import_image_func = import_image_func
        ctk.CTkButton(self, text = 'Open Image', command = self.open_dialog).place(relx  = .5, rely = .5, anchor = 'center')


    def open_dialog(self):
        path = filedialog.askopenfile().name
        
        self.import_image_func(path)

        # path = filedialog.askopenfile().name
        # print(path)


class ImageOutput(Canvas):
    def __init__(self, parent):
        super().__init__(parent, background = BACKGROUND_COLOR , bd = 0, highlightthickness = 0, relief = 'ridge')
        self.grid(row = 0, column = 1, sticky = 'news')