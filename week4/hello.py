import pyautogui

with open("hello.txt") as file:
    re = file.readlines()
    for i in re:
        newline = i.replace("\n", "")
        pyautogui.shortcut("ctrl", "a")
        pyautogui.press("delete")
        pyautogui.typewrite(newline)
        pyautogui.press("enter")
