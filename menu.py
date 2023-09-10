import customtkinter as ctk
from panel import *


class Menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row = 0 , column = 0, sticky = 'news', pady = 10, padx = 10)

        #* TABS
        self.add('Position')
        self.add('Color')
        self.add('Effect')
        self.add('Export')

        #* WIDGETS
        PositionFrame(self.tab('Position')) #! attaches the frame to the position tab when clicked on
        ColorFrame(self.tab('Color')) #! attaches the frame to the position tab when clicked on


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')

        SliderPanel(self, text = 'Rotation')
        SliderPanel(self, text = 'Zoom')

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')
