import requests, json
from requests.exceptions import HTTPError
url = "
https://collectionapi.metmuseum.org/public/collection/v1/search?q=python&hasImages=true"
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        json_response = json.loads(response.text)
        listIds = json_response['objectIDs']
        list_range = len(listIds)
        listIds[random.randint(1,list_range)]


        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success')

