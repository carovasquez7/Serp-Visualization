# -*- coding: cp1252 -*-
import os
import json
import csv


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
