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


    def open_dialog(self): #! gets file path to image on user's PC
        path = filedialog.askopenfile().name
        
        self.import_image_func(path) #! calls import_image func in main 

        # path = filedialog.askopenfile().name
        # print(path)


class ImageOutput(Canvas): #! where the image will be on
    def __init__(self, parent, resize_image):
        super().__init__(parent, background = BACKGROUND_COLOR , bd = 0, highlightthickness = 0, relief = 'ridge')
        self.grid(row = 0, column = 1, sticky = 'news')
        self.bind('<Configure>', resize_image)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_edit_func):
        super().__init__(parent, 
                         text  = 'x', 
                         text_color = WHITE, 
                         fg_color = 'transparent', 
                         width = 40, 
                         height = 40,
                         corner_radius = 0,
                         hover_color = CLOSE_RED,
                         command = close_edit_func)
        
        self.place(relx = .99, rely = .01, anchor = 'ne')