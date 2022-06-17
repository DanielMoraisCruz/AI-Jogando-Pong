import pyautogui


ident = pyautogui.pixel(100, 100)

print(ident)

r = ident[0]
g = ident[1]
b = ident[2]

print(r, g, b)
