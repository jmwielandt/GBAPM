#The main window.
import sys
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from common_backend import CommonBackend
#import params as p

"""
from ColorMixer import *
from Rgb5toU16 import *
from Rgb5toU32 import *

from Export import *
from JPAL import *
"""


class MainRoot(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("GBA Palette Manager")
        self.initGUI()
        self.show()
    
    def initGUI(self):
        self.layout0 = QHBoxLayout()
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.open_file_button = QPushButton("Open")
        self.add_pal_index_button = QPushButton("Add palette index")
        self.rem_pal_index_button = QPushButton("Remove palette index")
        self.edit_pal_index_button = QPushButton("Edit color at current index")
        self.show_pal_index_button = QPushButton("Show the current palette index color")
        self.save_file_button = QPushButton("Save as json")
        self.pal_save_button = QPushButton("Export to pal")
        self.export_button = QPushButton("Export to C")

        self.pal_list = QComboBox()

        self.layout0.addWidget(self.open_file_button)
        self.layout1.addWidget(self.pal_list)
        self.layout1.addWidget(self.add_pal_index_button)
        self.layout1.addWidget(self.rem_pal_index_button)
        self.layout2.addWidget(self.edit_pal_index_button)
        self.layout2.addWidget(self.show_pal_index_button)
        self.layout3.addWidget(self.save_file_button)
        self.layout3.addWidget(self.pal_save_button)
        self.layout3.addWidget(self.export_button)
        
        self.layout.addLayout(self.layout0)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        self.setLayout(self.layout)
        pass
    
    def initBack(self):
        pass
    
    def open_file(self):
        pass
    
    def save_file(self):
        pass
    
    def save_pal_file(self):
        pass
    
    def export_file(self):
        pass
    
    def pal_index_change(self, i):
        pass
    
    def add_pal_index(self):
        pass
    
    def rem_pal_index(self):
        pass
    
    def edit_pal_index(self):
        pass
    
    def show_pal_index(self):
        pass


main_app = QApplication([])
main_root = QWidget()

pal_index_counter = 0

def main_window():
    main_app.setStyle('Fusion')
    open_file_button.clicked.connect(openfile)
    
    pal_list.addItem("0")
    pal_list.currentIndexChanged.connect(palindexchange)
    add_pal_index_button.clicked.connect(addpalindex)
    rem_pal_index_button.clicked.connect(rempalindex)
    edit_pal_index_button.clicked.connect(editpalindex)
    show_pal_index_button.clicked.connect(showpalindex)
    save_file_button.clicked.connect(savefile)
    pal_save_button.clicked.connect(savepalfile)
    export_button.clicked.connect(exportfile)
    main_root.show()
    main_app.exec_()

def openfile():
    global pal_index_counter
    
    filedialog = QFileDialog
    filepath = filedialog.getOpenFileName(main_root, 'Open file', 'c:\\', "Json files (*.json)")
    with open(filepath[0], 'r') as f:
        data = json.load(f)
        
        length = data["length"]
        pal_list.clear()
        pal_index_counter = length - 1
        for ii in range(0, length):
            pal_list.addItem(str(ii))
        pal_index[0] = 0
        
        pal_data = data["palette"]
        
        pal.clear()
        
        for ii in pal_data:
            pal.append(ii)
            print(ii)

def savefile():
    filedialog = QFileDialog
    filepath = filedialog.getSaveFileName(main_root, 'Save file', 'c:\\', "Json files (*.json)")
    with open(filepath[0], 'w') as f:
        data = {}
        data["length"] = pal_index_counter + 1
        data["palette"] = pal
        
        f.write(json.dumps(data, ensure_ascii = False))
        
        f.close()

def savepalfile():
    filedialog = QFileDialog
    filepath = filedialog.getSaveFileName(main_root, 'Save file', 'c:\\', "Palette files (*.pal)")
    
    ArraytoJascPal(pal, pal_index_counter + 1, filepath[0])

def exportfile():
    export_handler(pal_index_counter + 1)

def palindexchange(i):
    global pal_index
    
    pal_index[0] = i

def addpalindex():
    global pal_index_counter
    
    pal_index_counter += 1
    pal_list.addItem(str(pal_index_counter))
    pal.append([0, 0, 0])

def rempalindex():
    global pal_index_counter
    
    pal_list.removeItem(pal_index_counter)
    pal_index_counter -= 1
    pal.pop()

def editpalindex():
    color_mixer(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])

def showpalindex():
    global pal
    global pal_index
    
    alert = QMessageBox()
    alert.setAutoFillBackground(True)
    alert.setText('Current color: \nRed: ' + str(pal[pal_index[0]][0]) + '\nGreen: ' + str(pal[pal_index[0]][1]) + '\nBlue: ' + str(pal[pal_index[0]][2]) + '\nHex (16 bit): ' + str(RGB5tou16(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])))
    bgpal = alert.palette()
    clr_ = RGB5toRGB8(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])
    bgpal.setColor(alert.backgroundRole(), QColor(clr_[0], clr_[1], clr_[2]))
    alert.setPalette(bgpal)
    alert.exec_()



if __name__ == "__main__":
    app = QApplication([])
    wdw = MainRoot()
    sys.exit(app.exec_())

