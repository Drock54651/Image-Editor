import customtkinter as ctk
from settings import *
from tkinter import filedialog
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
        self.data_var = data_var
        self.data_var.trace('w', self.update_text)

        #* WIDGETS
        ctk.CTkLabel(self, text = text).grid( row  = 0, column = 0, sticky = 'w', padx = 5)

        ctk.CTkSlider(self,
                      fg_color = SLIDER_BG, 
                      from_ = min_value, 
                      to = max_value, 
                      variable = self.data_var).grid( row = 1, column = 0, columnspan = 2, sticky = 'we', padx = 5, pady = 5)
        
        self.num_label = ctk.CTkLabel(self, text = data_var.get())
        self.num_label.grid(row = 0, column = 1, sticky = 'e', padx = 5 )

    def update_text(self, *args): #! updates values from the slider
        self.num_label.configure(text = f'{round(self.data_var.get(),2):.2f}')

class SegmentedPanel(Panel):
    def __init__(self, parent, text, data_var, options):
        super().__init__(parent)

        ctk.CTkLabel(self, text = text).pack()
        ctk.CTkSegmentedButton(self, variable = data_var, values = options).pack(expand = True, fill = 'both', padx = 4, pady = 4)

class SwitchPanel(Panel):
    def __init__(self, parent, *args): #! args is a tuple containing tuples: ((var, text), (var, text), (var, text))
        super().__init__(parent)

        for var, text in args:
            switch = ctk.CTkSwitch(self, text = text, variable = var, button_color = BLUE, fg_color = SLIDER_BG)
            switch.pack(side = 'left', expand = True, fill = 'both', padx = 5, pady = 5)

class DropDownPanel(ctk.CTkOptionMenu):    
    def __init__(self, parent, data_vars, options):
        super().__init__(parent, 
                         variable = data_vars, 
                         values = options, 
                         fg_color = DARK_GREY, 
                         button_color = DROPDOWN_MAIN_COLOR, 
                         button_hover_color = DROPDOWN_HOVER_COLOR, 
                         dropdown_fg_color = DROPDOWN_MENU_COLOR)
        
        self.pack(fill = 'both', pady = 4)

class FileNamePanel(Panel):
    def __init__(self, parent, name_string, file_string):
        super().__init__(parent)

        #* DATA
        self.name_string = name_string
        self.name_string.trace('w', self.update_text)
        self.file_string = file_string

        #* CHECK BOXES FOR FILE FORMAT
        ctk.CTkEntry(self, textvariable = self.name_string).pack(fill = 'x', padx = 20, pady = 5)
        frame = ctk.CTkFrame(self, fg_color = 'transparent')
        frame.pack(expand = True, fill = 'both', padx = 20)
        jpg_check = ctk.CTkCheckBox(frame, text = 'jpg', variable = self.file_string, command = lambda: self.click('jpg') , onvalue = 'jpg', offvalue = 'png' ) #! file_string value determines onvalue or offvalue
        png_check = ctk.CTkCheckBox(frame, text = 'png', variable = self.file_string, command = lambda: self.click('png') , onvalue = 'png', offvalue = 'jpg' )
        jpg_check.pack(side = 'left', fill = 'x', expand = True)
        png_check.pack(side = 'left', fill = 'x', expand = True)

        #* PREVIEW TEXT
        self.output = ctk.CTkLabel(self, text = '')
        self.output.pack()

    def click(self, value):
        self.file_string.set(value)
        self.update_text()

    def update_text(self, *args):
        if self.name_string.get():
            text = self.name_string.get().replace(' ', '_') + '.' + self.file_string.get() #! replaces the white space with _ so if file name is "pic 1" -> "pic_1"
            self.output.configure(text = text)

class FilePathPanel(Panel):
    def __init__(self, parent, path_string):
        super().__init__(parent)
        self.path_string = path_string
        ctk.CTkButton(self, text = 'Export Image To...', command = self.open_file).pack(pady = 10)
        ctk.CTkEntry(self, textvariable = path_string).pack( fill = 'x', pady = 10)

    def open_file(self):
        path = filedialog.askdirectory()
        self.path_string.set(path)

class RevertButton(ctk.CTkButton): #! reverts values to 0
    def __init__(self, parent, *args):
        super().__init__(parent, text = 'Revert', command = self.reset)
        self.pack(side = 'bottom', pady = 10)
        self.args = args

    def reset(self):
        for vars, value in self.args:
            vars.set(value)