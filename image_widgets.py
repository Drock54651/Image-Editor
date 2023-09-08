import customtkinter as ctk


    #TODO cover entire window, contain button in middle, button says open image
class ImageImport(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'news')

        ctk.CTkButton(self, text = 'Open Image').place(relx  = .5, rely = .5, anchor = 'center')