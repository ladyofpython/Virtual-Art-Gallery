#!/usr/bin/python3

import requests, json, random, urllib, os.path
import mod
import menuLogic
from requests.exceptions import HTTPError

def mainMenu():
	print("--> PRESS 0 TO EXIT <--")
	print("- - - - - - - - - - - -")
	print("  1) Return an image based on keyword")
	print("  2) Randomly return an image")

	#take user input
	userInput = input("Select an Option: ")
	# set user decision
	if userInput == '1':
		option1()
	elif userInput == '2':
		option2()
	elif userInput == '0':
		option0()

# INTERNAL FUNCTIONS
# option 1 - search for an image
def option1():
	print("You selected: 1 - Search for an image")
	# get search term from user
	userInput = input("Enter a search term: ")
	try:	
		# use term to search for image
		url=mod.generateSearch(userInput)
		# TEST PRINT
		# print("URL: " + url)
		# return an image from the Met
		r = mod.getImageInfoAll(url)
		filename, rImage = mod.setImageInfo(r)
		mod.getImage(filename, rImage)
	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
	except Exception as err:
		print(f'Other error occurred: {err}')
	else:
		print(' [+] File Downloaded Successfully. =^.^=')
		mod.decorator()

def option2():
	# option 2 - randomly return an image
	print("You selected: 2 - Randomly return an image")
	try:
		rWord = mod.rWord()
		url = mod.generateSearch(rWord)
		r = mod.getImageInfo(url)
		filename, rImage = mod.setImageInfo(r)
		mod.getImage(filename, rImage)
		print(' [+] File Downloaded Successfully. =^.^=')
	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
	except Exception as err:
		print(f'Other error occurred: {err}')
	else:
		print('[-]FAIL: Program End.')
	mod.decorator()

def option0():
		# option 0 - exit program
		print("You selected: 0 - Exit Program")
		print("Exiting Program.")
		exit(0)

# MAIN 
mainMenu()
