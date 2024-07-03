import pyautogui
import random
import sys

pyautogui.useImageNotFoundException(False)

def main():
  pyautogui.hotkey('alt', 'tab')

  pyautogui.sleep(1)

  repeat = True

  while repeat:
    settingImg = pyautogui.locateOnScreen('images/setting.png', minSearchTime=2, confidence=0.9)
    if settingImg:
      pyautogui.leftClick(966, 668, duration=0.5)
    else:
      imgNotFound()
      repeat = False

    cancelImg = pyautogui.locateCenterOnScreen('images/cancel.png', minSearchTime=2, confidence=0.9)
    if cancelImg:
      pyautogui.leftClick(cancelImg.x, cancelImg.y, duration=0.5)
    else:
      imgNotFound()
      repeat = False

    pyautogui.sleep(random.randint(10, 30))

def imgNotFound():
  pyautogui.alert(text='Image not found', title='Error', button='OK')
  sys.exit("Image not found")

main()