from selenium import webdriver
import pyautogui as gui
import time
from selenium.webdriver.common.keys import Keys


#launching ie
vpnLink = "https://manila1-dcn-ras.accenture.com/dana-na/auth/url_17/welcome.cgi"
browser = webdriver.Ie("C:/Users/daryl.c.m.cabacungan/Desktop/hc/IEDriverServer.exe")
gui.press('f6')
gui.typewrite(vpnLink)
gui.press('enter')
time.sleep(5)
gui.press('f12')
time.sleep(5)
version_pos = gui.locateCenterOnScreen('ie_version.PNG')
time.sleep(5)
if(version_pos == None):
	print("Cant find the image. Exiting now...")
else:
	print(version_pos)
	gui.click(version_pos)
	time.sleep(2)
	new_version_pos = gui.locateCenterOnScreen('ie_version_9.PNG')
	time.sleep(5)
	if(new_version_pos == None):
		print("Cant find the image. Exiting now...")
	else:
		gui.click(new_version_pos)
		time.sleep(5)
		gui.typewrite("daryl.c.m.cabacungan")
		gui.press('tab')
		gui.typewrite("")
		gui.press('tab')
		gui.press('enter')
		time.sleep(2)
		gui.press('enter')

#time.sleep(5)
#gui.click(version_pos)
#time.sleep(2)
#new_version_pos = gui.locateCenterOnScreen('ie_version_9.PNG')
#time.sleep(5)
#gui.click(new_version_pos)
