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

#Get current Time
currentTime = driver.execute_script("return document.getElementById('player-current-time').value;")
currentTimeString = str(int(float(currentTime)))

#Get expected duration
expectedTime = driver.execute_script("return document.getElementById('player-expected-duration').value;")
expectedTimeString = str(int(float(expectedTime)))


#Write a while loop that checks if current time = duration and continually update the drift ammount.
while (currentTimeString != expectedTimeString):
    currentTime = driver.execute_script("return document.getElementById('player-current-time').value;")
    currentTimeString = str(int(float(currentTime)))

    #Get drift and convert from ms to seconds
    driftTime = driver.execute_script("return document.getElementById('drift').value;")
    msToSeconds = float(driftTime) / 1000

    print ("Current Time: " + currentTimeString + " in Seconds")
    print ("Current Drift: " + str(float(msToSeconds)) + " in Seconds")
    time.sleep(60)

print("Finished!")
print ("Final Time: " + currentTimeString + " in Seconds")
print ("Final Drift: " + str(float(msToSeconds)) + " in Seconds")

#TODO: print/write out drift difference to a file.

#TODO: decide if we want to wrap it all in a for loop to test multiple videos
driver.close()
