# Chris Albert, Last Update 5/17/2019
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import listdir, path
import sys
# -h : help
# -t : text spam
# -i : image spam

args = sys.argv

if args[1] == '-h':
    print("Options\n-h  Help Menu"
          "\n-t [message] [path to driver]     Text Spam"
          "\n-i [path to directory of spam images] [path to driver]    Image Spam"
          "\nChromeDriver default; edit script for other drivers.")
    sys.exit()

browser = webdriver.Chrome(args[-1])
browser.get('https://web.groupme.com/chats')
input("\nLoad target chat. No multichat! Press enter when ready.")


# Text Nuke
if args[1] == '-t':
    text = ' '.join(args[2:-1])
    chat_input = browser.find_element_by_class_name('emoji-wysiwyg-editor')
    while True:
        chat_input.send_keys(text)
        chat_input.send_keys(Keys.ENTER)


# Image Nuke
if args[1] == '-i':
    while True:
        ammo_dir = str(args[2])
        for pic in listdir(ammo_dir):
            extension = pic.title().split('.')[-1]
            if extension not in ['Png','Jpg','Gif']:
                pass
            else:
                ammo_path = path.join(ammo_dir,pic)
                browser.find_element_by_id('filestyle-0').send_keys(ammo_path)
                sleep(2)
                for x in browser.find_elements_by_tag_name('BUTTON'):
                    try:
                        if x.get_property('outerText') == "Send":
                            x.click()
                    except:
                        pass
