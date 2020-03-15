# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autoxray.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        icon_path = resource_path("./images/x-ray-icon.ico")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.lbl1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl1.setGeometry(QtCore.QRect(20, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl1.setFont(font)
        self.lbl1.setObjectName("lbl1")
        self.spbNumber = QtWidgets.QSpinBox(self.centralwidget)
        self.spbNumber.setGeometry(QtCore.QRect(220, 20, 71, 41))
        self.spbNumber.setRange(0,500)
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spbNumber.setFont(font)
        self.spbNumber.setObjectName("spbNumber")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(40, 80, 101, 51))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(160, 80, 101, 51))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnStop.setFont(font)
        self.btnStop.setObjectName("btnStop")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 150, 281, 16))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 281, 16))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 281, 16))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(20, 210, 261, 121))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_result.setFont(font)
        self.lbl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_result.setObjectName("lbl_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menu.addAction(self.actionQuit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        # self.spbNumber.valueChanged.connect(MainWindow.selectNumber)
        self.btnStart.clicked.connect(MainWindow.startChk)
        self.btnStop.clicked.connect(MainWindow.stopChk)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Onit X-ray 판정"))
        self.lbl1.setText(_translate("MainWindow", "검진 인원을 입력하세요"))
        self.btnStart.setText(_translate("MainWindow", "판정 시작"))
        self.btnStop.setText(_translate("MainWindow", "판정 종료"))
        self.label.setText(_translate("MainWindow", "이 프로그램은 모든 흉부방사선을 정상 판정합니다. "))
        self.label_2.setText(_translate("MainWindow", "일반검진, 저장후 자동 다음사람선택 체크 필요"))
        self.label_3.setText(_translate("MainWindow", "골밀도 검사 확인 필요한 수검자명 ↓"))
        self.lbl_result.setText(_translate("MainWindow", "확인 필요 수검자명"))
        self.menu.setTitle(_translate("MainWindow", "메뉴"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
