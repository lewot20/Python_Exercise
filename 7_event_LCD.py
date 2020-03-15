import sys
from PySide2.QtWidgets import QApplication, QWidget, QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout, QSpinBox, QGridLayout, QSizePolicy, QStyle, QStackedLayout, QLCDNumber, QSlider
from PySide2.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle(" ")
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vb = QVBoxLayout()
        vb.addWidget(lcd)
        vb.addWidget(sld)

        self.setLayout(vb)
        sld.valueChanged.connect(lcd.display)

        self.resize(250,150)



app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())