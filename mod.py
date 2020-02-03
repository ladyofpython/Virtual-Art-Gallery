import requests, json, random, urllib, os.path

######################
# EXTERNAL FUNCTIONS #
######################

def rWord():
    f = open("wordlist.txt", "r")
    txt = f.read()
    #print(txt)
    txt = txt.split('\n')
    rnum = random.randint(1,len(txt))
    rWord = txt[rnum]
    rWord = rWord.replace("'", "")
    return rWord

def generateSearch():
    word = rWord()
    print("Search Word: "+str(word))
    query = "search?q="+word+"&hasImages=true"
    baseurl = "https://collectionapi.metmuseum.org/public/collection/v1/"
    url = str(baseurl)+str(query)
    return url

def getImageInfo(url):
    response = requests.get(url)
    r = json.loads(response.text)
    lIDs = r['objectIDs']
    lr = len(lIDs)
    rn = lIDs[random.randint(1,lr)]
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    url += str(rn)
    response = requests.get(url)
    r = json.loads(response.text)
    return r

######################
# INTERNAL FUNCTIONS #
######################

def setImageInfo(r):
    i={}
    # set primage image
    rImage=r['primaryImage']
    
    # set object name
    rON = r['objectName']
    
    # set object title
    rTitle = r['title']
    
    # set object time period
    rPeriod = r['period']
    if rPeriod == "":
        rPeriod = "n.d."

    # set artist name
    rName = r['artistDisplayName']
    if rName == "":
        rName = "unknown"

    # set fileName
    fName = str(rName+str(rTitle)+str(rPeriod))
    filename = ""
    for x in fName:
        if x.isalnum():
            filename += x
    filename += ".jpg"
    # Display Data
    print("Artist: "+rName)
    print("Title: "+rTitle)
    print("Medium: "+rON)
    print("Period: "+rPeriod)
    print("Filename: "+filename)
    
    return filename, rImage

