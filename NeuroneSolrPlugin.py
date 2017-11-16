# -*- coding: cp1252 -*-

from core import *
import collections
import os
import json
import csv

def GooglePlugin(JSONFilename):
    dic = jsonToDictionary(JSONFilename)
    dicFinal = {}
    #dicFinal = obtainAttributesFromJsonGoogle(dic)
    DictionaryToJson(dicFinal, 'internalJsonNeuroneSolr')
    