import customtkinter as ctk

class Menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row = 0 , column = 0, sticky = 'news')

        #* TABS
        self.add('Position')
        self.add('Color')
        self.add('Effect')
        self.add('Export')