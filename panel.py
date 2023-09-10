import customtkinter as ctk
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = DARK_GREY)
        self.pack(fill = 'both', pady = 4, ipady = 8)


class SliderPanel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent)

        #* DATA
        self.value = ctk.IntVar(value = 0)

        #* LAYOUT
        self.rowconfigure((0,1 ), weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        #* WIDGETS
        ctk.CTkLabel(self, text = text).grid( row  = 0, column = 0, sticky = 'w', padx = 5)
        ctk.CTkSlider(self,fg_color = SLIDER_BG, from_ = 0, to = 100, variable = self.value).grid( row = 1, column = 0, columnspan = 2, sticky = 'we', padx = 5, pady = 5)
        ctk.CTkLabel(self, textvariable = self.value).grid(row = 0, column = 1, sticky = 'e', padx = 5 )


