import pywinctl
import pyautogui
import pydirectinput
import time
import cv2
import glob
import os
import threading


def otpokemon_active():
    window_name = pywinctl.getActiveWindowTitle()
    return window_name and window_name.find("otPokemon") != -1


def search_loot(sprite, screenshot):
    try:
        loot = pyautogui.locate(sprite, screenshot, confidence=0.7)
        print("Loot encontrado!")
        sprite_center = pyautogui.center(loot)
        pydirectinput.click(pokeball.x, pokeball.y)
        pydirectinput.click(sprite_center.x, sprite_center.y)
    except:
        pass


pokeball = None
pokeball_image = cv2.imread("pokeball.png")
print("Procurando pokeball...")
while not pokeball:
    if otpokemon_active():
        try:
            pokeball = pyautogui.locateCenterOnScreen(pokeball_image, confidence=0.9)
            print("Pokeball encontrada!")
        except:
            time.sleep(1)

sprites = []
for sprite in glob.glob(os.path.join("sprites", "*.png")):
    sprites.append(cv2.imread(sprite))
print("Procurando loot...")
while True:
    if otpokemon_active():
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        threads = []
        for sprite in sprites:
            thread = threading.Thread(target=search_loot, args=(sprite, screenshot))
            threads.append(thread)
            thread.start()
        thread.join()
