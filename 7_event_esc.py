import sys
from PySide2.QtWidgets import QApplication, QWidget, QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout, QSpinBox, QGridLayout, QSizePolicy, QStyle, QStackedLayout
from PySide2.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle(" ")
        self.initUI()

    def initUI(self):
        self.resize(250,150)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())