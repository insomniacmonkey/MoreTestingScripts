from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from password import *
from PIL import Image 
import pytesseract
import time
import datetime

loginURL = "https://master.thorhudl.com/login"
videoSpaURL = "https://master.thorhudl.com/watch/video/VmlkZW81ZjBjYTEyYjdjMGE1YjYxY2NiOTcxMzY=/organizer"
windowsReadTheImagePath = "C:/Users/chanse.strode/Documents/GitHub/MoreTestingScripts/Scripts/VideoPlayer/croppedImage.png"

##login
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_position(0, 0)
driver.set_window_size(1200, 700)
driver.get(loginURL)
time.sleep(1)
emailField = driver.find_element_by_id("email")
emailField.send_keys(myEmail)
passwordField = driver.find_element_by_id("password")
passwordField.send_keys(password)
passwordField.submit()

##Load Video Spa Page
driver.get(videoSpaURL)
#let the player play for 15 seconds. This has to be a number that doesn't have a "0" in it due to image text conversion below. 
time.sleep(5)
#pause player
pauseButton = driver.find_element_by_xpath("//*[@data-qa-id='vi-controls-playpause']")
pauseButton.click()
#get play time
playTime = driver.find_element_by_xpath("//*[@data-qa-id='player-time-label']")
getPausedRunTime = playTime.text.split("/")
getJustTheSeconds = getPausedRunTime[0].split(":")
currentPlayTime = int(getJustTheSeconds[1])
print("Playhead Time: " + str(currentPlayTime))
#grab Screen shot of the vspa page
driver.get_screenshot_as_file("screenshot.png")
theImage = Image.open(r"C:/Users/chanse.strode/Documents/GitHub/MoreTestingScripts/Scripts/VideoPlayer/screenshot.png") 


width, height = theImage.size
print(width,height)
# Setting the points in pixels for cropped image. If we force the browser size we can use this approach. 
#number of pixels starting from the left side of the screen. the more you add the further RIGHT it goes.
windowsLeft = 250  
windowsTop = 200  
windowRight = 600
windowsBottom = 400
    
# Cropped image of above dimension 
# (It will not change orginal image) 
cropTheImage = theImage.crop((windowsLeft, windowsTop, windowRight, windowsBottom)) 
    
# Shows the image in image viewer 
cropTheImage.save("croppedImage.png") 
# navigate to pytesseract exe location
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/chanse.strode/Documents/tesseract/tesseract'

#get the image and convert it to text
readTheImageTime = pytesseract.image_to_string("C:/Users/chanse.strode/Documents/GitHub/MoreTestingScripts/Scripts/VideoPlayer/croppedImage.png")
print(str(readTheImageTime))
getNumber = readTheImageTime[0] #gets the first character in the string
print(getNumber)
convertedImageTime = int(getNumber)
print("Displayed Time: " + str(convertedImageTime))

#check to see if the player has played at least 10 seconds
playTimeDifference = currentPlayTime - convertedImageTime
print("Difference in Seconds: " + str(playTimeDifference))
#Check to see if play head time and whats on the screen is within 1 second
if abs(playTimeDifference) >= 2:
    print("ERROR: The difference between the playhead time and displayed time is greater than 1 second:")
    print("Playhead Time: " + str(currentPlayTime))
    print("Displayed Time: " + str(convertedImageTime))
else:
    print("SUCCESS! TEST PASSED!")

driver.close()
