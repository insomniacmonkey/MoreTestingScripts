from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from listA import *
from password import *
from functions import *

ListNumber = "A1"
totalTeams = str(len(listA1))

for teamId in listA1:
    ##login
    driver = webdriver.Chrome()
    driver.get(thorenv + str(teamId))
    time.sleep(1)
    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(myEmail)
    inputElement = driver.find_element_by_id("password")
    inputElement.send_keys(password)
    inputElement.submit()
    ##load Admin Page
    driver.get(thorenv + str(teamId))

    #shouldn't be elite
    #shouldn't have sports code licenses
    try:
        #Navigate to school Page
        navToSchool = driver.find_element_by_xpath("//a[contains(@href,'/school/')]")
        navToSchool.click()
        print("Navigated to school page...")

    except:
        errorState(ListNumber,teamId,"Couldn't Navigate to school page",totalTeams)
        driver.close()
        continue

    #Check if business unit is elite
    try:
        isItAnEliteTeam = driver.find_element_by_class_name("business-unit")
        whatIsIt = isItAnEliteTeam.text
        print("Business Unit: " + whatIsIt)
        if(whatIsIt == "Elite"):
            errorState(ListNumber,teamId,"Elite School",totalTeams)
            driver.close()
            continue

        else:
            print("Not an Elite School " + "Business Unit: " + whatIsIt)

    except:
        errorState(ListNumber,teamId,"Couldn't Find Business Unit",totalTeams)
        driver.close()
        continue

    try:
        #Check if they have a sportscode licens
        navToSportsCode = driver.find_element_by_xpath("//a[contains(@href,'/admin/sportscode/licenses/')]")
        navToSportsCode.click()
        time.sleep(1)
        print("Was able to navigate to sports code page...")

    except:
        errorState(ListNumber,teamId,"Couldn't navigate to sports code page",totalTeams)
        driver.close()
        continue

    try:
        doTheyHaveASportsCodeLicenses = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2][contains(string(), '(this School has no Licenses)')]")
        wellDoThey = doTheyHaveASportsCodeLicenses.text

        if(wellDoThey == "(this School has no Licenses)"):
            print("Didn't have sports code licenses")
            passingState(ListNumber,teamId,totalTeams)
            driver.close()
            continue

        else:
            errorState(ListNumber,teamId,"Has SportsCode Licenses",totalTeams)
            driver.close()
            continue


    except:
        print("Made it to the last except")
        errorState(ListNumber,teamId,"something was wrong on sportscode page",totalTeams)
        driver.close()
        continue

    driver.close()
