import time
import pyautogui

while True:
    pyautogui.move(10, 0)  # Move 10 pixels para a direita
    time.sleep(20)
    pyautogui.move(-10, 0)  # Move 10 pixels para a esquerda
    time.sleep(20)
