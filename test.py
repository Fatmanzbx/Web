import shutil
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import common
import time
import requests
import os
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
Location="/Users/zbx/Desktop/Summer/JOCR"
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": Location+'/PDF', #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
driver = webdriver.Chrome(options=options)
s =1
a = random.random()
title='Primary and Secondary Validity of Consumer Purchase Probabilities'
driver.get('https://scholar.google.com/')
t = random.random()
time.sleep(5*t)
element=driver.find_element_by_name('q')
element.send_keys(title)
b = random.random()
time.sleep(6*t*b)
element.submit()
time.sleep(4*b*b)
out = 1
while out ==1 :
    out -=1
    try:
        paper=driver.find_element_by_partial_link_text('Full View')
    except common.exceptions.NoSuchElementException as e:
        out+=1
        time.sleep(5)
paper.click()
