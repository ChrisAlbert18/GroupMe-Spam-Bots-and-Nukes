Welcom Python GroupMe Nukes.
This repo contains scripts to run and manage automated processes on the group chat platform GroupMe.
The main goal of this project is to cause havoc.

Requirements: 
Python 2 or 3, Selenium module for Python, and Selenium web driver for google chrome (https://sites.google.com/a/chromium.org/chromedriver/downloads)

If you want to uses another browser, other drivers can be found here: https://pypi.org/project/selenium/
and you will have to change the driver in the code.

After being run, all scripts need you to log-in to GroupMe, load the target chat (no multichat), then give the script the prompt is requests.

So far this repository contains:

Standard_Nuke.py
	Description: Indefinately spams the same string of text or images in a directory.
	Usage: python3 Standard_Nuke.py [spam type] [spam option] [path to driver]
	Options:
		-h  							  |Help Menu
        	-t [message] [path to driver]                             |Text Spam
        	-i [path to directory of spam images] [path to driver]    |Image Spam

Standard_Nuke_From_IDE.py
	Description: Same as Standard_Nuke.py.
	Usage: Edit script and fill in driver path, spammed text, and path to image directroy.
	       Then put either text or image function in main and run.

Reply_Bot.py
	Description: Replies to keywords with a predetermined text or image reply.
		     Can be set to reply to itself by deleting
			"and last_message not in [dict[key1] for key1 in dict]"
		     from line 47.
	Usage: python3 Reply_Bot.py [path to web driver]
	Options: 
		-h  							  |Help Menu
		
	       Enter stimulus and response into Reply.csv in the form
	       		stimulus,response
	       and use quotes if the response has commas (,) in it.
	       		stimulus,"response, response"	
	       Enter images as a response with
			stimulus,[path to image]
	       If you are using a relative path on windows, replace all "\" with "/".

Smart_Bot.py
	Description: Connects Cleverbot to the GroupMe. Can either be purely reactive or
		     can drop a nuke by having an infinie conversation with itself.
	Usage: python3 Smart_Bot.py [bot function] [path to web driver]
	Options:
		-h  							  |Help Menu
          	-n [path to driver]     				  |Smart Nuke/Schizo Mode 
          	-c [path to driver]    				          |Chat Bot Mode
          
		Function defaults to Smart Nuke.
