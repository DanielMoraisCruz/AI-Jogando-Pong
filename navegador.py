import pyautogui
import pyperclip


def iniciar_Navegador():
    """Funcao que abre o navegador chrome
    """
    pyautogui.moveTo(583, 1054, 3)
    pyautogui.click()

    pyautogui.moveTo(196, 58, 3)
    pyautogui.click()

    pyperclip.copy('https://www.google.com/logos/2010/pacman10-i.html')

    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('enter', 3)
