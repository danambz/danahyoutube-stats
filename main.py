import requests
import json
from playsound import playsound
import time
import os

channelID = "UCfL6BmHxOSMIedRmHe1gobA"

apiKey = "AIzaSyDT999IkC1QAwonw4AqRjGnSLk-tlP9qno"


def getSubscriberCount():
    rawData = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channelID}&key={apiKey}")

    decodedData = json.loads(rawData.content)
    
    # extracting subscriberCount from data
    subsciberCount = decodedData["items"][0]["statistics"]["subscriberCount"]
    return subsciberCount


oldSubscriberCount=getSubscriberCount()

print(oldSubscriberCount)

def playSound():
    #playsound('beep.mp3')
    os.system('mpg123 -q beep.mp3')

    
while True:
    count = getSubscriberCount()
    if count > oldSubscriberCount:
        playSound()
        oldSubscriberCount = count
    print(count)
    time.sleep(10)
    