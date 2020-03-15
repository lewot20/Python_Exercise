import pyperclip
import pyautogui
import time
import openpyxl

#TODO : 개인별 검진현황 넣고 싶은 연월 입력하기


#TODO : 일특채 수검자 넣고 싶은 연월 입력하기


#TODO : G-health 실행하기
pyautogui.PAUSE = 0.2
pyautogui.doubleClick(1546,36)
pyautogui.PAUSE = 1
pyautogui.click(975,470)
pyautogui.pause = 1

#TODO : 로그인하기
pyautogui.click(1230,710)
pyperclip.copy('admin')
pyautogui.hotkey('ctrl','v')
pyautogui.typewrite('\n')
pyautogui.typewrite('1230')
pyautogui.typewrite('\n')
pyautogui.click(655,367)
time.sleep(1)
pyautogui.hotkey('alt','space','x')
pyautogui.keyDown('altleft')
pyautogui.keyUp('altleft')
pyautogui.press('right')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')

#TODO : 개인별검진현황 일자 조회
pyautogui.click(101,83)
pyautogui.click(668,84)
pyautogui.press('1')
pyautogui.press('0')
pyautogui.click(693,84)
pyautogui.press('0')
pyautogui.press('4')
pyautogui.click(778,84)
pyautogui.press('1')
pyautogui.press('0')
pyautogui.click(798,84)
pyautogui.press('0')
pyautogui.press('4')

#TODO : 자료조회 누르기
pyautogui.click(1040,95)
time.sleep(25)
pyautogui.click(977,590)
pyautogui.click(1169,95)
time.sleep(5)

#TODO : 엑셀 저장하기
pyautogui.hotkey('alt','space','x')
pyautogui.hotkey('ctrl','s')
pyautogui.click(254,357)
pyautogui.hotkey('alt','space','x')
pyautogui.press('x')
pyautogui.click(505,49)
pyautogui.typewrite('')

