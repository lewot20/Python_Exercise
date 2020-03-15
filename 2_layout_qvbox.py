from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("차근차근")

        ### 여기가 핵심입니다. #####
        self.vb = QVBoxLayout()
        self.setLayout(self.vb)

        self.hbTop = QHBoxLayout()
        self.hbMid = QHBoxLayout()
        self.hbBot = QHBoxLayout()
        ### 여기까지

        self.vb.addLayout(self.hbTop)
        self.vb.addStretch()

        self.vb.addLayout(self.hbMid)

        self.vb.addLayout(self.hbBot)

        self.lbl  = QLabel("박스 레이아웃 예제")
        self.ln = QLineEdit()
        self.btn1 = QPushButton("출력")
        self.btn2 = QPushButton("지우기")
        self.btn3 = QPushButton("출력하고 지우기")

        self.hbTop.addWidget(self.lbl)
        self.hbTop.addWidget(self.ln)
        self.hbMid.addWidget(self.btn1)
        self.hbBot.addWidget(self.btn2)
        self.hbBot.addStretch()
        self.hbBot.addWidget(self.btn3)

        self.btn1.clicked.connect(self.prt_line)
        self.btn2.clicked.connect(self.del_line)
        self.btn3.clicked.connect(self.prt_del)

    def prt_line(self):
        print(self.ln.text())

    def del_line(self):
        self.ln.clear()

    def prt_del(self):
        self.prt_line()
        self.del_line()


app = QApplication([])
form = Form()
form.show()
app.exec_()