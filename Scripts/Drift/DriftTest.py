from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from password import *
from urls import *
from csv import writer
import time
import datetime

#Sets the count so we know how many files we run through
count = 0

#Get current Time
def firstTimeCheck():
    time.sleep(1)
    global currentTime
    global currentTimeString
    currentTime = driver.execute_script("return document.getElementById('player-current-time').value;")
    #Makes currentTime resilent if the page hasn't fished loading when it checks for the time. 
    if currentTime == '':
        currentTime = 0
    else:
        currentTime = int(float(currentTime))
    currentTimeString = str(currentTime)

def secondTimeCheck():
    time.sleep(3)
    global currentTimeSecondCheck
    global currentTimeSecondCheckString
    currentTimeSecondCheck = driver.execute_script("return document.getElementById('player-current-time').value;") 
    if currentTimeSecondCheck == '':
        currentTimeSecondCheck = 0
    else:
        currentTimeSecondCheck = int(float(currentTimeSecondCheck))
    currentTimeSecondCheckString = str(currentTimeSecondCheck)

#TODO Change this to an output that makes sense for capturing how bad the drift is, what file was run, etc.
def outputFinalResults():
    global count
    print("Finished Run Number: " + str(count))
    print ("Final Time: " + currentTimeString + " Seconds")
    print ("Expected Duration: " + str(expectedDuration))
    print ("Final Drift: " + totalDriftAmmount + " Seconds")
    print ("------------------------------")
    
    #Output We are saving
    row_contents = [str(now),videoSrc[0],totalDriftAmmount,currentTimeString,str(expectedDuration),videoSrc[1],videoSrc[2],videoSrc[3]]
    
    # Append a list as new line to an old csv file
    append_list_as_row('DriftOutput.csv', row_contents)

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

for videoSrc in url:
    driver = webdriver.Chrome()
    driver.get(thorenv)
    time.sleep(1)
    count +=1
    #Load stream info
    inputElement = driver.find_element_by_xpath("//*[@id='player-stream-src']")
    inputElement.clear()
    inputElement.send_keys(videoSrc[0])
    submitButton = driver.find_element_by_id("player-stream-load").click()
    time.sleep(1)

    #Select 2x speed
    setTheSpeed = driver.find_element_by_xpath("//*[@id='player-playbackrate']/option[5]").click()

    #initialzing values so the first while loop runs
    currentTime = 0
    currentTimeString = ""
    currentTimeSecondCheck = 0
    currentTimeSecondCheckString = "2"
    driftTime = 0
    totalDriftAmmount = 0
    expectedDuration = 0

    #Continue to loop through until the video stops playing. 
    #TODO Make this more redundent incase the video buffers/freezes
    while currentTimeString != currentTimeSecondCheckString:
        #get the duration
        firstTimeCheck()
        secondTimeCheck()
        #Get drift and convert from ms to seconds
        driftTime = driver.execute_script("return document.getElementById('drift').value;")
        if driftTime == '':
            driftTime = 0
        else:
            driftTime = float(driftTime)
        totalDriftAmmount = str(round(float(driftTime / 1000),2))
        expectedDuration = driver.execute_script("return document.getElementById('player-expected-duration').value;")
        #Makes Expected duration resilent if the page hasn't fished loading when it checks for the time. 
        if expectedDuration == '':
            expectedDuration = 0
        else:
            expectedDuration = int(float(expectedDuration))
        percentComplete = round(float(currentTimeSecondCheck / expectedDuration),2) * 100
        print ("Current Run Number: " + str(count))
        print ("Current Time: " + currentTimeString + " Seconds")
        print ("Percent Complete: " + str(percentComplete) + "%")
        print ("Current Drift: " + totalDriftAmmount + "  Seconds")
        print ("------------------------------")
        time.sleep(5)
    now = datetime.datetime.now()
    outputFinalResults()
    driver.close()
