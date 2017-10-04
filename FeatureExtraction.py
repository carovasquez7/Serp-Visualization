# -*- coding: cp1252 -*-

from core import *
import os
import json
import csv

def FeatureExtraction(JSONFilename):
    dic = jsonToDictionary(JSONFilename)
    #print dic['attribute']
    #AssignedID(dic)
    CountWordsDescription(dic)
    
## PLUGINS Set correlative ID
'''
def AssignedID(dic):
    countID = 0
    for key in dic:
        if key =='info':
            pass
        else:
            countID+=1
            dic['id'] = countID
    
     #   dic[key]['id']=countID
'''


## PLUGINS Count Words

def CountWord(string):
    numberWord= len(string.split())
    return numberWord
    
    
"""    
def CountWordsDescription(dic):
    for key in dic:
        if key =='info':
            pass
        else:
            for key_atr in dic[key]:
                print dic[key_atr]
                
 """   

def CountWordsDescription(dic):
    #print dic['SERP3']['description']
    keylist = []
    for key in dic:
        keylist.append(key)
    #print keylist

    for elem in keylist:
        print dic[elem]['description']

        #for keya in dic[key]:
        #    print dic.get('description')
    
    
    
    
def main():
    currentDir = os.getcwd()
    for filename in os.listdir(currentDir):
        if ".json" in filename:
            FeatureExtraction(filename)
        else:
            print "[INFO] " + str(filename) + " cant be process because is not a .json"

if __name__ == "__main__":
    main()

  

## PLUGINS Ranking




