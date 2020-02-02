import requests
from requests.exceptions import HTTPError

for url in ['https://collectionapi.metmuseum.org/public/collection/v1/departments']:
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        print(response.text)
        print()
        response.json()
        print()
        #print(response.headers)
        
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success')

