import sys
from PySide2.QtWidgets import QApplication, QWidget, QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout, QSpinBox, QGridLayout, QSizePolicy, QStyle, QStackedLayout
from PySide2.QtCore import Qt


class Btn(QPushButton):
    def __init__(self, caption):
        super(Btn, self).__init__()
        self.setText(caption)
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Expanding)
        self.setFixedSize(150, 150)
        self.setStyleSheet("font-size: 20px;"
                           "font-weight: bold;")


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("Signal & Slot")
        self.resize(700,500)

        self.vb = QVBoxLayout()
        self.hbMid = QHBoxLayout()

        self.vb.addStretch()
        self.vb.addLayout(self.hbMid)
        self.vb.addStretch()

        self.gl = QGridLayout()
        self.hbMid.addStretch()
        self.hbMid.addLayout(self.gl)
        self.hbMid.addStretch()

        self.setLayout(self.vb)

        self.btnPressed = Btn("Pressed")
        self.btnReleased = Btn("Released")
        self.btnClicked = Btn("Clicked")
        self.btnToggled = Btn("Toggled")
        self.btnToggled.setCheckable(True)
        self.btnReset = Btn("reset")
        self.btnLambda = Btn("Lambda")

        self.gl.addWidget(self.btnPressed, 0, 0)
        self.gl.addWidget(self.btnReleased, 0, 1)
        self.gl.addWidget(self.btnLambda, 0, 2)
        self.gl.addWidget(self.btnClicked, 1, 0)
        self.gl.addWidget(self.btnToggled, 1, 1)
        self.gl.addWidget(self.btnReset, 1, 2)

        self.btnPressed.pressed.connect(self.sendText)
        self.btnReleased.released.connect(self.sendText)
        self.btnClicked.clicked.connect(self.sendText)
        self.btnToggled.toggled.connect(self.sendText)
        self.btnReset.clicked.connect(self.reset)
        self.btnLambda.pressed.connect(
            lambda: self.test_lambda(self.btnReset.text()))

        self.cnt = 0
        self.cntt = 0

    def clkCnt(self):
        self.cnt +=1
        self.btnReset.setText(str(self.cnt))

    def sendText(self):
        self.clkCnt()
        print(self.sender().text())

    def test_lambda(self, i):
        print("입력:{}".format(i))
        self.clkCnt()


    def reset(self):
        self.cnt = 0
        if self.cnt == 0 :
            self.cntt = "Reset"
        else:
            self.cntt = self.cnt
        self.btnReset.setText(str(self.cntt))


### 람다를 한번 이해해보자꾸나


app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())