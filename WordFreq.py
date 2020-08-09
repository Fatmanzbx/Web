import re
import os
Uselesslist=[ 'an', 'the', 'this', 'that', 'is', 'are', 'be', 'then', 'so', 'and', 'just', 'all',
             'in', 'on', 'at', 'by', 'to', 'of', 'for', 'with', 'from', 'after', 'until', 'no',
             'before', 'toward', 'as', 'or', 'if', 'because', 'which', 'it', 'we', 'have', 'was','each',
             'their', 'they', 'were', 'these', 'has', 'its', 'but', 'also', 'some', 'when', 'not','lot',
             'many', 'much', 'often', 'would', 'too', 'more', 'without','them','than','can','will','been']

Location= '/Users/zbx/Desktop/Summer/JOCR'
Data='/Users/zbx/Desktop/Count'
def rank(words):
    if len(words) < 2: return words
    words1 = rank(words[0:int(len(words)/2)])
    words2 = rank(words[int(len(words)/2): len(words)])
    result=[]
    i=0
    j=0
    k=0
    while True:
        a=dic[words1[i]]
        b=dic[words2[j]]
        if a>b:
            result.append(words1[i])
            i+=1
        else:
            result.append(words2[j])
            j+=1
        if i >= len(words1):
            k=2
            break
        if j >= len(words2):
            k=1
            break
    if k==1:
        for t in range(i,len(words1)):
            result.append(words1[t])
    if k==2:
        for t in range(j,len(words2)):
            result.append(words2[t])
    return result

for i in range(0,5):
    words = []
    dic = {}
    files = os.listdir(Location + '/Passage')
    for file in files:
        if file[:2] == '.D': continue
        n = int(file[:2])
        if n < (i+4)*5+3 or n > (i+4)*5+7: continue
        try:
            txt = open(Location+'/Passage/'+file, 'r').read().splitlines()
        except UnicodeDecodeError as e:
            continue
        n = 0
        for line in txt:
            line = re.sub(r'[.:“;(\"+”=\')?!,""/]', ' ', line)  # 要替换的标点符号，英文字符可能出现的
            line = re.sub(r' - ', ' ', line)  # 替换单独的‘-’
            for word in line.split():
                if word[-1] == '-':
                    m = word[:-1]
                    n = 1
                    break
                if n == 1:
                    word = m + word
                    n = 0
                if len(word.lower()) > 1:
                    try:
                        dic[word.lower()]+=1
                    except KeyError as e:
                        dic.setdefault(word.lower(), 0)  # 不区分大小写
                        dic[word.lower()] += 1
                        words.append(word.lower())
    for word in Uselesslist:
            words.remove(word)
    wordfre = rank(words)
    print(len(wordfre))
    with open(Data+str(i)+'.txt', 'a')as file_handle:
        for word in wordfre:
            n = int(len(word)/8)
            file_handle.write(str(word))
            for i in range(1,4-n):
                file_handle.write('\t')
            file_handle.write('\t'+str(dic[word]))
            file_handle.write('\n')