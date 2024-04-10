import os

def getListFiles():
    listTable =  os.listdir('GraphsFiles')
    for j in range(len(listTable)):
        for i in range(len(listTable)-1):
            if (listTable[i][6] == "." and listTable[i+1][6] == "."):
                if (listTable[i][5] >= listTable[i+1][5]):
                    greaterValue = listTable[i]
                    listTable[i] = listTable[i+1]
                    listTable[i+1] = greaterValue
            elif ((listTable[i][6] != "." and listTable[i+1][6] == ".") or (listTable[i][6] == "." and listTable[i+1][6] != ".")):
                if (listTable[i][6] != "."):
                    biggestValue = listTable[i]
                    listTable[i] = listTable[i+1]
                    listTable[i+1] = biggestValue
            else:
                if(listTable[i][6] > listTable[i+1][6]):
                    greaterValue = listTable[i]
                    listTable[i] = listTable[i+1]
                    listTable[i+1] = greaterValue
    return listTable