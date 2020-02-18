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
def generateSearch(word):
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
    lr = len(lIDs)
    #rn = random.choice[lIDs]
    rn = lIDs[random.randint(1,lr)]
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    url += str(rn)
    response = requests.get(url)
    r = json.loads(response.text)
    return r

# gives the user a choice on which image to download based off of artist and title
def getImageInfoAll(url):
    response = requests.get(url)
    r = json.loads(response.text)
    lIDs = r['objectIDs']
    i = 0
    idict = {"0":"",}
    print()
    for x in lIDs:
        if i >= 10:
            break
        i+=1
        idict[i]=str(x)
        url="https://collectionapi.metmuseum.org/public/collection/v1/objects/"+str(x)
        response=requests.get(url)
        r=json.loads(response.text)
        #print(r)
        rArtist=r['artistDisplayName']
        if rArtist=="":rArtist="Unknown"
        rTitle=r['title']
        if rTitle=="":rTitle="Unknown"
        print(str(i)+" "+str(rArtist)+" - "+str(rTitle))
    i=int(input("Select an image to download: "))
    imgID=idict[i]
    url="https://collectionapi.metmuseum.org/public/collection/v1/objects/"+str(imgID)
    response=requests.get(url)
    return json.loads(response.text)

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
    print(" [-] Filename: "+filename)
    
    return filename, rImage

# gets the image from the Met
def getImage(filename, rImage):
    with open(filename, 'wb') as handle:
        response = requests.get(rImage, stream=True)
        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
