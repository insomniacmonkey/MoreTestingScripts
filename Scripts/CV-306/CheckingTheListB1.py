from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from listB import *
from password import *


passed = 0
errorCount = 0
badTeamIds = ""
MTL = "Checking The List "
txt = ".txt"
newLine = "\n"
now = datetime.datetime.now()

def append_new_line(file_name, text_to_append):
    with open(file_name, "w") as file_object:
        file_object.writelines(text_to_append)



ListNumber = "B1"
totalNumber = len(listB1)
for i in listB1:
    true = "True"
    runningListName = (MTL + ListNumber + newLine)
    totalRan = passed + errorCount
    currentTime = ("Time at Run: " + str(now) + newLine)
    itPassed = ("PASSED! Team ID = " + str(i) + newLine)
    itFailed = ("FAILED! Team ID = " + str(i) + newLine)
    totalPassedCount = ("Passed Count " + str(passed) + newLine)
    totalErrorCount =("Error Count " +  str(errorCount) + newLine)
    failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
    progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
    ##login
    driver = webdriver.Chrome()
    driver.get(thorenv + str(i))
    time.sleep(1)
    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(myEmail)
    inputElement = driver.find_element_by_id("password")
    inputElement.send_keys(password)
    inputElement.submit()
    ##load Admin Page
    driver.get(thorenv + str(i))
    time.sleep(1)

    ## Check for elite toggle = true
    eliteToggle = driver.find_element_by_xpath("//*[@id='isEliteTeam']").is_selected()
    if (str(eliteToggle) == true):
        errorCount = errorCount + 1
        badTeamIds = badTeamIds + ", " +  str(i) + " eliteToggleTrue"
        totalRan = passed + errorCount
        totalErrorCount =("Error Count " +  str(errorCount) + newLine)
        progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
        failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
        textToWrite = [
        runningListName,
        currentTime,
        itFailed,
        totalPassedCount,
        totalErrorCount,
        failedTeamIds,
        progress]
        append_new_line((MTL + ListNumber + txt),textToWrite)
        print (runningListName)
        print (currentTime)
        print (itFailed)
        print (totalPassedCount)
        print (totalErrorCount)
        print (failedTeamIds)
        print (progress)
        print ("something went wrong")

    elif (str(eliteToggle) != true):
        ##Load Team Priv Page
        driver.get(teamPrivs + str(i))

        ##Check for League Exchange toggle
        exchangesTrue = driver.find_element_by_xpath("//*[@id='chk4']").is_selected()

        if (str(exchangesTrue) != true):
            errorCount = errorCount + 1
            badTeamIds = badTeamIds + ", " +  str(i) + " exchangesFalse"
            totalRan = passed + errorCount
            totalErrorCount =("Error Count " +  str(errorCount) + newLine)
            progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
            failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
            textToWrite = [
            runningListName,
            currentTime,
            itFailed,
            totalPassedCount,
            totalErrorCount,
            failedTeamIds,
            progress]
            append_new_line((MTL + ListNumber + txt),textToWrite)
            print (runningListName)
            print (currentTime)
            print (itFailed)
            print (totalPassedCount)
            print (totalErrorCount)
            print (failedTeamIds)
            print (progress)
            print ("something went wrong")

        elif (str(exchangesTrue) == true):
            ##Check for SportsCode toggles
            DownloadHudlTaggingDataAsSportscodeXml = driver.find_element_by_xpath("//*[@id='chk574']").is_selected()
            HudlSportscodeVideoDownload = driver.find_element_by_xpath("//*[@id='chk631']").is_selected()
            SportscodeBridge = driver.find_element_by_xpath("//*[@id='chk377']").is_selected()
            SportscodeDownloadXml = driver.find_element_by_xpath("//*[@id='chk517']").is_selected()
            SportscodeRegistrationManagement = driver.find_element_by_xpath("//*[@id='chk538']").is_selected()
            SportscodeUploadToPlaylist = driver.find_element_by_xpath("//*[@id='chk472']").is_selected()
            SportscodeVideoSPA = driver.find_element_by_xpath("//*[@id='chk455']").is_selected()
            SportscodeVideoSpaBeta = driver.find_element_by_xpath("//*[@id='chk478']").is_selected()
            V3MultiAngleSportscodeZips = driver.find_element_by_xpath("//*[@id='chk556']").is_selected()

            if (str(DownloadHudlTaggingDataAsSportscodeXml) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " DownloadHudlTaggingDataAsSportscodeXml"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")

            elif (str(HudlSportscodeVideoDownload) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " HudlSportscodeVideoDownload"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")

            elif (str(SportscodeBridge) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " SportscodeBridge"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")

            elif (str(SportscodeDownloadXml) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " SportscodeDownloadXml"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")


            elif (str(SportscodeRegistrationManagement) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " SportscodeRegistrationManagement"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")

            elif (str(SportscodeUploadToPlaylist) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " SportscodeUploadToPlaylist"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")

            elif (str(SportscodeVideoSPA) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " SportscodeVideoSPA"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")

            elif (str(SportscodeVideoSpaBeta) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " SportscodeVideoSpaBeta"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")

            elif (str(V3MultiAngleSportscodeZips) == true):
                errorCount = errorCount + 1
                badTeamIds = badTeamIds + ", " +  str(i) + " V3MultiAngleSportscodeZips"
                totalRan = passed + errorCount
                totalErrorCount =("Error Count " +  str(errorCount) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)
                failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
                textToWrite = [
                runningListName,
                currentTime,
                itFailed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)
                print (runningListName)
                print (currentTime)
                print (itFailed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("something went wrong")


            else:
                passed = passed + 1
                totalRan = passed + errorCount
                totalPassedCount = ("Passed Count " + str(passed) + newLine)
                progress = ("Completed: " + str(totalRan) + "/" + str(totalNumber) + newLine)

                textToWrite = [
                runningListName,
                currentTime,
                itPassed,
                totalPassedCount,
                totalErrorCount,
                failedTeamIds,
                progress]
                append_new_line((MTL + ListNumber + txt),textToWrite)

                print (runningListName)
                print (currentTime)
                print (itPassed)
                print (totalPassedCount)
                print (totalErrorCount)
                print (failedTeamIds)
                print (progress)
                print ("Passed")


    driver.close()
