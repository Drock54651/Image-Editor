import customtkinter as ctk
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = DARK_GREY)
        self.pack(fill = 'both', pady = 4, ipady = 8)


class SliderPanel(Panel):
    def __init__(self, parent, text, data_var, min_value, max_value):
        super().__init__(parent)

        

        #* LAYOUT
        self.rowconfigure((0,1 ), weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        #* WIDGETS
        ctk.CTkLabel(self, text = text).grid( row  = 0, column = 0, sticky = 'w', padx = 5)

        ctk.CTkSlider(self,
                      fg_color = SLIDER_BG, 
                      command = self.update_text,
                      from_ = min_value, 
                      to = max_value, 
                      variable = data_var).grid( row = 1, column = 0, columnspan = 2, sticky = 'we', padx = 5, pady = 5)
        
        self.num_label = ctk.CTkLabel(self, text = data_var.get())
        self.num_label.grid(row = 0, column = 1, sticky = 'e', padx = 5 )

    def update_text(self, value): #! updates values from the slider
        self.num_label.configure(text = f'{round(value,2)}')


