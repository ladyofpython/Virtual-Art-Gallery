import requests, json, random, urllib, os.path, time

# internal functions

def decorator_glasses():
    time.sleep(1)
    print("( •_•)>⌐■-■ ")
    time.sleep(1)
    print("(⌐■_■) ")

# external functions

def decorator():
    print()
    print()

# generates a random word using a local dictionary file
def rWord():
    f = open("wordlist.txt", "r")
    txt = f.read()
    txt = txt.split('\n')
    random.seed(time.time())
    rnum = random.randint(1,len(txt))
    #print("rnum: "+str(rnum))
    rWord = txt[rnum]
    #print("rWord: "+str(rWord))
    rWord = rWord.replace("'", "")
    return rWord

# retrieves information from a random object
def generateSearch():
    word = rWord()
    decorator()
    print("Search Word: "+str(word))
    decorator_glasses()
    baseurl = "https://collectionapi.metmuseum.org/public/collection/v1/"
    query = "search?q="+word+"&hasImages=true"
    url = str(baseurl)+str(query)
    return url

# selects an object in the Met database and returns information on it
def getImageInfo(url):
    response = requests.get(url)
    r = json.loads(response.text)
    #print("reponse.text: "+str(r))
    lIDs = r['objectIDs']
    
    #i=0
    #for x in lIDs:
    #    i+=1
    #    print(str(i)+":"+str(x))
    lr = len(lIDs)
    #rn = random.choice[lIDs]
    rn = lIDs[random.randint(1,lr)]
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    url += str(rn)
    response = requests.get(url)
    r = json.loads(response.text)
    return r

# sets some information about the selected object in the Met database
def setImageInfo(r):
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
    print("\n   Artist:    "+rName)
    print("   Title:     "+rTitle)
    print("   Medium:    "+rON)
    print("   Period:    "+rPeriod+"\n")
    print(" [/] Filename: "+filename)
    
    return filename, rImage

