import customtkinter as ctk


    #TODO cover entire window, contain button in middle, button says open image
class ImageImport(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand = True, fill = 'both')