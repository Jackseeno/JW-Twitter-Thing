from twitter import *
import cPickle as pickle
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from datetime import date, timedelta, datetime

def twitstuff():


    a = 'zzz'
    b = 'zzz'
    c = 'zzz'
    d = 'zzz'
    t = Twitter(auth=OAuth(a, b, c, d))
    #ogid = 930143044749414401
    
    with open('id.txt', 'r+') as read_id:
        last_id = int(read_id.readline())
    print last_id
    jw = t.statuses.user_timeline(count=200, screen_name='JWONDER21')
    it_id = jw[0]['id']
    add_id = open('id.txt', 'w')
    add_id.write(str(it_id))
    add_id.close
    lst = []
    it = '#ITUNES'
    ht = 'http'
    remove = '-'
    rtwd = 'Retweeted'
    tc = 'https://t.co'
    cl = 'click'
    new = "#new"
    you = 'youtu'
    nuum = you[-2]
    for item in jw:
        #print item['id']
        rt = item['retweeted']
        x = item['text'].encode('utf-8')

        if x [0:2] == 'RT': 
            pass #removes retweets
        elif x[:4] == cl:
            pass #removes click to buy
        elif x[:3] == new:
            pass #removes new music friday stuff
        elif x[0] == '@':
            pass #removes tweets that start with @

        elif ht in x:
            
            end1 = int(x.find(it))
            end2 = int(x.find(ht))
            n = x[:end1]
            i = n.translate(None, ''.join(remove))
            i = i.strip(' ')
            if i in lst:
                pass
#            elif tc in i:
#                pass
            else:
                lst.append(i)
    return lst
    print "Retrieved tweets..."
#    wrte = open('id.txt', 'w')
#    wrte.write(last_id)
#    wrte.close()
    
    

def ytsrch(x):
    
    batch = {}
    url_header= "https://www.youtube.com/watch?v="
    DEVELOPER_KEY = "zzz"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    page_size = 1
    playlist = 'PLGo8zA-BDOfTRjVNmjJA9CbpoiPaqzThT'
    for item in x:
        dd = item
        #print dd
        #videos.append("Channel Title: %s\nTitle: %s\nID: %s\nPicURL: %s\n" % (search_result["snippet"]["channelTitle"],      
        search_result = youtube.search().list(q=dd, type="video", part="id", maxResults=1).execute()
        for thing in search_result.get("items", []):
            #print search_result
            if thing["id"]["kind"] != "youtube#video":
                pass
            else:
                try:
                    vid_id = thing["id"]["videoId"].encode('utf-8')
                    url = url_header + vid_id
                    batch[dd] = url
                    print "Added To Batch"
                except KeyError:
                    continue
    print "Youtube Search Complete"
    return batch

def save_to_text(x):
    print "Saving html file..."
    one = '<a href="'
    two = '" target="_blank">'
    three = '</a>'
    f = open("jw.html", "a")
    datentime = str(datetime.now())
    print datentime
    f.write(datentime + '<br />' + '\n')
    f.close()
    for key, value in x.items():
        d = open("jw.html", "r+")
        w = d.read()
        thing = one + value + two + key + three
        #check = f.readlines()
        if thing in w:
            pass
        else:
            d.write(str(thing + '<br />' + '\n'))
        d.close()
    f.close()
   
ccc = twitstuff()
ddd = ytsrch(ccc)
sss = save_to_text(ddd)

#songs = pickle.load( open( "songs.p", "rb" ) )
#        if item in songs:
#            pass
#        else:
#            pickle.dump( lst, open( "songs.p", "wb" ) )
#    pickle.dump( id, open( "songs.p", "wb" ) )
