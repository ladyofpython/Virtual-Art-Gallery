import requests, json, random, urllib, os.path
import mod
import menuLogic
from requests.exceptions import HTTPError

def mainMenu():
    print("  Virtual Art Museum")
    print("- - - - - - - - - - - -")
    print("  1) Search for an image")
    print("  2) Randomly return an image")
    print("  0) Exit Program")

    #take user input
    userInput = input("Select an Option: ")
    # set user decision
    if userInput == '1':
        # option 1 - search for an image
        print("You selected: 1 - Search for an image")
        userInput = ("Enter a search term: ")

    elif userInput == '2':
        # option 2 - randomly return an image
        print("You selected: 2 - Randomly return an image")

        try:
            rWord = mod.rWord()
            url = mod.generateSearch(rWord)
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
            print(' [+] File Downloaded Successfully. =^.^=')
            mod.decorator()

    elif userInput == '0':
        # option 0 - exit program
        print("You selected: 0 - Exit Program")
        print("Exiting Program.")
        exit(0)


mainMenu()
