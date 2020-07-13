from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from password import *
from PIL import Image
import pytesseract
import time
import datetime


# ==============
# VARIABLES
# ==============


loginURL = "https://master.thorhudl.com/login"
videoSpaURL = "https://master.thorhudl.com/watch/video/VmlkZW81ZjBjNzY3MTdjMGE1YjYxY2NiOTY2NWE=/organizer"
windows = r'C:/Users/chanse.strode/Documents/tesseract/tesseract'
emailField = driver.find_element_by_id("email")
passwordField = driver.find_element_by_id("password")
driver = webdriver.Chrome()
pauseButton = driver.find_element_by_xpath("//*[@data-qa-id='vi-controls-playpause']")
playTime = driver.find_element_by_xpath("//*[@data-qa-id='player-time-label']")
theImage = Image.open("/Users/chase.grizzle/Documents/github/MoreTestingScripts/Scripts/VideoPlayer/screenshot.png") 
width, height = theImage.size
windowsLeft = 0
windowsTop = 100
windowRight = width
windowsBottom = height


# ==============
# GIVENS
# ==============

@given('I log into Hudl')
def login_with_hudl(context):
    driver.set_window_position(0, 0)
    driver.set_window_size(1200, 700)
    driver.get(loginURL)
    time.sleep(1)
    emailField.send_keys(myEmail)
    passwordField.send_keys(password)
    passwordField.submit()


# ==============
# WHENS
# ==============


@when('I load the video in the VSPA')
def load_video_in_vspa(context):
    ##Load Video Spa Page
    driver.get(videoSpaURL)
    #let the player play for 15 seconds. This has to be a number that doesn't have a "0" in it due to image text conversion below. 
    time.sleep(15)


@when('I pause the video in the VSPA')
def pause_video_in_vspa(context):
    #pause player
    pauseButton.click()


@when('I get the play time in the VSPA')
def get_play_time_in_vspa(context):
    #get play time
    getPausedRunTime = playTime.text.split("/")
    getJustTheSeconds = getPausedRunTime[0].split(":")
    currentPlayTime = int(getJustTheSeconds[1])
    print("Playhead Time: " + str(currentPlayTime))


# ==============
# THENS
# ==============


@then('I take a screenshot of the page')
def take_screenshot_of_page(context):
    #grab Screen shot of the vspa page
    driver.get_screenshot_as_file("screenshot.png")
    print(width,height)

@then('I set the points in pixels')
def set_points_in_pixels(context):
    # Setting the points in pixels for cropped image. If we force the browser size we can use this approach.
    #left = 630
    #top = 300
    #right = 800
    #bottom = 700


@then('I crop the image')
def crop_the_image(context):
    # Cropped image of above dimension
    # (It will not change orginal image)
    cropTheImage = theImage.crop((left, top, right, bottom))
    # Shows the image in image viewer
    cropTheImage.save("croppedImage.png")
    # navigate to pytesseract exe location
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

@then('I convert the image to text')
def convert_image_to_text(context):
    #get the image and convert it to text
    readTheImageTime = pytesseract.image_to_string("/Users/chase.grizzle/Documents/github/MoreTestingScripts/Scripts/VideoPlayer/croppedImage.png")
    print(str(readTheImageTime))
    convertedImageTime = int(float(readTheImageTime))
    print("Displayed Time: " + str(convertedImageTime))

@then('I verify the video played back correctly')
def verify_playback(context):
    #check to see if the player has played at least 10 seconds
    if currentPlayTime >= 10:
        print("Played at least 10 seconds!")

        playTimeDifference = currentPlayTime - convertedImageTime
        print("Difference in Seconds: " + str(playTimeDifference))
        #Check to see if play head time and whats on the screen is within 1 second
        if abs(playTimeDifference) >= 2:
            print("ERROR: The difference between the playhead time and displayed time is greater than 1 second:")
            print("Playhead Time: " + str(currentPlayTime))
            print("Displayed Time: " + str(convertedImageTime))
        else:
            print("SUCCESS! TEST PASSED!")

    else:
        print("ERROR: The video did not play more than 10 seconds!")

    driver.close()
