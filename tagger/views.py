from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.staticfiles.views import serve
from django.http import JsonResponse
import json
import discogs_client
import re
from pprint import pprint
import spotipy
import spotipy.util as util
import random
from datetime import datetime
import datetime

from django.http import JsonResponse

from urllib.parse import unquote

def index(request):
    #template = loader.get_template("tagger/index.html")
    #return HttpResponse(template.render())

    context = {'pageName': "tagger.site", 'icon':'https://cdn4.iconfinder.com/data/icons/48-bubbles/48/06.Tags-512.png' }
    return render(request, 'tagger/index.html', context)

def discogsURL(request):
    print("discogsURL()")
    releaseId = str(request)[:-2]
    releaseId = releaseId[releaseId.index('&data=')+6:]
    print("releaseId = ", releaseId)
    
    #print('path = ', request.path)
    #print('body = ', request.body)
    #print('str body = ', str(request.body))
    #print('data = ', request.body.json())
    #print("request.POST['text'] = ", request.text)

    #body = request.body
    #parse releaseId from post request, convert to string
    #body = body.decode('utf-8')
    #print(' body = ', body)
    
    #indexOfReleaseId = body.index("&data=")
    #releaseId = request.body[indexOfReleaseId+6:]
    #releaseId = releaseId.decode("utf-8")
    
    print("releaseId = ", releaseId)
    #generate tags for this releaseId
    data = generateTracklist(releaseId)
    print("taggerpy() final data = ")
    print(data)
    #return the tags
    
    response_data = {}
    response_data['tracklist'] = data
    #response_data['tracklist'] = 'test'

    #data = "temp popularify_py() Return Data"
    return HttpResponse(json.dumps(response_data))


def generateTracklist(releaseID):
    #connect to discogs
    d = discogs_client.Client('ExampleApplication/0.1', user_token="WPXDcCQCrgWSpjsOFANeRZMOPpopFzObQdQIzerO")
    #get release info
    release = d.release(releaseID)
    print(dir(release))
    #add release tracklist info to array
    everyTrackHasDuration = True
    tracklistArr = []
    count = 0
    if hasattr(release, 'tracklist'):
        for track in release.tracklist:
            if hasattr(track, 'duration') and track.duration != '':
                print(track.title, ' ', track.duration)
                trackDurationMinutes = track.duration
                
                #convert time to seconds
                chunks = map(int, trackDurationMinutes.split(':')[::-1])
                trackDurationSeconds = sum(chunk*60**i for i,chunk in enumerate(chunks))

                #append [title, trackDurationSeconds] to tracklistArr
                tracklistArr.append([ track.title , trackDurationSeconds])
                count = count+1
            else:
                everyTrackHasDuration = False

    #make sure each track has duration before continuing
    if everyTrackHasDuration:
        print("tracklistArr = ")
        print(tracklistArr)
        finalTracklist = calculateTracklist(tracklistArr)
        return finalTracklist
    else:
        print("everyTrackHasDuration = False")
        return ['Discogs Release tracklist does not have a duration for every track.']


def calculateTracklist(input):
    #input will look like this:
    #[['Night In Tunisia', '3:34'], ['Herds And Hoards', '4:35'], ['Credo', '4:45'], ["Winter's Light (A Dream)", '7:08'], ['First Of All One Must Be Very Open Minded', '16:22'], ['The Charioteer', '3:50']]
    output = []
    STC = 0     #start time cumulative 
    ETC = 0     #end time cumulative
    for i in range(0, len(input)):
        print("calculateTracklist(), i = ", i, ' input[i][0] = ', input[i][0])
        if i == 0:
            print("first")
            STC = 0
            ETC = input[i][1]
        else:
            print("not first")
            STC = ETC 
            trackDuration = input[i][1]
            print('trackDuration = ', trackDuration)
            ETC = STC + input[i][1]

        print("STC = ", STC, ". ETC = ", ETC)
        #convert STC and ETC to dateTime format
        STC_dateTime = str(datetime.timedelta(seconds=STC))
        ETC_dateTime = str(datetime.timedelta(seconds=ETC))
        
        print("STC_dateTime = ", STC_dateTime, ". ETC_dateTime = ", ETC_dateTime)
        print("\n")
        trackStr = STC_dateTime + " - " + ETC_dateTime + " " + input[i][0]
        output.append([ trackStr])
    #tracklist = [['00:00 - 01:23', '01. boboadasd'], ['01:23 - 22:43',  '02. momo'], ['22:43 - 33:02', '03. koko']]
    return output