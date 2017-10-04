# -*- coding: cp1252 -*-

from core import *
import os
import json
import csv

def processingSerps(JSONFilename):
    dic = jsonToDictionary(JSONFilename)
    attributes = obtainAttributesFromJson(dic)
    dic['attribute']= attributes
    DictionaryToJson(dic)

    
def main():
    currentDir = os.getcwd()
    for filename in os.listdir(currentDir):
        if ".json" in filename:
            processingSerps(filename)
        else:
            print "[INFO] " + str(filename) + " cant be process because is not a .json"

if __name__ == "__main__":
    main()

