
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup

url = "https://academic.oup.com/jcr/article/22/4/345/1790489"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
def getPage(url):
    session = requests.Session()

    try:
        req = session.get(url, headers=headers, verify=False, timeout=10)
        req.encoding = 'utf-8'
        bsObj = BeautifulSoup(req.text, 'html.parser')
    except Exception as e:
        return None
    return bsObj
soup = getPage(url)
data = soup.find_all('a')
a = 'f'
for item in data:
    try:
        if item.string is not None and item['href'] != 'javascript:;' and item['href'] != '#':
            if str.__add__(item['href'], '\n').find(".pdf") > -1:
                a = str.__add__(item['href'], '\n')
    except KeyError as e:
        continue
a='https://academic.oup.com/jcr/article-pdf/22/4/345/5065852/22-4-345.pdf'
r=requests.get(a, headers=headers, verify=False, timeout=10)
urlretrieve(a,'/Users/zbx/Desktop/demo.txt')



