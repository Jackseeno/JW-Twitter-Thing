from twitter import *
import cPickle as pickle
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

def twitstuff():


    a = 'xxx'
    b = 'xxx'
    c = 'xxx'
    d = 'xxx'
    t = Twitter(auth=OAuth(a, b, c, d))
    jw = t.statuses.user_timeline(count=200, screen_name='JWONDER21')
    lst = []
    it = '#ITUNES'
    ht = 'http'
    remove = '-'
    id = jw[0]['id']
    rtwd = 'Retweeted'
    tc = 'https://t.co'
    cl = 'click'
    new = "#new"
    print id
    for item in jw:
        rt = item['retweeted']
        x = item['text'].encode('utf-8')
        if x [0:2] == 'RT': 
            pass
        elif x[:4] == cl:
            pass
        elif x[:3] == new:
            pass
        elif x[0] == '@':
            pass
        elif ht in x:
            end1 = int(x.find(it))
            end2 = int(x.find(ht))
            n = x[:end1]
            i = n.translate(None, ''.join(remove))
            i = i.strip(' ')
            if i in lst:
                pass
            elif tc in i:
                pass
            else:
                lst.append(i)
    return lst



def ytsrch(x):
    batch = {}
    url_header= "https://www.youtube.com/watch?v="
    DEVELOPER_KEY = "xxx"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    page_size = 1
    playlist = 'xxx'
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
                    
                except KeyError:
                    continue
    print "returning batch"
    return batch

def save_to_text(x):
    one = '<a href="'
    two = '" target="_blank">'
    three = '</a>'
    f = open("jw.html", "w")
    for key, value in x.items():
        thing = one + value + two + key + three
        #check = f.readlines()
        f.write(str(thing + '<br />'))
        
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
