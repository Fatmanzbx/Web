import os
Location= '/Users/zbx/Desktop/Summer/JOCR'
Data='/Users/zbx/Desktop/Key'
def getAbstruct(Location,Data):
    codeWrong = []
    files = os.listdir(Location+'/Passage')
    for file in files:
        if file[:2]=='.D':continue
        if int(file[:2])<37: continue
        try:
            lines = open(Location + '/Passage/' + file, 'r').readlines()
        except UnicodeDecodeError as e:
            continue
        a = 1
        for line in lines:
            if line == 'key words\n':
                a = 0
                continue;
            if line == '\n' and a==0: a=2
            if a==1: continue
            if a==2 : break
            with open(Data+'.txt', 'a')as file_handle:
                file_handle.write(line)
    for file in codeWrong:
        print(file)
getAbstruct(Location,Data)