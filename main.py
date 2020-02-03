import requests, json, random, urllib, os.path
import randomWord
from requests.exceptions import HTTPError

# generate search
word = randomWord.rWord()
print("Search Word: "+str(word))
query = "search?q="+word+"&hasImages=true"
baseurl ='https://collectionapi.metmuseum.org/public/collection/v1/'
url = str(baseurl)+str(query)
print(url)
try:
    # Grab information
    response = requests.get(url)
    
    # Pull a random art selection from the list
    r = json.loads(response.text)
    lIDs = r['objectIDs']
    lr = len(lIDs)
    rn = lIDs[random.randint(1,lr)]
    # print(rn)
    url2='https://collectionapi.metmuseum.org/public/collection/v1/objects/'
    url2+=str(rn)
    # request the image from the MET API
    response = requests.get(url2)
    r = json.loads(response.text)
    # print(r)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success')


# grab primary image [primaryImage]
rImage=r['primaryImage']
# print(rImage)
# grab the physical type of the object [objectName]
rON=r['objectName']
# print(rON)
# grab title [title]
rTitle=r['title']
# print(rTitle)
# grab time period when object was created [period]
rPeriod=r['period']
# print(rPeriod)
# grab artist name [artistDisplayName]
rName=r['artistDisplayName']
# print(rName)

# print the location where the image was saved
# file is saved as ARTIST_TITLE_PERIOD
fName = str(rName)+str(rTitle)+str(rPeriod)
fileName = ""

# remove spaces and special character from the file name fName
for x in fName:
    if x.isalnum():
        fileName += x
fileName+=".jpg"
print("fName: "+fileName)
try:
    with open(fileName, 'wb') as handle:
        response2 = requests.get(rImage, stream=True)
        if not response2.ok:
            print(response2)

        for block in response2.iter_content(1024):
            if not block:
                break

            handle.write(block)
except:
    print("File download fail")
