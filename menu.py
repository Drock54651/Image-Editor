import customtkinter as ctk
from panel import *


class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars):
        super().__init__(parent)

        self.grid(row = 0 , column = 0, sticky = 'news', pady = 10, padx = 10)

        #* TABS
        self.add('Position')
        self.add('Color')
        self.add('Effect')
        self.add('Export')

        #* WIDGETS
        PositionFrame(self.tab('Position'), pos_vars,) #! attaches the frame to the position tab when clicked on
        ColorFrame(self.tab('Color'), color_vars) #! attaches the frame to the position tab when clicked 
        EffectFrame(self.tab('Effect'), effect_vars)
        ExportFrame(self.tab('Export'))
        

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')

        SliderPanel(self, text = 'Rotation', data_var = pos_vars['rotate'], min_value = 0, max_value = 360)
        SliderPanel(self, text = 'Zoom', data_var = pos_vars['zoom'], min_value = 0, max_value = 200 )
        SegmentedPanel(self, 'Invert', pos_vars['flip'], FLIP_OPTIONS)
        RevertButton(self, 
                     (pos_vars['rotate'], ROTATE_DEFAULT),
                     (pos_vars['flip'], FLIP_OPTIONS[0]),
                     (pos_vars['zoom'], ZOOM_DEFAULT))

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')
        SwitchPanel(self, (color_vars['grayscale'], 'B/W'), (color_vars['invert'], 'Invert'))
        SliderPanel(self, text = 'Brightness', data_var = color_vars['brightness'], min_value = 0, max_value = 5)
        SliderPanel(self, text = 'Vibrance', data_var = color_vars['vibrance'], min_value = 0, max_value = 5 )

        RevertButton(self, 
                     (color_vars['brightness'], VIBRANCE_DEFAULT),
                     (color_vars['grayscale'], GRAYSCALE_DEFAULT),
                     (color_vars['invert'], INVERT_DEFAULT),
                     (color_vars['vibrance'], VIBRANCE_DEFAULT))

class EffectFrame(ctk.CTkFrame):
        def __init__(self, parent, effect_vars):
            super().__init__(parent, fg_color = 'transparent')
            self.pack(expand = True, fill = 'both')

            DropDownPanel(self, effect_vars['effect'], EFFECT_OPTIONS)
            SliderPanel(self, text = 'Blur', data_var = effect_vars['blur'], min_value = 0, max_value = 30 )
            SliderPanel(self, text = 'Contrast', data_var = effect_vars['contrast'], min_value = 0, max_value = 10 )

            RevertButton(self, 
                     (effect_vars['blur'], BLUR_DEFAULT),
                     (effect_vars['contrast'], CONTRAST_DEFAULT),
                     (effect_vars['effect'], EFFECT_OPTIONS[0]))

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
            super().__init__(parent, fg_color = 'transparent')
            self.pack(expand = True, fill = 'both')

            #* DATA
            self.name_string = ctk.StringVar()
            self.file_string = ctk.StringVar(value = 'jpg')
            self.path_string = ctk.StringVar()
            #* WIDGETS 
            FileNamePanel(self, self.name_string, self.file_string)
            FilePathPanel(self, self.path_string)
