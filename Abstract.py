import os
Location= '/Users/zbx/Desktop/Summerproject/JournalOfMarketing'
Data='/Users/zbx/Desktop/Key'
def getAbstruct(Location,Data):
    codeWrong = []
    files = os.listdir(Location+'/Passage')
    for file in files:
        try:
            lines = open(Location + '/Passage/' + file, 'r').readlines()
        except UnicodeDecodeError as e:
            continue
        a = 1
        for line in lines:
            if line == 'abstract\n': continue;
            if line == 'key words\n': continue;
            with open(Data+'.txt', 'a')as file_handle:
                file_handle.write(line)
    for file in codeWrong:
        print(file)
getAbstruct(Location,Data)