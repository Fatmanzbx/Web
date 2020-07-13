from typing import Dict
import requests
from bs4 import BeautifulSoup
import os
import time
import random
Location = '/Users/zbx/Desktop/Summerproject/JournalOfConsumerResearch'
codeWrong =[]
def getPage(url):
    session = requests.Session()
    headers: Dict[str, str] = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    try:
        req = session.get(url, headers=headers, verify=False, timeout=10)
        req.encoding = 'utf-8'
        bsObj = BeautifulSoup(req.text, 'html.parser')
    except Exception as e:
        return None
    return bsObj
def getContent(html,issue,number):
    file_name = Location+'/Passage/'+issue+'Passage'+str(number)+'.txt'
    with open(file_name, 'a') as file_handle:
        # get title
        title = html.find('h1')
        try:
            result = title.get_text()
            if not result is None:
                file_handle.write(result)
        except AttributeError as e:
            return 1
        # get date
        date = html.find('div', class_='citation-date')
        try:
            file_handle.write('\n')
            file_handle.write(date.get_text())
            file_handle.write('\n')
        except AttributeError as e:
            return 1

        # get author
        author = html.find_all('div', class_="info-card-author authorInfo_OUP_ArticleTop_Info_Widget")
        file_handle.write('\n')
        file_handle.write('author\n')
        for content in author:
            try:
                for result in content.find_all('div', class_="info-card-name"):
                    file_handle.write(result.get_text())
                    file_handle.write('\n')
            except AttributeError as e:
                continue
        # get abstact
        abstract = html.find('section', class_='abstract')
        file_handle.write('\n')
        file_handle.write('abstract\n')
        try:
            file_handle.write(abstract.get_text())
            file_handle.write('\n')
        except AttributeError as e:
            os.remove(file_name)
            return 100
        # get key words
        file_handle.write('\n')
        file_handle.write('key words\n')
        try:
            keywords = html.find('div', class_='kwd-group').find_all('a')
            for content in keywords:
                result = content.get_text()
                if not result is None:
                    file_handle.write(content.get_text())
                    file_handle.write('\n')
        except AttributeError as e:
            print("pass")

        # get article
        article = html.find_all('p', class_='chapter-para')
        file_handle.write('\n')
        k = 0
        for content in article:
            if k == 0:
                k = k + 1
                continue
            try:
                result = content.get_text()
                if not result is None:
                    file_handle.write(content.get_text())
                    file_handle.write('\n')
            except AttributeError as e:
                continue
    file_handle.close
    return os.path.getsize(file_name)

def generateCorpus(file):
    fopen = open(file)
    issue =file[-14:-4]
    try:
        lines = fopen.readlines()
    except UnicodeDecodeError as e:
        codeWrong.append(issue)
        return
    i = 1
    t = 1
    for line in lines:
        while True:
            url = line[:-1]
            Web = getPage(url)
            if Web is None:
                break
            else:
                size = getContent(Web,issue,i)
            if size < 50:
                t = t + 1
                time.sleep(10 + 3 * t * t + random.random() * t)
                continue
            if size < 300:
                break
            i=i+1
            t = 1
            break

files = os.listdir(Location+'/Links')
for file in files:
    generateCorpus(Location+'/Links/'+file)
for issue in codeWrong:
    print(issue)

