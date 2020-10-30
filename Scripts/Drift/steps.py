import time
from selenium import webdriver
from env import *
from selenium.webdriver.common.keys import Keys



#Get current Time
def firstTimeCheck(driver):
    currentTime = int(float(driver.execute_script("return document.getElementById('player-current-time').value;")))
    currentTimeString = str(currentTime)
    return currentTimeString

def loadStream(driver,videoSrc):
    inputElement = driver.find_element_by_xpath("//*[@id='player-stream-src']")
    inputElement.clear()
    inputElement.send_keys(videoSrc)
    submitButton = driver.find_element_by_id("player-stream-load").click()
    time.sleep(3)
    #Select 2x speed
    setTheSpeed = driver.find_element_by_xpath("//*[@id='player-playbackrate']/option[5]").click()

def printCurrentResults(driver,currentTimeString,currentTimeSecondCheckString,count):
    while currentTimeString != currentTimeSecondCheckString:
        currentTimeString = firstTimeCheck(driver)
        time.sleep(2)
        currentTimeSecondCheckString = firstTimeCheck(driver)
        expectedDuration = int(float(driver.execute_script("return document.getElementById('player-expected-duration').value;")))
        driftTime = float(driver.execute_script("return document.getElementById('drift').value;"))
        msToSeconds = str(round(float(driftTime / 1000),2))
        percentComplete = round(float(int(currentTimeString) / expectedDuration),2) * 100
        print ("Current Run Number: " + str(count))
        print ("Current Time: " + currentTimeString + " Seconds")
        print ("Percent Complete: " + str(percentComplete) + "%")
        print ("Current Drift: " + msToSeconds + "  Seconds")
        print ("------------------------------")
        time.sleep(5)
    
    

def printFinalResults(driver,currentTimeString):
    expectedDuration = int(float(driver.execute_script("return document.getElementById('player-expected-duration').value;")))
    driftTime = float(driver.execute_script("return document.getElementById('drift').value;"))
    msToSeconds = str(round(float(driftTime / 1000),2))
    percentComplete = round(float(int(currentTimeString) / expectedDuration),2) * 100
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
    print ("------------------------------")
