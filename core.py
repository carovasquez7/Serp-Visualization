# -*- coding: cp1252 -*-
import os
import json
import csv

d1 = {u'SERP3': 23, u'SERP2': 12, u'SERP1': 27, u'SERP4': 0}


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
    attr =  list(set(lista))
    return attr        

def DictionaryToJson(dic):
    print dic
    with open ('data.json', 'w') as fp:
        json.dump(dic, fp)

def isElementaSERP(string):
    if "SERP" in string:
        return True
    else:
        return False

def insertNewKeytoDic(dic,key,value,elem):
    dicAux = {}    
    dic[elem][key] = value
    return dic
    

def makeDicAux(dic):
    dicAux= {}
    dicAux['info'] = dic['info']
    dicAux['attribute'] = dic['attribute']

    return dicAux


#sin uso
def mergeDictionary (dic1, dic2):
    ds = [dic1, dic2]
    d = {}
    for k in d1.iterkeys():
        d[k] = tuple(d[k] for d in ds)
    return d



            
    
    
