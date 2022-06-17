import pyautogui
import pyperclip
from neural.indentifica import print_tela


def iniciar_Navegador():
    """Funcao que abre o navegador chrome
    """
    pyautogui.moveTo(583, 1054)
    pyautogui.click()

    pyautogui.moveTo(190, 70, 2)
    pyautogui.click()

    pyperclip.copy('https://www.ponggame.org/')

    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('enter')

    pyautogui.moveTo(450, 450, 5)

    pyautogui.scroll(-325)

    print_tela()
