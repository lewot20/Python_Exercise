import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout,  QGridLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
import pyautogui



class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("마우스 추적 프로그램")
        self.initUI()
        self.setWindowIcon(QIcon('mouse.ico'))

        oImage = QImage("background.png")
        sImage = oImage.scaled(QSize(400, 300))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))  # Palette.window는 배경을 설정하겠다는 뜻
        self.setPalette(palette)


    def initUI(self):

        vb = QVBoxLayout()
        hbMid = QHBoxLayout()

        vb.addStretch()
        vb.addLayout(hbMid)
        vb.addStretch()

        gl = QGridLayout()
        hbMid.addStretch()
        hbMid.addLayout(gl)
        hbMid.addStretch()

        gl.setSpacing(30)
        x = 0
        y = 0
        z = 0
        r = 0
        d = 0

        self.lbl2 = QLabel("스페이스 바를 누르십시오")
        gl.addWidget(self.lbl2, 0, 0, Qt.AlignCenter)

        self.text = "X:{0}, Y:{1}, R:{2}, G:{3}, B:{4}".format(x, y, z, r, d)
        self.lbl = QLabel(self.text, self)
        self.lbl.setStyleSheet("font-size: 20px;"
                               "color: white;"
                              "font-weight: bold;"
                               )
        gl.addWidget(self.lbl, 1, 0, Qt.AlignCenter)



        self.setLayout(vb)

        self.resize(400, 200)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            self.mouseTracking()

    def mouseTracking(self):
        x,y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        z = int(pixelColor[0])
        r = int(pixelColor[1])
        d = int(pixelColor[2])

        text = "X:{0}, Y:{1}, R:{2}, G:{3}, B:{4}".format(x, y, z, r, d)
        self.lbl.setText(text)
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())