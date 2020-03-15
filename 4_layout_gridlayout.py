import sys
from PySide2.QtWidgets import QApplication, QWidget, QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout, QSpinBox, QGridLayout, QSizePolicy, QStyle
from PySide2.QtCore import Qt, QSize

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("Grid layout 공부할거야")
        self.vb = QVBoxLayout()
        self.setLayout(self.vb)

        self.ln = QLineEdit()
        self.ln.setAlignment(Qt.AlignRight)
        ### 이야 이렇게 하면 스타일 바꿀수 있구낭
        self.ln.setStyleSheet("font-size: 24px;"
                              "font-weight: bold;")
        self.vb.addWidget(self.ln)



        self.gl = QGridLayout()
        self.vb.addLayout(self.gl)

        self.value = [
            [QPushButton('+-'), [0, 0]],
            [QPushButton('/'), [0, 1]],
            [QPushButton('*'), [0, 2]],
            [QPushButton('-'), [0, 3]],
            [QPushButton('1'), [1, 0]],
            [QPushButton('2'), [1, 1]],
            [QPushButton('3'), [1, 2]],
            [QPushButton('+'), [1, 3, 2, 1]],
            [QPushButton('4'), [2, 0]],
            [QPushButton('5'), [2, 1]],
            [QPushButton('6'), [2, 2]],
            [QPushButton('7'), [3, 0]],
            [QPushButton('8'), [3, 1]],
            [QPushButton('9'), [3, 2]],
            [QPushButton('='), [3, 3, 2, 1]],
            [QPushButton('0'), [4, 0, 1, 2]],
            [QPushButton('.'), [4, 2]],
        ]

        for i, p in self.value:
            if len(p) > 2:
                i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.gl.addWidget(i, p[0],p[1],p[2],p[3])
            else:
                self.gl.addWidget(i, p[0],p[1])
            i.setStyleSheet("font-size:20px;"
                            "font-weight: bold;")
            i.clicked.connect(self.clk)

    def clk(self):
        self.ln.setText(self.ln.text()+self.sender().text())

app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())
