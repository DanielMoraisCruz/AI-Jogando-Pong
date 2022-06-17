import pyautogui


def print_tela():
    sc = pyautogui.screenshot(region=(63, 369, 814, 602))
    sc.save('exemplo.png')
