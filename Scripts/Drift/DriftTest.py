from env import *
from urls import *
from steps import *
import datetime

#Sets the count so we know how many files we run through
global count
count = 0

for videoSrc in url:
    driver = webdriver.Chrome()
    driver.get(thorenv)
    driver.set_window_size(1024, 768)
    time.sleep(1)
    count +=1
    #Load stream info
    loadStream(driver,videoSrc)

    #initialzing values so the first while loop runs
    driftTime = 0
    msToSeconds = 0
    
    currentTimeString = firstTimeCheck(driver)
    time.sleep(2)
    currentTimeSecondCheckString = firstTimeCheck(driver)

    
    #Get drift and convert from ms to seconds
    printCurrentResults(driver,currentTimeString,currentTimeSecondCheckString,count)

    #log a message depending on playback completion 
    printFinalResults(driver,currentTimeString)
    #TODO (Add ammount of drift compared to total video length)
    driver.close()
