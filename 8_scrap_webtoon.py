from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer
from bs4 import BeautifulSoup as bs
import urllib.request as req, sys, time
from scrap_Ui_01 import Ui_MainWindow
import logging

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.chk)
        self.timer.setInterval(5*60*1000) # 1000은 ms이다.
        self.rb_5min.setChecked(True)
        self.show()

    def setCycle(self):
        if self.rb_30min.isChecked():
            self.timer.setInterval(30* 60 * 1000)
        elif self.rb_10min.isChecked():
            self.timer.setInterval(10* 60* 1000)
        elif self.rb_5min.isChecked():
            self.timer.setInterval(5* 60* 1000)
        elif self.rb_30sec.isChecked():
            self.timer.setInterval(30* 1000)
        else:
            self.timer.setInterval(10* 1000)

    def startChk(self):
        self.lineEdit.setEnabled(False)
        self.timer.start()

    def stopChk(self):
        self.lineEdit.setEnabled(True)
        self.timer.stop()

    def chk(self):
        self.rsp = req.urlopen(self.lineEdit.text())
        self.html = bs(self.rsp, "html.parser")
        logger = logging.Logger('catch_all')
        try:
             if self.html.find(alt="UP").attrs['alt'] == "UP":
                self.test == "업데이트 완료 되었습니다."
        except:
            self.test = "아직 업데이트 되지 않았습니다."

        self.t = time.localtime()
        self.label_3.setText("{}:{}:{} 체크결과: {}".format(self.t.tm_hour, self.t.tm_min, self.t.tm_sec, self.test))

app = QApplication([])
form = Form()
sys.exit(app.exec_())