from env import *
from sourcevideo import *
from steps import *
import datetime

#Sets the count so we know how many files we run through
global count
count = 0
DriftOutputCSV = "DriftOutput.csv"
deleteOldFile()
createDriftOutputCSV(DriftOutputCSV)
for manifestFile in videoData:
    driver = webdriver.Chrome()
    driver.get(thorenv)
    driver.set_window_size(1024, 768)
    time.sleep(1)
    count +=1
    #Load stream info
    loadStream(driver,manifestFile,count)
    #initialzing values so the first while loop runs
    driftTime = 0
    msToSeconds = 0
    #Do first time check
    currentTimeString = firstTimeCheck(driver)
    time.sleep(2)
    currentTimeSecondCheckString = firstTimeCheck(driver)
    #Get drift and convert from ms to seconds
    biggestDriftInSeconds = printCurrentResults(driver,currentTimeString,currentTimeSecondCheckString)
    #Write output to csv
    list_of_elem = generateFinalResults(driver,manifestFile,biggestDriftInSeconds,count)
    append_list_as_row(DriftOutputCSV, list_of_elem)
    driver.close()
    