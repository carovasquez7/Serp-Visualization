# -*- coding: cp1252 -*-

from core import *
import collections
import os
import json
import csv


def FeatureExtraction(JSONFilename):
    dic = jsonToDictionary(JSONFilename)
    #print dic
    #print dic['attribute']
    #getValueinDic(dic, 'description')
    dicFinal = countWordDescription(dic,'numberWord')
    DictionaryToJson(dicFinal)
   
## PLUGINS Count Words

def countWords(word):
    NumberWord = len(word.split())
    return NumberWord
    
#get VALUE in DIC (Obtiene los valores de la llave que se le entrega.)
def getValueinDic(dic, query):
    keylist = []
    dicDesc={}
    for key in dic:
        if isElementaResults(key):
            keylist.append(key)
    
    for elem in keylist:
        dicDesc[elem] = dic[elem][query]
    
    return dicDesc 

    
#get Description of SERP (Obtiene los valores de la llave Description)
def getDescriptionFromSERPS(dic):    
    keylist = []
    dicDesc = collections.defaultdict(dict)
    #dicDesc={}
    for key in dic: #
        if isElementaResults(key):
            keylist.append(key)
        
    for elem in keylist:
        dicDesc[elem]['description']= dic[elem]['description']
    
    return dicDesc

# Count word of Description (Calcula el numero de palabras del atributo Description)
def countWordDescription(dic,name,queryname):
    keylist = []
    dicCount={}
    dicAux={}
    dicAux = makeDicAux(dic)
    

    
    for key in dic:
        if isElementaResults(key):
            keylist.append(key)
    for elem in keylist:
        count = countWords(dic[elem][queryname])
        dicCount = insertNewKeytoDic(dic,name,count,elem)

    listAtr = []
    for elemAtrb in dicAux['attribute']:
        listAtr.append(elemAtrb)
    listAtr.append(name)        
    dicCount['info']=dicAux['info']    
    dicCount['attribute']=listAtr
    
    #print dicCount
    return dicCount

    #print dicAux
    #return dicAux

    
    



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
    FeatureExtraction("SERP.json")

if __name__ == "__main__":
    main()

  

## PLUGINS Ranking




