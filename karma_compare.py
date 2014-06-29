#!/usr/bin/python

#import libs for parseing reddit json data.
import urllib.request
import json


#while loop switch
x = True

#store user ID's
def userInput():
    global id1, id2

    id1 = input('Please provide the first user you wish to compare. \n')
    id2 = input('Please provide the second user. \n')
    
    userInfo(id1, id2)    

#gather users karma information and store it for comparison
def userInfo(user1, user2):
    global total

    userList = [user1, user2]
    total = []
    
    for num in userList:
        #pulls users data from reddit.com/user/
        for user in userList:
            score = []
            rawdata = urllib.request.urlopen('http://www.reddit.com/user/%s.json' % (user)).read()
            data = json.loads(rawdata.decode('utf8'))
            results = data['data']['children']
            #scrapes out relevant json data
            for eachResult in results:
                score.append(eachResult['data']['score'])
                #print(score)
        print(sum(score)) 
        total.append(sum(score))
    
    print(total)
    compUsers()

#displays differences in users karma score.
def compUsers():
    print(total)
    print(id1,' has a karma score of ', total[0])
    print('-'*10)
    print(id2,' has a karma score of ', total[1])
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
 
