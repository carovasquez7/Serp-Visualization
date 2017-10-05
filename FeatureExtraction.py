# -*- coding: cp1252 -*-

from core import *
import collections
import os
import json
import csv

def FeatureExtraction(JSONFilename):
    dic = jsonToDictionary(JSONFilename)
    #print dic['attribute']
    #AssignedID(dic)
    getDescriptionFromSERPS(dic)
    #getValueinDic(dic, 'description')
    #countWordDescription(dic)
    

## PLUGINS Count Words

def countWords(word):
    NumberWord = len(word.split())
    return NumberWord
    
#get VALUE in DIC
def getValueinDic(dic, query):
    keylist = []
    dicDesc={}
    for key in dic:
        if isElementaSERP(key):
            keylist.append(key)
    #print keylist

    for elem in keylist:
        dicDesc[elem] = dic[elem][query]
    #print dicDesc
    return dicDesc 

    
#get Description of SERP
def getDescriptionFromSERPS(dic):    
    keylist = []
    dicDesc = collections.defaultdict(dict)
    #dicDesc={}
    for key in dic: #
        if isElementaSERP(key):
            keylist.append(key)
    #print keylist
    
    for elem in keylist:
        dicDesc[elem]['description']= dic[elem]['description']
    print dicDesc
    return dicDesc

def countWordDescription(dic):
    keylist = []
    dicCount={}
    for key in dic:
        if isElementaSERP(key):
            keylist.append(key)
    for elem in keylist:
        count = countWords(dic[elem]['description'])
        dicCount[elem] = count

    print dicCount        
    return dicCount

    
    



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
"""    
def CountWordsDescription(dic):
    for key in dic:
        if key =='info':
            pass
        else:
            for key_atr in dic[key]:
                print dic[key_atr]
                
 """        

'''
def findWordsDescription(dic):    
    keylist = []
    for key in dic:
        if isElementaSERP(key):
            keylist.append(key)
    print keylist

    for elem in keylist:
        print dic[elem]['description']


 '''   
    
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




