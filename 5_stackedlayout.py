import sys
from PySide2.QtWidgets import QApplication, QWidget, QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout, QSpinBox, QStackedLayout
from PySide2.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("stacked layout ")

        self.wgtA = QWidget()
        self.wgtA_vl = QVBoxLayout()
        self.btnA = QPushButton("A")
        self.btnB = QPushButton("B")
        self.btnC = QPushButton("C")
        self.wgtA_vl.addWidget(self.btnA)
        self.wgtA_vl.addWidget(self.btnB)
        self.wgtA_vl.addWidget(self.btnC)
        self.wgtA.setLayout(self.wgtA_vl)

        self.wgt1 = QWidget()
        self.wgt1_vl = QVBoxLayout()
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.wgt1_vl.addWidget(self.btn1)
        self.wgt1_vl.addWidget(self.btn2)
        self.wgt1_vl.addWidget(self.btn3)
        self.wgt1.setLayout(self.wgt1_vl)

        self.wgtGA = QWidget()
        self.wgtGA_vl = QVBoxLayout()
        self.btnGA = QPushButton("가")
        self.btnNA = QPushButton("나")
        self.btnDA = QPushButton("다")
        self.wgtGA_vl.addWidget(self.btnGA)
        self.wgtGA_vl.addWidget(self.btnNA)
        self.wgtGA_vl.addWidget(self.btnDA)
        self.wgtGA.setLayout(self.wgtGA_vl)

        self.layout = QStackedLayout()
        self.layout.addWidget(self.wgtA)
        self.layout.addWidget(self.wgt1)
        self.layout.addWidget(self.wgtGA)
        self.setLayout(self.layout)

        self.btnA.clicked.connect(lambda s=None, i = 0: self.set_stack_index(s,i))
        self.btnB.clicked.connect(lambda s=None, i=1: self.set_stack_index(s, i))
        self.btnC.clicked.connect(lambda s=None, i=2: self.set_stack_index(s, i))

        self.btn1.clicked.connect(lambda s=None, i=0: self.set_stack_index(s, i))
        self.btn2.clicked.connect(lambda s=None, i=1: self.set_stack_index(s, i))
        self.btn3.clicked.connect(lambda s=None, i=2: self.set_stack_index(s, i))

        self.btnGA.clicked.connect(lambda s=None, i=0: self.set_stack_index(s, i))
        self.btnNA.clicked.connect(lambda s=None, i=1: self.set_stack_index(s, i))
        self.btnDA.clicked.connect(lambda s=None, i=2: self.set_stack_index(s, i))

    def set_stack_index(self, s, i):
        self.layout.setCurrentIndex(i)


app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())