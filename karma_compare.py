#!/usr/bin/python

#import libs for parseing reddit json data.
import urllib.request
import json


#while loop switch
x = True

#check if user name exsists
def userCheck(user):
    r = urllib.request.Request('http://www.reddit.com/user/%s.json' % (user))
    try:
        urllib.request.urlopen(r)
    except urllib.error.HTTPError:
        newUser = input('Does not exsist. Try again. \n')
        userCheck(newUser)
        return(newUser)
    else:
        return(user)

#store user ID's
def userInput():
    global id1, id2

    id1 = input('Please provide the first user you wish to compare. \n')
    id1 = userCheck(id1)
    id2 = input('Please provide the second user. \n')
    id2 = userCheck(id2)
    userInfo(id1, id2)    

#gather users karma, up votes, and downvote information and stores it for comparison
def userInfo(user1, user2):
    global total, uTotal, dTotal

    userList = [user1, user2]
    total = []
    uTotal = []
    dTotal =  []
    #pulls users data from reddit.com/user/
    for user in userList:
        
        ups = []
        downs = []
        score = []
        results = None  
        rawdata = urllib.request.urlopen('http://www.reddit.com/user/%s.json' % (user)).read()
        data = json.loads(rawdata.decode('utf8'))
        results = data['data']['children']
        #scrapes out relevant json data
        
        for eachResult in results:
            score.append(eachResult['data']['score'])
            ups.append(eachResult['data']['ups'])
            downs.append(eachResult['data']['downs'])
        
        total.append(sum(score))
        uTotal.append(sum(ups))
        dTotal.append(sum(downs))

    compUsers()

#displays differences in users karma score.
def compUsers():
    
    print(id1,' has a karma score of ', total[0], ' ||up votes:',uTotal[0], '||down votes:',dTotal[0])
    print('-'*10)
    
    print(id2,' has a karma score of ', total[1], ' ||up votes:',uTotal[1], '||down votes:',dTotal[1])
    print('-'*10)

    if total[0] > total[1]:
        diference = total[0] - total[1]
        print(id1,' wins with ', diference, ' more karma points!')
    elif total[0] == total[1]:
        print('It\'s a tie!')
    else:
        diference = total[1] - total[0]
        print(id2,' wins with ', diference, ' more karma points!')

#loop to keep progam alive for more then one cycle
while x == True:
    userInput()
    choice = input('Would you like to compare another 2 users?(y/n) \n')
    if choice == 'y':
        x = True
    else:
        x = False

