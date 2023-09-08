import customtkinter as ctk


#TODO cover entire window, contain button in middle, button says open image
class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_image_func):
        super().__init__(parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'news')
        self.import_image_func = import_image_func
        ctk.CTkButton(self, text = 'Open Image', command = self.open_dialog).place(relx  = .5, rely = .5, anchor = 'center')


    def open_dialog(self):
        path = 'test'
        self.import_image_func(path)