import re
import os
def DiffenrentWord(Location, Data):
    dic = {}
    files = os.listdir(Location + '/Passage')
    for file in files:
        try:
            txt = open(Location+'/Passage/'+file, 'r').read().splitlines()
        except UnicodeDecodeError as e:
            continue
        n = 0
        for line in txt:
            line = re.sub(r'[.?!,""/]', ' ', line)  # 要替换的标点符号，英文字符可能出现的
            line = re.sub(r' - ', ' ', line)  # 替换单独的‘-’
            for word in line.split():
                # 当一行的最后一个字符是-的时候，需要跟下一个英文字符串联起来构成单词
                if word[-1] == '-':
                    m = word[:-1]
                    n = 1
                    break
                if n == 1:
                    word = m + word
                    n = 0
                dic.setdefault(word.lower(), 0)  # 不区分大小写
                dic[word.lower()] += 1
    print(len(dic))

Location= '/Users/zbx/Desktop/Summerproject/JournalOfMarketingResearch'
Data='/Users/zbx/Desktop/Count.txt'
def wordCount(Location,Data):
    codeWrong = []
    result= [0, 0, 0, 0, 0, 0, 0]
    files = os.listdir(Location+'/Passage')
    for file in files:
        try:
            words = sum([len(line.split()) for line in open(Location+'/Passage/'+file, 'r')])
        except UnicodeDecodeError as e:
            codeWrong.append(file)
            continue
        period = int((int(file[:2])+3)/10)
        result[period] = result[period]+words
    with open(Data, 'a')as file_handle:
        for n in range(0,7):
            file_handle.write(str(result[n]))
            file_handle.write('\n')
    for file in codeWrong:
        print(file)
DiffenrentWord(Location,Data)