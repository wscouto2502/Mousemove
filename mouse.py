import time
import pyautogui

while True:
    pyautogui.move(10, 0)  # Move 10 pixels para a direita
    print('movido para direita')
    time.sleep(20)
    pyautogui.move(-10, 0)  # Move 10 pixels para a esquerda
    print('movido para esquerda')
    time.sleep(20)
