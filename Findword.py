import os
import numpy
Location= '/Users/zbx/Desktop/Summer/JOM'
Data='/Users/zbx/Desktop/Count'
def phraseCount(v0,v1,str):
    k=0
    codeWrong = []
    files = os.listdir(Location + '/Passage')
    for file in files:
        if file[:2] == '.D': continue
        n = int(file[:2])
        if n < v0 or n > v1: continue
        fopen = open(Location + '/Passage/'+file)
        try:
            lines = fopen.readlines()
        except UnicodeDecodeError as e:
            codeWrong.append(file)
            continue
        for line in lines:
            line=line.lower()
            while True:
                if line.find(str)>-1:
                    tag = line.find(str) + len(str)
                    line=line[tag:]
                    k+=1
                else: break
    return k
#print(phraseCount(70,80,'big data'))
a = 0
str='stop'
fopen = open('/Users/zbx/Desktop/README.txt')
try:
    lines = fopen.readlines()
except UnicodeDecodeError as e:
    print('fuck')
for line in lines:
    line=line.lower()
    while True:
        if line.find(str)>-1:
            tag = line.find(str) + len(str)
            line=line[tag:]
            a+=1
        else: break
print(a)