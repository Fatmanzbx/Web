
import numpy
import os
Location='/Users/zbx/Desktop/Summer/MS/'
files = os.listdir(Location+'Passage2')
number = numpy.zeros(500)
wrong = []
for file in files:
    try:
        volumn = int(file[5:7])
        issue = int(file[8])
    except ValueError as e:
        continue
    if volumn == 17 or volumn == 18:
        number[10 * volumn + issue]+=1
        try:
            lines = open(Location + '/Passage2/' + file, 'r').readlines()
        except UnicodeDecodeError as e:
            wrong.append(file)
            continue
    else: continue
    b = 0
    k = 0
    with open('/Users/zbx/Desktop/Summer/MS/Passage/' + str(volumn) + '#issue#'
        + str(issue) + 'Passage' +str(number[10*volumn+issue]) + '.txt','a')as file_handle:
        for line in lines:
            if line.find('http://www.informs.org')>-1:
                b = 1
                continue
            if b == 1 and str.isalnum(line[0]):
                k = 1
            if k == 1:
                file_handle.write(line)
                file_handle.write('\n')
with open('/Users/zbx/Desktop/Demo.txt', 'r') as error:
    for file in wrong:
        error.write(file+'\n')




