import requests, json, random, urllib, os.path

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

def getImage(url):
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
