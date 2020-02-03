import mod

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
    elif userInput == '2':
        # option 2 - randomly return an image
        print("You selected: 2 - Randomly return an image")
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

    elif userInput == '0':
        # option 0 - exit program
        print("You selected: 0 - Exit Program")
        print("Exiting Program.")
        exit(0)
