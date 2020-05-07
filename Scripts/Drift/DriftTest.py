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
#TODO: Select 2x speed
setTheSpeed = driver.find_element_by_xpath("//*[@id='player-playbackrate']/option[5]").click()

#TODO: Get current Time
currentTime = driver.find_element_by_id("player-current-time")
currentTime.get_parameter('Value')
print(str(currentTime))
#TODO: GET EXPECTED DURATION

#TODO: GET drift and convert from ms to seconds

#TODO: write a while loop that checks if current time = duration and continually update the drift ammount.

#TODO: print/write out drift difference to a file. 

#TODO: decide if we want to wrap it all in a for loop to test multiple videos
driver.close()
