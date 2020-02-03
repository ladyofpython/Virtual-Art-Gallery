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
