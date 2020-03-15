import sys
from PySide2.QtWidgets import QApplication, QWidget, QApplication, QLabel, QWidget, QPushButton, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QFormLayout, QSpinBox, QGridLayout, QSizePolicy, QStyle, QStackedLayout
from PySide2.QtCore import Qt
import pyautogui
import time

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("마우스 프로그램")
        self.initUI()

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


        gl.setSpacing(100)
        x = 0
        y = 0
        z = 0
        r = 0
        d = 0

        self.text = "X:{0}, Y:{1}, R:{2}, G:{3}, B:{4}".format(x,y,z,r,d)
        self.lbl = QLabel(self.text, self)
        gl.addWidget(self.lbl, 0, 0, Qt.AlignTop)

        self.setLayout(vb)

        self.resize(350,200)
        self.show()
        self.MouseTracking()

    def MouseTracking(self):
        try:
            while True:
                x, y = pyautogui.position()

                # positionStr = 'X:' + str(x).rjust(4) + '  Y:' + str(y).rjust(4)
                pixelColor = pyautogui.screenshot().getpixel((x, y))
                # positionStr += ' RGB : (' + str(pixelColor[0]).rjust(3)
                # positionStr += ',  ' + str(pixelColor[1]).rjust(3)
                # positionStr += ',  ' + str(pixelColor[2]).rjust(3) + ')'
                # print(positionStr, end='')
                #                 # time.sleep(0.2)
                #                 # print('\b' * len(positionStr), end='', flush=True)
                #
                # x = int(x)
                # y = int(y)
                z = int(pixelColor[0])
                r = int(pixelColor[1])
                d = int(pixelColor[2])

                text = "X:{0}, Y:{1}, R:{2}, G:{3}, B:{4}".format(x, y, z, r, d)
                self.lbl.setText(text)
                time.sleep(1)

        except KeyboardInterrupt :
            print('\nDone.')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())