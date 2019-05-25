# Chris Albert, Last Update 5/25/2019
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# -h : help
# -n : nuke
# -c : chat bot

args = sys.argv
if len(args) == 1:
    raise ValueError("No path to driver specified. Format: python Smart_Bot.py [bot function] [path to web driver]")
if args[1] == '-h':
    print("Options\n-h  Help Menu"
          "\n-n [path to driver]     Smart Nuke (aka Schizo Mode) "
          "\n-c [path to driver]    Chat Bot Mode"
          "\nChromeDriver default; edit script for other drivers."
          "\nFunction defaults to Smart Nuke.")
    sys.exit()
elif args[-1].split('.')[-1] != 'exe':
    raise ValueError("No path to driver specified. Format: python Smart_Bot.py [bot function] [path to web driver]")


browser1 = (webdriver.Chrome(args[-1]))
browser1.get('https://web.groupme.com/chats')
browser2 = (webdriver.Chrome(args[-1]))
browser2.get('https://www.cleverbot.com/')

input("\nLoad target chat. No multichat! Press enter when ready.")

chat_input = browser1.find_element_by_class_name('emoji-wysiwyg-editor')
clever_bot_input = browser2.find_element_by_class_name('stimulus')
clever_bot_output = ''
old_message = ''

while True:
    last_message = browser1.find_elements_by_class_name('message-text')[-1].get_property('outerText')
    words_in_l_m = last_message.split(" ")
    clever_bot_output = browser2.find_elements_by_class_name('bot')[-1].get_property('outerText')

    # Chat Bot Mode
    if args[1] == '-c':

        if old_message != last_message and last_message != clever_bot_output:
            old_message = last_message
            clever_bot_input.send_keys(last_message)
            sleep(0.5)
            clever_bot_input.send_keys(Keys.ENTER)

            sleep(4)

            clever_bot_output = browser2.find_elements_by_class_name('bot')[-1].get_property('outerText')

            chat_input.send_keys(clever_bot_output)
            chat_input.send_keys(Keys.ENTER)

    # Smart Nuke/Schizo Mode
    elif args[1] == '-n' or len(args) == 2:
        old_message = last_message
        clever_bot_input.send_keys(last_message)
        sleep(0.5)
        clever_bot_input.send_keys(Keys.ENTER)

        sleep(4)

        clever_bot_output = browser2.find_elements_by_class_name('bot')[-1].get_property('outerText')

        chat_input.send_keys(clever_bot_output)
        chat_input.send_keys(Keys.ENTER)