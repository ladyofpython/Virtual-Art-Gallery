import requests, json, random, urllib, os.path
import mod
from requests.exceptions import HTTPError

try:
    url = mod.generateSearch()
    r = mod.getImageInfo(url)
    filename, rImage = mod.setImageInfo(r)
    with open(filename, 'wb') as handle:
        response = requests.get(rImage, stream=True)
        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('File Downloaded Successfully. =^.^=')

