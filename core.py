# -*- coding: cp1252 -*-
import os
import json
import csv


RESULTS_GLOBAL_NAME = 'Result'
lista = []

def jsonToDictionary(filename):
    with open(filename, 'r') as fp:
        dic = json.load(fp)
    return dic

def JsonToOrderDictionary(filename):
    with open(filename, 'r') as fp:
        dic = json.load(fp, object_pairs_hook=collections.OrderDict)
    return dic

def obtainAttributesFromJson(dic):
    for key in dic:
        for key_nested in dic[key]:
            lista.append(key_nested)  
    #print set(lista)
    attr =  list(set(lista))
    return attr        

def DictionaryToJson(dic, nameFile):
    #print dic
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, nameFile+'.json')
    #newstr = nameFile + ".json"
    with open (json_url, 'w') as fp:
        json.dump(dic, fp)


def isElementaResults(string):
    if RESULTS_GLOBAL_NAME in string:
        return True
    else:
        return False

def insertNewKeytoDic(dic,key,value,elem):
    dicAux = {}    
    dic[elem][key] = value
    return dic
    

def makeDicAux(dic):
    dicAux= {}
    dic['attribute'] = obtainAttributesFromJson(dic)
    dicAux['info'] = dic['info']
    dicAux['attribute'] = dic['attribute']
    return dicAux

def mergeDictionary(dic1, dic2):
    dicAux = dic1.copy()
    dicAux.update(dic2)
    return dicAux


def formatJsonToD3(dic):
    listdic = []
    FinalDic = {}

    for key in dic:
        if key != "info" and key !="attribute":
            listdic.append(dic[key])

    FinalDic["Result"] = listdic
    FinalDic["info"] = dic["info"]
    FinalDic["attribute"] = dic["attribute"]
    return FinalDic
            
            
    
    
