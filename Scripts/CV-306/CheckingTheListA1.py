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
    time.sleep(1)


    ## Check for elite toggle = true
    eliteToggle = driver.find_element_by_xpath("//*[@id='isEliteTeam']").is_selected()
    if (str(eliteToggle) == true):
        errorState(ListNumber,str(teamId),"EliteToggleIsOn",totalTeams)

    elif (str(eliteToggle) != true):
        ##Load Team Priv Page
        driver.get(teamPrivs + str(teamId))

        ##Check for League Exchange toggle
        exchangesTrue = driver.find_element_by_xpath("//*[@id='chk4']").is_selected()

        if (str(exchangesTrue) == true):
            errorState(ListNumber,str(teamId),"ExchangesIsOn",totalTeams)


        elif (str(exchangesTrue) != true):
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
                errorState(ListNumber,str(teamId),"DownloadHudlTaggingDataAsSportscodeXml",totalTeams)

            elif (str(HudlSportscodeVideoDownload) == true):
                errorState(ListNumber,str(teamId),"HudlSportscodeVideoDownload",totalTeams)

            elif (str(SportscodeBridge) == true):
                errorState(ListNumber,str(teamId),"SportscodeBridge",totalTeams)

            elif (str(SportscodeDownloadXml) == true):
                errorState(ListNumber,str(teamId),"SportscodeDownloadXml",totalTeams)


            elif (str(SportscodeRegistrationManagement) == true):
                errorState(ListNumber,str(teamId),"SportscodeRegistrationManagement",totalTeams)

            elif (str(SportscodeUploadToPlaylist) == true):
                errorState(ListNumber,str(teamId),"SportscodeUploadToPlaylist",totalTeams)

            elif (str(SportscodeVideoSPA) == true):
                errorState(ListNumber,str(teamId),"SportscodeVideoSPA",totalTeams)

            elif (str(SportscodeVideoSpaBeta) == true):
                errorState(ListNumber,str(teamId),"SportscodeVideoSpaBeta",totalTeams)

            elif (str(V3MultiAngleSportscodeZips) == true):
                errorState(ListNumber,str(teamId),"V3MultiAngleSportscodeZips",totalTeams)


            else:
                passingState(ListNumber,str(teamId),totalTeams)

    driver.close()
