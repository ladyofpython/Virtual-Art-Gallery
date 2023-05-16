#!/usr/bin/python3

import requests, json, random, urllib, os.path
import mod
from requests.exceptions import HTTPError

def main():
	print("          VIRUTAL ART MUSEUM")
	print("- - - - - - - - - - - - - - - - - - - -")
	print("  1) Return an image based on keyword")
	print("  2) Randomly return an image")
	print("  0) Exit Program")

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
	userInput = input("Enter a search term: ")
	try:	
		url=mod.generateSearch(userInput)
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
		mod.decorator()

def option0():
		print("Exiting Program.")
		exit(0)

main()
