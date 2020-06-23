import requests
import json
import boto3
import botocore.exceptions
import time
import os
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from password import *
from PIL import Image 
from os import listdir
from os.path import isfile, join
from pathlib import Path
from configs import *
from datetime import datetime

#base vars
uploadCount = 0
sourceVideo = "https://vtemp.hudl.com/thor/video-temp-10d/47313/275183/1f8/5ef0d7a3c2e10516302e71f8/5ef0d7a3c2e10516302e71f8.mp4"
authenticateApi =  hudlUrl + "/api/v2/authenticate"
openPublishSessionApi = hudlUrl + '/api/v3/record/teams/' + uploadTeamId + '/publishSessions/openSession'
newCredentialsApi = ""
sendFileCompleteApi = ""
publishSessionCompleteApi = ""
checkPublishSessionStatusApi = ""
authToken = ""
publishSessionId = ""
videoId = ""
uploadSegments = {}
sourceFileId = ""
target_bucket = ""
target_key = ""
authHeader = {}
emptyRequest = {}
VIDEO_READY_STATUS = 64

#Set chromes setting to autodownload
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": r"C:\Users\chanse.strode\Desktop\1000", 
    "download.directory_upgrade": "True",
    "download.prompt_for_download": "False",
    "safebrowsing.enabled": "False"
    }
options.add_experimental_option("prefs", prefs)

while uploadCount <= 10:
    ##login
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get(loginURL)
    time.sleep(1)
    emailField = driver.find_element_by_id("email")
    emailField.send_keys(myEmail)
    passwordField = driver.find_element_by_id("password")
    passwordField.send_keys(password)
    passwordField.submit()

    #download the source file created mp4
    driver.get(sourceVideo)
    #get and rename latest source file
    srcFolderPath = "C:/Users/chanse.strode/Desktop/1000"
    eachImageName = [myfiles for myfiles in listdir(srcFolderPath) if isfile(join(srcFolderPath, myfiles))]
    while eachImageName == []:
        print("Waiting 15 seconds for the video to upload...")
        time.sleep(15)
        eachImageName = [myfiles for myfiles in listdir(srcFolderPath) if isfile(join(srcFolderPath, myfiles))]

    #rename the file to the lastest upload
    filePath1 = "C:\\Users\\chanse.strode\\Desktop\\1000\\" + str(eachImageName[0])
    filePath2 = "C:\\Users\\chanse.strode\\Desktop\\1000\\" + str(uploadCount) + ".mp4"
    os.rename(filePath1, filePath2)
    print("Renamed file...")

    driver.close()

    # This authenticates the user in hudl and pulls out the necessary auth tokens for that user
    postData = {'username': username,'password':password}
    postAuthRequest = requests.post(authenticateApi, data = postData)
    authResponse = dict(postAuthRequest.json())
    authToken = authResponse.get("token")
    authHeader = {'Content-Type': 'application/json', 'Accept': 'application/json', 'hudl-authtoken': authToken}
    print("Authed...")

    # This opens a publish session  for the user and stores the correct variables to use in future steps
    params = {
        'videoName': '1000 Video Test- Upload - ' + str(uploadCount),
        'source': 'V3WebUploader',
        'files': [{
        'id': '1',
        'name': 'Upload-' + str(uploadCount) + '.mp4',
        'source': 'Hudl',
        'sizeBytes': 5022174,
        'selectedOrder': 0,
        'mimeType': 'video/mp4',
        'sourceDateModified': '2020-04-29T04:32:31.041Z'
        }],
        'shouldDiscardAudio': 'false'
    }
    openPublishSessionRequest = requests.post(openPublishSessionApi, data = json.dumps(params), headers = authHeader)
    openSessionResponse = openPublishSessionRequest.json()
    publishSessionId = openSessionResponse.get("uploadId")
    videoId = openSessionResponse.get("newEvent",{}).get("eventId")
    uploadSegments = json.dumps(openSessionResponse.get("newEvent",{}).get("videoSegments"))
    converToArray = json.loads(uploadSegments)
    sourceFileId = str(converToArray[0]["segmentId"])
    target_bucket = str(converToArray[0]["bucket"])
    target_key = str(converToArray[0]["key"])
    newCredentialsApi = hudlUrl + '/api/v3/record/teams/' + uploadTeamId + '/publishSessions/' + publishSessionId + '/credentials'
    sendFileCompleteApi = hudlUrl + '/api/v3/record/teams/' + uploadTeamId + '/publishSessions/' + publishSessionId + '/files/' + sourceFileId + '/complete'
    publishSessionCompleteApi = hudlUrl + '/api/v3/record/teams/'+ uploadTeamId + '/publishSessions/' + publishSessionId + '/complete'
    checkPublishSessionStatusApi = hudlUrl + '/api/v3/record/teams/' + uploadTeamId + '/publishSessions/' + publishSessionId
    checkAdminInfoApi = hudlUrl + '/admin/record/videos/' + videoId + '/getVideoData'
    print("Opened Publish Session...")

    # This copies the file on S3 into the test bucket
    getNewCredentials = requests.post(newCredentialsApi, data = emptyRequest, headers = authHeader)
    # puts publishSessionId,sourceFileId,source_file_bucket,source_file_key,target_bucket,target_key, uploadCredentials.secretKey, uploadCredentials.accessKey
    s3 = boto3.client(
        's3',
        region_name = 'us-east-1',
        aws_access_key_id =  ACCESS_KEY,
        aws_secret_access_key = SECRET_KEY
        )
    copy_source = {
        'Bucket': source_file_bucket,
        'Key': source_file_key
    }

    sourceFile = filePath2

    try:
        s3.upload_file(
            Bucket = target_bucket,
            Filename = sourceFile,
            Key = target_key
        )
    except botocore.exceptions.ClientError as e:
        raise Exception(e)
    sendFileCompleteRequest = requests.post(sendFileCompleteApi, data = emptyRequest, headers = authHeader)
    print("Uploaded file...")


    # This finishes the publish session for the team that the file was uploaded to 
    response = requests.post(publishSessionCompleteApi, data = emptyRequest, headers = authHeader)
    print("Closed Publish Session...")

    # This waits for the video to become "Video Ready" on the video admin page
    videoIsReady = False
    maxRetries = 0
    # waits 5 mins for the stream to become playable
    while (videoIsReady == False and maxRetries <= 30):
        maxRetries = maxRetries + 1
        publishSessionRequest = requests.get(checkPublishSessionStatusApi, headers = authHeader)
        publishSessionResponse = publishSessionRequest.json()
        if publishSessionResponse.get("mediaStreamStatus") & VIDEO_READY_STATUS == VIDEO_READY_STATUS:
            videoIsReady = True
            break
        time.sleep(10)
        print("Waiting for video ready...")

    if not videoIsReady:
        print("Video did not become ready in time.")
    print("Video is Ready...")

    #check to see if the download is ready
    downloadIsReady = False
    maxDownloadRetries = 0
    while (downloadIsReady == False and maxDownloadRetries <=30):
        maxDownloadRetries = maxDownloadRetries + 1
        adminGetAllInfoRequest = requests.get(checkAdminInfoApi, headers = authHeader)
        adminGetAllInfoResponse = adminGetAllInfoRequest.json()
        getStreaminfo = json.dumps(adminGetAllInfoResponse.get("video",{}).get("streams"))
        converToArray = json.loads(getStreaminfo)
        isDownloadMP4Null = converToArray[0]["downloadMp4"]
        if isDownloadMP4Null == None:
            isDownloadMP4Null = converToArray[0]["downloadMp4"]
            time.sleep(10)
        else:
            getDownloadMp4Status = str(converToArray[0]["downloadMp4"].get("status"))
            if getDownloadMp4Status == "Ready":
                sourceVideo = str(converToArray[0]["downloadMp4"].get("downloadUrl"))
                if sourceVideo == None:
                    sourceVideo = str(converToArray[0]["downloadMp4"].get("downloadUrl"))
                    print("Waiting for Download Mp4 URL")
                    time.sleep(10)
                else:
                    sourceVideo = str(converToArray[0]["downloadMp4"].get("downloadUrl"))
                    print(sourceVideo)
                    downloadIsReady = True
                    break
            else:
                time.sleep(10)
                print("Waiting for Download Mp4 Ready Status")
        print("Waiting for Download Mp4 Ready Status")
    print("Download MP4 URL Is Ready...")

    #move the file to a new folder
    filePath3 = "C:\\Users\\chanse.strode\\Desktop\\Moved1000\\Moved" + str(uploadCount) + ".mp4"
    os.rename(filePath2, filePath3)
    print("Moved file to a new folder...")
    uploadCount = uploadCount + 1
    print("--------------------------------------")
    print("Starting Next Upload...")

print("End Test")