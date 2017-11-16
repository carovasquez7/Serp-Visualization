# -*- coding: cp1252 -*-

from core import *
import collections
import os
import json
import csv


#SE TOMA EL JSON DE ENTRADA Y SE PASA AL JSON INTERNO
def GooglePlugin(JSONFilename):
    dic = jsonToDictionary(JSONFilename)
    dicFinal = {}
    dicFinal = obtainAttributesFromJsonGoogle(dic)
    DictionaryToJson(dicFinal, 'internalJsonGoogle')


def obtainAttributesFromJsonGoogle(dic):
    dicAuxinfo = {}
    dicAuxResult = {}
    dicMerge = {}
    dicAuxfinalinfo = {}
    i = 0

    for key in dic:
        if key != 'items':
            dicAuxinfo[key] = dic[key]
        else:
            for elem in dic['items']:
                STR = 'Result' + str(i)
                dicAuxResult[STR] = elem
                i += 1

    dicAuxfinalinfo['info'] = dicAuxinfo
    dicMerge = mergeDictionary(dicAuxfinalinfo, dicAuxResult)
    return dicMerge


def main():
    currentDir = os.getcwd()
    GooglePlugin("GoogleResults.json")


if __name__ == "__main__":
    main()
'''
	

def obtainAttributesFromJsonGoogle1(dic):
	dicAux={}
	i=0
	for elem in dic['items']:
		STR = 'Result'+ str(i)
		dicAux[STR]= elem
		i+=1	
	return dicAux
	#DictionaryToJson(dicAux, 'datagoogle')
	

def obtainAttributesFromJsonGoogle2(dic):
	dicAux1={}
	for key in dic:
		if key != 'items':
			dicAux1[key]=dic[key]
	return dicAux1
	#DictionaryToJson(dicAux, 'datagoogle2')

'''
