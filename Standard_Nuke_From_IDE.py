# Chris Albert, Last Update 5/17/2019

# To get running, you need to:
#     1) Enter paths/inputs.
#     2) Choose a function to run in main.
driver_path = ''
spammed_text = ''
image_directory = ''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import listdir, path

browser = webdriver.Chrome(driver_path)

# Text Nuke
def text_nuke(text):
    chat_input = browser.find_element_by_class_name('emoji-wysiwyg-editor')
    while True:
        chat_input.send_keys(text)
        chat_input.send_keys(Keys.ENTER)

# Image Nuke
def image_nuke(directory):
    for pic in listdir(directory):
        extension = pic.title().split('.')[-1]
        if extension not in ['Png','Jpg','Gif']:
            pass
        else:
            ammo_path = path.join(directory,pic)
            browser.find_element_by_id('filestyle-0').send_keys(ammo_path)
            sleep(2)
            for x in browser.find_elements_by_tag_name('BUTTON'):
                try:
                    if x.get_property('outerText') == "Send":
                        x.click()
                except:
                    pass

if __name__ == '__main__':
    browser.get('https://web.groupme.com/chats')
    input("\nLoad target chat. No multichat! Press enter when ready.")

    #text_nuke(spammed_text)
    #image_nuke(image_directory)
