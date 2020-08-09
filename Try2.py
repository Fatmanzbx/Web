from typing import Dict
import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
url = "https://academic.oup.com/jcr/article/22/4/345/1790489"
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
def getContent(html):
    file='/Users/zbx/Desktop/demo.txt'
    with open(file, 'a') as file_handle:
        # get title
        title = html.find('h1')
        try:
            result=title.get_text()
            if result is None:
                return
            else:
                file_handle.write(result)
        except AttributeError as e:
            print("pass")
        #get date
        date = html.find('div', class_='citation-date')
        try:
            file_handle.write('\n')
            file_handle.write(date.get_text())
            file_handle.write('\n')
        except AttributeError as e:
            print("pass")

        #get author
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
        #get abstact
        abstract = html.find('section', class_='abstract').find('p', class_='chapter-para')
        file_handle.write('\n')
        file_handle.write('abstract\n')
        try:
            file_handle.write(abstract.get_text())
            file_handle.write('\n')
        except AttributeError as e:
            print("pass")
        #get key words
        keywords = html.find('div', class_='kwd-group').find_all('a')
        file_handle.write('\n')
        file_handle.write('key words\n')
        for content in keywords:
            try:
                result=content.get_text()
                if result is None:
                    return
                else:
                    file_handle.write(content.get_text())
                    file_handle.write('\n')
            except AttributeError as e:
                continue
        # get article
        article = html.find_all('p', class_='chapter-para')
        file_handle.write('\n')
        k = 0
        for content in article:
            if k == 0:
                k=k+1
                continue
            try:
                result=content.get_text()
                if result is None:
                    return
                else:
                    file_handle.write(content.get_text())
                    file_handle.write('\n')
            except AttributeError as e:
                continue
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

Web = getPage(url)
a=getTitle(Web).strip()
print(a)