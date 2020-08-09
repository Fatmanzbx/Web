import os
import numpy
Location= '/Users/zbx/Desktop/Summer/JOCR'
Data='/Users/zbx/Desktop/Count'
def wordCount(Location):
    codeWrong = []
    result= [0, 0, 0, 0, 0]
    files = os.listdir(Location+'/Passage')
    for file in files:
        try:
            words = sum([len(line.split()) for line in open(Location+'/Passage/'+file, 'r')])
        except UnicodeDecodeError as e:
            codeWrong.append(file)
            continue
        period = int((int(file[:2])-3)/5)-4
        result[period] = result[period]+words
    return result


def passageCount(Location):
    total=0
    files = os.listdir(Location + '/Links')
    codeWrong = []
    for file in files:
        try:
            a= int(file[1:-12])
            if a > 26: continue
            for line in open(Location+'/Links/'+file, 'r'):
                total+=1
        except TypeError and ValueError as e:
            codeWrong.append(file)
            continue
    print(total)

total=wordCount(Location)
for i in range (1,4):
    if i == 1: key = 'anova'
    if i == 2: key = 'scanner'
    if i == 3: key = 'mediation'
    result = numpy.zeros(5)
    for j in range(0,5):
        for line in open('/Users/zbx/Desktop/Count'+str(j)+'.txt', 'r'):
            if line.find(key)>-1:
                for k in range(1,20):
                    if str.isdigit(line[k]):
                        result[j] = float(line[k:k+7])/float(total[j])
                        break
                break
    print(result)


