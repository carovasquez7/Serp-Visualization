from core import *
import collections
import os
import json
import csv


def FeatureExtraction(JSONFilename):
    dic = jsonToDictionary(JSONFilename)
    print dic
    #print dic['attribute']
    #getValueinDic(dic, 'description')
    dicFinal = countWordDescription(dic,'numberWord')
    DictionaryToJson(dicFinal)
   


def countWordDescription(dic,name):
    keylist = []
    dicCount={}
    dicAux={}
    dicAux = makeDicAux(dic)
    
    print dicAux
    '''
    for key in dic:
        if isElementaSERP(key):
            keylist.append(key)
    for elem in keylist:
        count = countWords(dic[elem]['description'])
        dicCount = insertNewKeytoDic(dic,name,count,elem)

    listAtr = []
    for elemAtrb in dicAux['attribute']:
        listAtr.append(elemAtrb)
    listAtr.append(name)        
    dicCount['info']=dicAux['info']    
    dicCount['attribute']=listAtr
    
    return dicCount
'''


def main():
   currentDir = os.getcwd()
   for filename in os.listdir(currentDir):
        if ".json" in filename:
            FeatureExtraction(filename)
        else:
            print "[INFO] " + str(filename) + " cant be process because is not a .json\n"

if __name__ == "__main__":
    main()
