import sys
from PyQt5.QtWidgets import QApplication, QWidget, QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout, QSpinBox
from PyQt5.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("폼 레이아웃 설명")

        ###여기서부터 중요합니다.
        ### Formlayout에 대하여 배운다.
        self.form = QFormLayout()
        self.setLayout(self.form)
        ### 위젯간의 간격을 조정한다.
        self.form.setVerticalSpacing(10)

        ### 레이블의 정렬을 조정할 때 Qt를 불러와야함
        self.form.setLabelAlignment(Qt.AlignLeft)

        self.lnName = QLineEdit()
        self.lnId = QLineEdit()
        self.btnFindId = QPushButton("중복검사")

        self.form.addRow("이름 : ", self.lnName)

        self.vbId = QHBoxLayout()
        self.vbId.addWidget(self.lnId)
        self.vbId.addWidget(self.btnFindId)

        self.form.addRow("ID : ", self.vbId)

        self.lnPNum2 = QLineEdit()
        self.form.addRow("보호자 연락처 : ", self.lnPNum2)


        ### addWidget을 쓰면 label없이 우측에만 위젯을 추가할 수 있다
        ### addRow와는 다른 기능으로 위젯 쪽에만 추가!
        self.lblChkId = QLabel("ID 중복검사를 진행해주세요")
        self.form.addWidget(self.lblChkId)

        self.spAge = QSpinBox()
        self.spAge.setValue(19)
        self.lnPNum = QLineEdit()

        self.form.addRow("나이 : ", self.spAge)
        self.form.addRow("연락처", self.lnPNum)

        ### addRow를 label없이 그냥 쓰면 전체 길이로 위젯이 추가된다.
        ### 만약에 위와 같이 label이었다면 allign이 왼쪽이니까 왼쪽부터 추가됨.
        ### 그러나 label의 길이는 전체였을 것임.
        ### 글자 길이만 작은것일 뿐
        self.btnOk = QPushButton("확인")
        self.form.addRow(self.btnOk)

        ### 보호자 비활성화
        self.spAge.valueChanged[int].connect(self.chk_age)

        ### id 중복체크
        self.btnFindId.clicked.connect(self.chk_id)

        ### 확인
        self.btnOk.clicked.connect(self.chk_ok)


    def chk_age(self, v):
        if v < 20:
            self.lnPNum2.setEnabled(True)
        else:
            self.lnPNum2.setEnabled(False)

    def chk_id(self):
        ids = ["return", "zero", "abc", "python", "class"]
        if len(self.lnId.text()) <2:
            self.lblChkId.setText("2글자 이상 입력하세요")
        else :
            if ids.count(self.lnId.text()) == 1:
                self.lblChkId.setText("중복되는 ID가 존재합니다")
            else :
                self.lblChkId.setText("멋진 ID입니다!")

    def chk_ok(self):
        str = ""
        if self.lnName.text() =="":
            str += "이름"
        if self.lblChkId.text() != "멋진 ID입니다!":
            str += "ID"
        if len(self.lnPNum.text()) < 13:
            str += "연락처"
        if str != "":
            self.btnOk.setText(str + "을(를) 확인하세요")
        else:
            self.btnOk.setText("처리되었습니다")

app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())
