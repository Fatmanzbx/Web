from bs4 import BeautifulSoup
from urllib.error import URLError
import requests
from typing import Dict
import os
url = 'https://pubsonline.informs.org/toc/mksc/39/4'
session = requests.Session()
headers: Dict[str, str] = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
try:
    html = session.get(url, headers=headers, verify=False, timeout=10)
    html.encoding = 'utf-8'
except URLError as e:
    print('error')
if html.status_code == 404:
    print('error')
soup = BeautifulSoup(html.text, 'html.parser')

    # find all 'a' tag to locate all links
data = soup.find_all('a')

    # store them in a txt file
file = open('/Users/zbx/Desktop/demos.txt', mode='w', encoding='utf-8')

    # go over all 'a' tage and get their 'href' attribute
for item in data:
    try:
        if item.string is not None and item['href'] != 'javascript:;' and item['href'] != '#':
            if str.__add__(item['href'], '\n').find("/doi/pdf") > -1:
                file.write(str.__add__(item['href'], '\n'))
    except KeyError as e:
        print('fuck')
        continue

file.close()
print(os.path.getsize('/Users/zbx/Desktop/demos.txt'))

