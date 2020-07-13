from bs4 import BeautifulSoup
from urllib.error import URLError
import requests
from typing import Dict
import time
import random
import os

def saveLink(volume,issue):
    # request url
    url = 'https://pubsonline.informs.org/toc/mksc/'+str(volume)+'/'+str(issue)
    session = requests.Session()
    headers: Dict[str, str] = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"}
    try:
        html = session.get(url, headers=headers, verify=False, timeout=10)
        html.encoding = 'utf-8'
    except URLError as e:
        return 100
    if html.status_code == 404:
        return 100
    soup = BeautifulSoup(html.content, 'html.parser')
    '''
    if soup.find('title').get_text().find('Not Found') > -1:
        return 100
    '''
    # find all 'a' tag to locate all links
    data = soup.find_all('a')

    # store them in a txt file
    file_name='/Users/zbx/Desktop/Summerproject/MarketingScience/Links/V'+str(volume)+'#issue#'+str(issue)+'.txt'
    file = open(file_name, mode='w', encoding='utf-8')

    # go over all 'a' tage and get their 'href' attribute
    for item in data:
        try:
            if item.string is not None and item['href'] != 'javascript:;' and item['href'] != '#':
                if str.__add__(item['href'], '\n').find("/doi/pdf") > -1:
                    file.write(str.__add__('https://pubsonline.informs.org'+item['href'], '\n'))
        except KeyError as e:
            print('fuck')
            continue
    file.close()
    size = os.path.getsize(file_name)
    return size
t = 1
for i in range(1, 39):
    for j in range(1, 7):
        while True:
            a = saveLink(i,j)
            time.sleep(10)
            if a < 30 :
                t = t+1
                time.sleep(10+2*t*t+random.random()*t)
            else:
                t = 1
                break
