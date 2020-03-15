import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QPushButton, QToolTip, QAction, qApp, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt, QTime


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('눌러보시게나', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(100, 200)
        btn.resize(btn.sizeHint())

        quit_btn = QPushButton('종료', self)
        quit_btn.move(100, 350)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.clicked.connect(QCoreApplication.instance().quit)

        #메뉴 만들기
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate) +' '+ self.time.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('haeboja')
        self.setWindowIcon(QIcon('yonsei.ico'))
        self.resize (300, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())