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

#initialzing values so the first while loop runs
currentTime = 0
currentTimeString = ""
currentTimeSecondCheck = 0
currentTimeSecondCheckString = "2"
driftTime = 0
msToSeconds = 0
expectedDuration = int(float(driver.execute_script("return document.getElementById('player-expected-duration').value;")))
#Get current Time
def firstTimeCheck():
    time.sleep(1)
    global currentTime
    global currentTimeString
    currentTime = int(float(driver.execute_script("return document.getElementById('player-current-time').value;")))
    currentTimeString = str(currentTime)

def secondTimeCheck():
    time.sleep(3)
    global currentTimeSecondCheck
    global currentTimeSecondCheckString
    currentTimeSecondCheck = int(float(driver.execute_script("return document.getElementById('player-current-time').value;")))
    currentTimeSecondCheckString = str(currentTimeSecondCheck)


#Write a while loop that checks if current time = duration and continually update the drift ammount.
#TODO the current time and play time will be different because of drift... we need a way to confirm that they should match.
#TODO log
while currentTimeString != currentTimeSecondCheckString:
    #get the duration
    firstTimeCheck()
    secondTimeCheck()
    #Get drift and convert from ms to seconds
    driftTime = float(driver.execute_script("return document.getElementById('drift').value;"))
    msToSeconds = str(round(float(driftTime / 1000),2))

    percentComplete = round(float(currentTimeSecondCheck / expectedDuration),2) * 100
    print ("Current Time: " + currentTimeString + " Seconds")
    print ("Percent Complete: " + str(percentComplete) + "%")
    print ("Current Drift: " + msToSeconds + "  Seconds")
    print ("------------------------------")
    time.sleep(5)

#add timeout for while loop

print("Finished!")
#log a message depending on playback completion (maybe change this to ammount of drift? or ammount of drift compared to total video length)
print ("Percent Complete: " + str(percentComplete) + "%")
if percentComplete <= 80:
    print("CRITICAL FAILURE!")
elif percentComplete <= 90:
    print("WARNING!")
elif percentComplete <= 98:
    print("GOOD!")
elif percentComplete <= 100:
    print("GREAT")
elif percentComplete <= 101:
    print("CRITICAL FAILURE!")
print ("Final Time: " + currentTimeString + " Seconds")
print ("Expected Duration: " + str(expectedDuration))
print ("Final Drift: " + msToSeconds + " Seconds")


#TODO: print/write out drift difference to a file.

#TODO: decide if we want to wrap it all in a for loop to test multiple videos


driver.close()
