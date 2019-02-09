#mix and return a color.

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit, QPushButton
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import QIntValidator, QColor


class ColorMixer(QWidget):
    def __init__(self, common_back, *args, **kwargs):
        self.crl = [0, 0, 0]
        super().__init__(*args, **kwargs)
        self.setWindowTitle("GBA Color Mixer")
        self.setAutoFillBackground(True)
        self.common_backend = common_back
        self.initGUI()
        self.show()
    
    def initGUI(self):
        self.red_value_line_edit = QLineEdit()
        self.green_value_line_edit = QLineEdit()
        self.blue_value_line_edit = QLineEdit()

        RGB5validator = QIntValidator(0, 31)
        
        self.red_value_line_edit.setValidator(RGB5validator)
        self.red_value_line_edit.setMaxLength(2)
        self.red_value_line_edit.setAlignment(Qt.AlignRight)
        self.red_value_line_edit.textChanged.connect(self.crl_changed)

        self.green_value_line_edit.setValidator(RGB5validator)
        self.green_value_line_edit.setMaxLength(2)
        self.green_value_line_edit.setAlignment(Qt.AlignRight)
        self.green_value_line_edit.textChanged.connect(self.crl_changed)

        self.blue_value_line_edit.setValidator(RGB5validator)
        self.blue_value_line_edit.setMaxLength(2)
        self.blue_value_line_edit.setAlignment(Qt.AlignRight)
        self.blue_value_line_edit.textChanged.connect(self.crl_changed)

        savebutton = QPushButton('Save')
        savebutton.clicked.connect(self.save)

        layout = QFormLayout()
        layout.addRow("Red", self.red_value_line_edit)
        layout.addRow("Green", self.green_value_line_edit)
        layout.addRow("Blue", self.blue_value_line_edit)

        layout.addWidget(savebutton)
        self.setLayout(layout)
    
    def crl_changed(self):
        pal = self.palette()
        crl = self.common_backend.rgb5_to_rgb8(self.red_value_line_edit.text(), self.green_value_line_edit.text(), self.blue_value_line_edit.text())
        pal.setColor(self.backgroundRole(), QColor(*crl))
        self.setPalette(pal)
    
    def save(self):
        pass


def on_savebutton_click():
    global clr
    global pal
    global pal_index
    
    alert = QMessageBox()
    alert.setText('Saved.')
    if redvalue.text() != '':
        R = int(redvalue.text())
    else:
        R = 0
    if greenvalue.text() != '':
        G = int(greenvalue.text())
    else:
        G = 0
    if bluevalue.text() != '':
        B = int(bluevalue.text())
    else:
        B = 0
    
    clr = [R, G, B]
    alert.exec_()
    clr_mixer_root.hide()
    
    pal[pal_index[0]] = clr


def color_mixer(r, g, b):
    global clr

    clr = [r, g, b]
    
    redvalue.setText(str(r))
    greenvalue.setText(str(g))
    bluevalue.setText(str(b))
    
    clr_mixer_root.show()
    clr_mixer_app.exec_()