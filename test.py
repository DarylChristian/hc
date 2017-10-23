from selenium import webdriver
import pyautogui as gui
import time
from selenium.webdriver.common.keys import Keys



version_pos = gui.locateCenterOnScreen('ie_version.PNG')
time.sleep(5)
gui.click(version_pos)
time.sleep(2)
new_version_pos = gui.locateCenterOnScreen('ie_version_9.PNG')
time.sleep(5)
gui.click(new_version_pos)
