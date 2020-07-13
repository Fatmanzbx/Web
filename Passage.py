import os
def PassageCount(Location,Data):
    codeWrong = []
    result= [0, 0, 0, 0, 0, 0, 0]
    files = os.listdir(Location+'/Passage')
    for file in files:
        try:
            period = int((int(file[:2])+5)/10)
        except ValueError as e:
            print(file)
            continue
        result[period] = result[period]+1
    with open(Data, 'a')as file_handle:
        for n in range(0,7):
            print(result[n])
            print('\n')
    for file in codeWrong:
        print(file)
Location= '/Users/zbx/Desktop/Summerproject/JournalOfMarketingResearch'
Data='/Users/zbx/Desktop/Count.txt'
PassageCount(Location,Data)