# Chris Albert, Last Update 5/24/2019
import csv
import sys
from time import sleep
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# -h : help

args = sys.argv

if len(args) == 1:
    raise ValueError("No path to driver specified. Format: python Reply_Bot.py [path to web driver]")
if args[1] == '-h':
    print("Format: python Reply_Bot.py [path to web driver]\n"
          "\nEnter the trigger word and reply in Reply.csv in the following format:"
          "\ntrigger1,bot reply1"
          "\ntrigger2,bot reply2"
          "\ntrigger3,bot reply3"
          "\nEtc."
          "\n\nNote 1: If trigger or reply contains a comma, enclose reply in quotes"
          "\nex: trigger,\"bot, reply\""
          "\nNote 2: Send image reply by putting the path in reply spot"
          "\nNote 2.1: If using relative path on windows, replace \ with /")
    sys.exit()

browser = (webdriver.Chrome(args[-1]))
browser.get('https://web.groupme.com/chats')
input("\nLoad target chat. No multichat! Press enter when ready.")

chat_input = browser.find_element_by_class_name('emoji-wysiwyg-editor')

replies = open('Reply.csv', mode = 'r')
replies_read = csv.reader(replies)
dict = {}
for row in replies_read:
    dict[row[0]] = row[1]
replies.close()

while True:
    last_message = browser.find_elements_by_class_name('message-text')[-1].get_property('outerText')
    words_in_l_m = last_message.split(" ")

    for key in dict:
        # delete second condition to allow bot to loop itself
        if key in words_in_l_m and last_message not in [dict[key1] for key1 in dict]:
            # text reply
            if dict[key].split('.')[-1] not in ['png','jpg','gif','JPG']:
                chat_input.send_keys(dict[key])
                chat_input.send_keys(Keys.ENTER)
                sleep(1)
            # image reply
            else:
                browser.find_element_by_id('filestyle-0').send_keys(path.abspath(dict[key]))
                sleep(2)
                for x in browser.find_elements_by_tag_name('BUTTON'):
                    try:
                        if x.get_property('outerText') == "Send":
                            x.click()
                    except:
                        pass
