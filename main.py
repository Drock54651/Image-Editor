import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')

        #* RUN
        self.mainloop()




App()