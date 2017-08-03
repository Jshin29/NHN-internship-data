#author Justin Shin
import string
import urllib2


applist=[]
f = open("C\\Documents\\bundleids_head.txt")
line = f.readline()
while line:
    applist.append(line)
    line = f.readline()



Idlist= [ "bundleId", "trackName", "trackId", "isVpp", "primaryGenre",
          "releaseD", "sellerName" , "currentVersionReleaseDate",
          "formattedPrice", "averageUserRating", "userRatingCount"]

X= open('output_data.txt' , 'w')
for app in applist:
    url = 'http://itunes.apple.com/lookup?bundleId=' +app
    data = urllib2.urlopen(url)
    data = data.readlines()
    tokenList = []
    for line in data:
        words = line.split(",")
        for word in words:
            tokenList.append(word)

    for Id in Idlist:
        for token in tokenLIst:
            index = tokenList.index(token)
            while Id in tokenLIst[index]:
                print tokenLIst[index]
                index = index +1
    
