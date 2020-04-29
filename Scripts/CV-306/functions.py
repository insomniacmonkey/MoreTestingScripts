import time
import datetime

passed = 0
errorCount = 0
badTeamIds = ""
MTL = "Checking The List "
txt = ".txt"
newLine = "\n"
now = datetime.datetime.now()
true = "True"
totalRan = passed + errorCount
currentTime = ("Time at Run: " + str(now) + newLine)

def append_new_line(file_name, text_to_append):
    with open(file_name, "w") as file_object:
        file_object.writelines(text_to_append)

def errorState(ListNumber,teamId,theToggle,totalTeams):
    global passed
    global errorCount
    global badTeamIds
    global MTL
    global txt
    global newLine
    global now
    global true
    global runningListName
    global currentTime
    global totalRan

    runningListName = (MTL + ListNumber + newLine)
    #Increase failed count, total ran so far, total passed, current progress, and the list of failed ids.
    itFailed = ("FAILED! Team ID = " + str(teamId) + newLine)
    errorCount = errorCount + 1
    badTeamIds = badTeamIds + ", " +  teamId + " " + theToggle
    totalPassedCount = ("Passed Count " + str(passed) + newLine)
    totalErrorCount =("Error Count " +  str(errorCount) + newLine)
    failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
    progress = ("Completed: " + str(totalRan) + "/" + totalTeams + newLine)
    totalRan = passed + errorCount
    #Make sure the current list is set for the save file
    runningListName = (MTL + ListNumber + newLine)
    #Set what is being written in the file
    textToWrite = [
    runningListName,
    currentTime,
    itFailed,
    totalPassedCount,
    totalErrorCount,
    failedTeamIds,
    progress]
    #Write to the file
    append_new_line((MTL + ListNumber + txt),textToWrite)
    #Print to the console
    print (runningListName)
    print (currentTime)
    print (itFailed)
    print (totalPassedCount)
    print (totalErrorCount)
    print (failedTeamIds)
    print (progress)
    print ("Something went wrong...")
    return


def passingState(ListNumber,teamId,totalTeams):
    global passed
    global errorCount
    global badTeamIds
    global MTL
    global txt
    global newLine
    global now
    global true
    global runningListName
    global currentTime
    global totalRan

    #Increase pass count, total ran so far, total passed, current progress, and the list of failed ids.
    itPassed = ("PASSED! Team ID = " + str(teamId) + newLine)
    passed = passed + 1
    totalRan = passed + errorCount
    totalPassedCount = ("Passed Count " + str(passed) + newLine)
    totalErrorCount =("Error Count " +  str(errorCount) + newLine)
    progress = ("Completed: " + str(totalRan) + "/" + totalTeams + newLine)
    failedTeamIds =("Failed Team Id's" + str(badTeamIds) + newLine)
    #Make sure the current list is set for the save file
    runningListName = (MTL + ListNumber + newLine)
    #Set what is being written in the file
    textToWrite = [
    runningListName,
    currentTime,
    itPassed,
    totalPassedCount,
    totalErrorCount,
    failedTeamIds,
    progress]
    #Write to the file
    append_new_line((MTL + ListNumber + txt),textToWrite)
    #Print to the console
    print (runningListName)
    print (currentTime)
    print (itPassed)
    print (totalPassedCount)
    print (totalErrorCount)
    print (failedTeamIds)
    print (progress)
    print ("Passed")
    return
