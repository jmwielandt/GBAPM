from PyQt5.QtCore import pyqtSignal


class CommonBackend:

    trigger_add_pal = pyqtSignal(int)
    trigger_rem_pal = pyqtSignal(int)

    def __init__(self, parent):
        self.pal = [[0, 0, 0]]
        self.pal_index = [0]
        self.pal_index_counter = 0
        #print(parent)
    
    def connect_triggers(self, parent):
        self.trigger_add_pal.connect(parent.add_pal_list)
        self.trigger_rem_pal.connect(parent.rem_pal_list)
    
    def pal_index_change(self, i):
        self.pal_index[0] = i
    
    def add_pal_index(self):
        self.pal_index_counter += 1
        self.trigger_add_pal.emit(self.pal_index_counter)
        self.pal.append([0, 0, 0])
    
    def rem_pal_index(self):
        self.trigger_rem_pal.emit(self.pal_index_counter)
        self.pal_index_counter -= 1
        self.pal.pop()
    
    def edit_pal_index(self):
        pass
    
    def show_pal_index(self):
        pass
    
    def rgb5_to_rgb8(self, r, g, b):
        mul = 8.22580645161
        R = round(int(r) * mul) if r != '' else 0
        G = round(int(g) * mul) if g != '' else 0
        B = round(int(b) * mul) if b != '' else 0
        RGB = [R, G, B]
        return RGB
    
    def rgb5_to_u16(self, r, g, b):
        R = r & 0b11111
        G = g & 0b11111
        B = b & 0b11111
        RGB_ = R | (G << 5) | (B << 10)
        RGB = hex(RGB_)[2:]
        if len(RGB) < 4:
            RGB = ("0" * (4 - len(RGB))) + RGB
        RGB = "0x" + RGB
        return RGB
    
    def rgb5_to_u32(self, r1, g1, b1, r2, g2, b2):
        RGB1 = self.rgb5_to_u16(r1, g1, b1)[2:]
        RGB2 = self.rgb5_to_u16(r2, g2, b2)[2:]
        RGB = RGB2 + RGB1
        return RGB



