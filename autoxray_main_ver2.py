from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import pyautogui
import pyperclip
import os
import sys, time
from autoxray import Ui_MainWindow
import logging

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.DXA = 'DXA 확인 : '
        self.pjNumber = 0

        icon_path = resource_path("./images/x-ray-icon.ico")
        self.setWindowIcon(QIcon(icon_path))

    # def selectNumber(self):
    #     self.pjNumber = self.spbNumber.value()
    #     print(self.pjNumber)

    def startChk(self):
        self.spbNumber.setEnabled(True)
        print(str(self.spbNumber.value()) + "명의 정상 판정을 시작합니다.")
        self.chk()


    def stopChk(self):
        self.spbNumber.setAccelerated(True)
        sys.exit()

    def chk(self):
        def findChestXray():
            try:
                return pyautogui.locateCenterOnScreen('./images/chestXray.png')
            except:
                return 0

        def findDXA():
            try:
                return pyautogui.locateCenterOnScreen('./images/DXA.png')
            except:
                return 0

        for i in range(self.spbNumber.value()):
            print(str(i+1) + ' cycle 진행 시작')
            a = findChestXray()
            b = findDXA()

            if a != 0 and b != 0 : # Xray도 있고 골밀도 검사도 있는 경우
                print("흉부방사선과 골밀도를 모두 찾았습니다.")
                chestXray_position_x, chestXray_position_y = a
                pyautogui.click(chestXray_position_x + 140, chestXray_position_y, clicks=1, interval=0.5)
                pyautogui.press('1')
                pyautogui.click(585,90) # 사람 이름 클릭하기
                pyautogui.hotkey('Ctrl', 'c')
                self.DXA += '\'' + pyperclip.paste() +'\'' + ' ' #복사되어 있는 값 붙여넣기
                self.lbl_result.setText(self.DXA)
                pyautogui.click(1650, 250, clicks=1, interval=0.5) #자료처리 누르기
                time.sleep(2)
                pyautogui.press('space')

            elif a != 0 and b == 0 :  # Xray만 있는 대부분의 경우
                print("흉부방사선만 찾았습니다.")
                chestXray_position_x, chestXray_position_y = a
                pyautogui.click(chestXray_position_x + 140, chestXray_position_y, clicks=1, interval=0.5)
                pyautogui.press('1')
                pyautogui.click(1650, 250, clicks=1, interval=0.5)  # 자료처리 누르기
                time.sleep(2)
                pyautogui.press('space')

            else:
                print('흉부방사선검사 결과와 골밀도 검사를 찾는 도중 오류가 발생하였습니다.')



app = QApplication([])
form = Form()
sys.exit(app.exec_())