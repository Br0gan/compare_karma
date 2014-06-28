#!/usr/bin/python

#import libs for parseing reddit json data.
import urllib.request
import json


id1 = input('Please provide the first user you wish to compare. \n')
id2 = input('Please provide the second user. \n')

#userdata1 = None
#userdata2 = None

def userInfo(user1, user2):
    userList = [user1, user2]
    score = []  
    total = []
    
    for user in userList:
        rawdata = urllib.request.urlopen('http://www.reddit.com/user/%s.json' % (user)).read()
        data = json.loads(rawdata.decode('utf8'))
        results = data['data']['children']
        
        for eachResult in results:
            score.append(eachResult['data']['score'])
            #print(score)
    
    print(len(score))
    
    for num in score:
        if len(total) < 1:
            x = num
            print("check")
        else:
            x = x + num
            print("check2")
    
    total.append(x)
    print('This is x', x)

userInfo(id1, id2)
