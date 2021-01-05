import pyautogui
# sometimes u gotta retake the screenshots.
images = ["images/auto.png", "images/7.png", "images/fight.png", "images/isgilham.png", "images/map.png", "images/next.png", "images/replay.png"]

print("Creator: Splexas\n")
while True:
    for i in images:
        coords = pyautogui.locateCenterOnScreen(i)
        if coords == None:
            pass
        else:
            x, y = coords
            pyautogui.click(x, y)
            print(f"Clicked on: {i}")