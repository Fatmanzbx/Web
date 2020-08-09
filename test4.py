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
def getPage(url):
    session = requests.Session()
    try:
        req = session.get(url, headers=headers, verify=False, timeout=10)
        req.encoding = 'utf-8'
        bsObj = BeautifulSoup(req.text, 'html.parser')
    except Exception as e:
        return None
    return bsObj
def getTitle(html):
    title = html.find('h1')
    try:
        result=title.get_text()
        if result is None:
            return 'error'
        else:
            return result
    except AttributeError as e:
        return 'error'
def savePdf(url,name):
    s =1
    a = random.random()
    while True:
        Web = getPage(url)
        title=getTitle(Web).strip()
        print(title)
        if title != 'error': break
        else:
            time.sleep(10*a+5*s)
            s=s+1
    driver.get('https://scholar.google.com/')
    t = random.random()
    time.sleep(5*t)
    element=driver.find_element_by_name('q')
    element.send_keys(title)
    b = random.random()
    time.sleep(9*t*b)
    element.submit()
    time.sleep(7*b*b)
    out = 1
    while out ==1 :
        out -=1
        try:
            paper=driver.find_element_by_partial_link_text('PDF')
        except common.exceptions.NoSuchElementException as e:
            out+=1
            time.sleep(5)
    paper.click()
    link=paper.get_attribute('href')
    pdf=link.split('/')[-1]
    out=0
    k = 0
    while out==0:
        out+=1
        try:
            os.rename(Location+'/PDF/'+pdf, name)
        except FileNotFoundError as e:
            k+=1
            out -= 1
            time.sleep(2)
        if k > 50:
            file = '/Users/zbx/Desktop/demo.txt'
            with open(file, 'a') as f:
                f.write(pdf)
                break
codeWrong=[]
def generateCorpus(file):
    fopen = open(file)
    issue =file[-14:-4]
    try:
        lines = fopen.readlines()
    except UnicodeDecodeError as e:
        codeWrong.append(issue)
        return
    i = 1
    for line in lines:
        url = line[:-1]
        name = Location+'/PDF/'+issue+'Passage'+str(i)+'.pdf'
        savePdf(url, name)
        i=i+1

files = os.listdir(Location+'/Links')
for file in files:
    generateCorpus(Location+'/Links/'+file)
    shutil.move(Location+'/Links/'+file, Location+'/Links2/'+file)
    time.sleep(10)
for issue in codeWrong:
    print(issue)