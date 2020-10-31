import time
from datetime import datetime
from selenium import webdriver
from env import *
from selenium.webdriver.common.keys import Keys
from csv import writer
from sourcevideo import *
import os

def deleteOldFile():
    #Delete the DriftOutput.csv if it exist
    if os.path.exists("DriftOutput.csv"):
        print("Deleting old DriftOutput.csv file")
        os.remove("DriftOutput.csv")

def createDriftOutputCSV(DriftOutputCSV):
    with open(DriftOutputCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        headerRow = ["Time at Run","Drift In Seconds","P/F","Final Play Time","P/F","Biggest Drift","P/F", "Name of Video", "Admin Link", "Type","Manifest URL"]
        csv_writer.writerow(headerRow)

def firstTimeCheck(driver):
    currentTime = int(float(driver.execute_script("return document.getElementById('player-current-time').value;")))
    if(currentTime == ""):
        currentTime = 0
    currentTimeString = str(currentTime)
    return currentTimeString

def loadStream(driver,manifestFile,count):
    inputElement = driver.find_element_by_xpath("//*[@id='player-stream-src']")
    inputElement.clear()
    inputElement.send_keys(manifestFile[0])
    submitButton = driver.find_element_by_id("player-stream-load").click()
    time.sleep(3)
    #Select 2x speed
    setTheSpeed = driver.find_element_by_xpath("//*[@id='player-playbackrate']/option[5]").click()
    print ("Starting Video " + str(count) + " out of " + str(len(videoData)))

def printCurrentResults(driver,currentTimeString,currentTimeSecondCheckString):
    biggestDriftTime = 0
    while currentTimeString != currentTimeSecondCheckString:
        currentTimeString = firstTimeCheck(driver)
        time.sleep(2)
        currentTimeSecondCheckString = firstTimeCheck(driver)
        expectedDuration = int(float(driver.execute_script("return document.getElementById('player-expected-duration').value;")))
        driftTime = float(driver.execute_script("return document.getElementById('drift').value;"))
        if (driftTime >= biggestDriftTime):
            biggestDriftTime = driftTime
        currentDriftInSeconds = str(round(float(driftTime / 1000),2))
        biggestDriftInSeconds = round(float(biggestDriftTime / 1000),2)
        time.sleep(5)
    return biggestDriftInSeconds
    
def generateFinalResults(driver,manifestFile,biggestDriftInSeconds,count):
    currentTimeString = firstTimeCheck(driver)
    expectedDuration = int(float(driver.execute_script("return document.getElementById('player-expected-duration').value;")))
    driftTime = float(driver.execute_script("return document.getElementById('drift').value;"))
    currentDriftInSeconds = round(float(driftTime / 1000),2)
    finalTime = str(currentTimeString + "/" + str(expectedDuration))
    print ("Video Number: " + str(count) + " out of " + str(len(videoData)))
    print ("Final Time: " + finalTime + " seconds ")
    print ("Final Drift: " + str(currentDriftInSeconds) + " seconds")
    print ("Biggest Drift: " + str(biggestDriftInSeconds) + " seconds")
    print ("------------------------------")
    #logic that sets pass or fail
    if(currentTimeString != str(expectedDuration)):
        finalTimeStatus = "Fail"
    else:
        finalTimeStatus = "Pass"
    if(currentDriftInSeconds >= 1.0):
         driftStatus = "Fail"
    else:
        driftStatus = "Pass"
    if(biggestDriftInSeconds >= 1.0):
        maxDriftStatus = "Fail"
    else:
        maxDriftStatus = "Pass"
    timeAtFinish = datetime.now()
    return [str(timeAtFinish),currentDriftInSeconds,driftStatus,finalTime,finalTimeStatus,str(biggestDriftInSeconds),maxDriftStatus,manifestFile[1],manifestFile[2],manifestFile[3],manifestFile[0]]

def append_list_as_row(DriftOutputCSV, list_of_elem):
    # Open file in append mode
    with open(DriftOutputCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
