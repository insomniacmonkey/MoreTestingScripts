from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from password import *
import time
import datetime

##Load Page
driver = webdriver.Chrome()
driver.get(thorenv)
time.sleep(1)

#Load stream info
inputElement = driver.find_element_by_xpath("//*[@id='player-stream-src']")
inputElement.clear()
inputElement.send_keys(videoSrc)
submitButton = driver.find_element_by_id("player-stream-load").click()
time.sleep(3)

#Select 2x speed
setTheSpeed = driver.find_element_by_xpath("//*[@id='player-playbackrate']/option[5]").click()


currentTimeString = "intial set 1"
print(currentTimeString + "first time being set not in loop 1")

currentTimeSecondCheckString = "intial set 2"
print(currentTimeSecondCheckString +  "first time being set not in loop 1")

driftTime = driver.execute_script("return document.getElementById('drift').value;")
msToSeconds = float(driftTime) / 1000
#Get current Time
def firstTimeCheck():
    time.sleep(1)
    currentTime = driver.execute_script("return document.getElementById('player-current-time').value;")
    currentTimeString = str(int(float(currentTime)))
    print(currentTimeString)



def secondTimeCheck():
    time.sleep(3)
    currentTimeSecondCheck = driver.execute_script("return document.getElementById('player-current-time').value;")
    currentTimeSecondCheckString = str(int(float(currentTimeSecondCheck)))
    print(currentTimeSecondCheckString)

#Write a while loop that checks if current time = duration and continually update the drift ammount.
#TODO the current time and play time will be different because of drift... we need a way to confirm that they should match.
while currentTime != currentTimeSecondCheck:
    firstTimeCheck()
    currentTimeString
    print(currentTimeString + "loop run 1")
    secondTimeCheck()
    print(currentTimeSecondCheckString + "loop run 2")
    currentTimeSecondCheckString


    #Get drift and convert from ms to seconds
    driftTime = driver.execute_script("return document.getElementById('drift').value;")
    msToSeconds = float(driftTime) / 1000


    print ("Current Time: " + str(currentTimeString) + " in Seconds")
    print ("Current Drift: " + str(float(msToSeconds)) + " in Seconds")
    time.sleep(5)



print("Finished!")
print ("Final Time: " + currentTimeString + " in Seconds")
print ("Final Drift: " + str(float(msToSeconds)) + " in Seconds")

#TODO: print/write out drift difference to a file.

#TODO: decide if we want to wrap it all in a for loop to test multiple videos
driver.close()
