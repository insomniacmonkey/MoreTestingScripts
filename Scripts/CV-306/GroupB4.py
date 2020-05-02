from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from listA import *
from password import *
from functions import *

ListNumber = "B4"
totalTeams = str(len(listB4))

for teamId in listB4:
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

    #Navigate to school Page
    navToSchool = driver.find_element_by_xpath("//a[contains(@href,'/school/')]")
    navToSchool.click()

    #Check if business unit is elite
    isItAnEliteTeam = driver.find_element_by_class_name("business-unit")
    whatIsIt = isItAnEliteTeam.text
    if(whatIsIt == "Elite"):
        errorState(ListNumber,teamId,"Elite School",totalTeams)

    elif(whatIsIt != "Elite"):
        #Check if they have a sportscode licens
        navToSportsCode = driver.find_element_by_xpath("//a[contains(@href,'/admin/sportscode/licenses/')]")
        navToSportsCode.click()
        time.sleep(1)
        doTheyHaveASportsCodeLicenses = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2][contains(string(), '(this School has no Licenses)')]")
        wellDoThey = doTheyHaveASportsCodeLicenses.text

        if(wellDoThey != "(this School has no Licenses)"):
            errorState(ListNumber,teamId,"has SportsCode Licenses",totalTeams)

        elif(wellDoThey == "(this School has no Licenses)"):
            #TODO remove this before moving on to checking for league exchanges
            passingState(ListNumber,teamId,totalTeams)
        #TODO Check if they have league exchanges
    driver.close()
