# -*- coding: utf-8 -*-
"""
Created on Wed July 20 19:21:56 2022

@author: Alexandre HUANG & Kevin KAMALANATHAN

"""
#-------------------------------------------------------------------------------------------#
# This program includes the different functions that allow you to identify the different    #
# declarations of a DATA step.                                                              #
# It also includes the "TRANSLATOR" function which allows the DATA step to be translated.   #
#-------------------------------------------------------------------------------------------#

import re
import pandas as pd 
nba = pd. read_csv(r"C:\Users\kevin\Documents\Mémoire\Mémoire M2\NBA_list_new.csv")

#---------------------------------#
#           STATEMENTS            #
#---------------------------------#

STATEMENTS = [
    "keep",
    "drop",
    "rename"
    ]

#-------KEEP
def keep(elem):
    var = elem[5:]
    resultat = t_out + "=" + t_in2 +"[['" + "','".join(var.split()) + "']]"
    return resultat

#-------DROP
def drop(elem):
    var = elem[5:]
    resultat = t_out + "=" + t_in2 +".drop(columns=['" + "','".join(var.split()) + "'])"
    return resultat

#-------RENAME
def rename(elem):
    elem = elem.replace(" = ","=")
    elem = elem.replace(" =","=")
    elem = elem.replace("= ","=")
    var = elem[7:]
    resultat = t_out + "#" + t_in2 +".rename(columns:{'" + "','".join(var.split()) + "'})"
    resultat = resultat.replace("#","=")
    return resultat

#---------------------------------#
#         SAS FUNCTIONS           #
#---------------------------------#

#-------SUBSTR
def substr(elem):
    substr_contains = elem.split("=")
    new_var = substr_contains[0].strip()
    substr = substr_contains[1].strip()
    substr = re.split("[(),]",substr)
    old_var = substr[1].strip()
    N = substr[2].strip()
    if len(substr) > 3:
        length = substr[3].strip()
    else:
        length = ""
    if N == '1':
        resultat = t_out + "['" + new_var + "'] = " + t_in2 + "['" + old_var + "'].str[:"+ length +"]"
        return resultat
    if N != '1':
        N =str(int(N)-1)
        resultat = t_out + "['" + new_var + "'] = " + t_in2 + "['" + old_var + "'].str[" + N +":"+ length +"]"
        return resultat

#-------LOWCASE
def lowcase(elem):
    lowcase_contains = elem.split("=")
    new_var = lowcase_contains[0].strip()
    lowcase = lowcase_contains[1].strip()
    lowcase = re.split("[()]",lowcase)
    old_var = lowcase[1].strip()
    resultat = t_out + "['" + new_var + "'] = " + t_in2 + "['" + old_var + "'].str.lower()"
    return resultat

#-------UPCASE
def upcase(elem):
    upcase_contains = elem.split("=")
    new_var = upcase_contains[0].strip()
    upcase = upcase_contains[1].strip()
    upcase = re.split("[()]",upcase)
    old_var = upcase[1].strip()
    resultat = t_out + "['" + new_var + "'] = " + t_in2 + "['" + old_var + "'].str.upper()"
    return resultat

SAS_FUNCT = {
    "substr":substr,
    "lowcase":lowcase,
    "upcase":upcase
    }

#---------------------------------#
#           TRANSLATOR            #
#---------------------------------#
def translator(code):    
    global t_in2
    global t_out
    global elem2
    
    resultat=''
    flag=0
    word = code.split(";")
    
    #Separate the code into list 
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Loop that retrieves the output table
    for elem in word:
        if elem.lower().startswith("data"):
            t_out = elem[5:].strip()
          
    #Loop that retrieves the input table
    for elem in word:
        if elem.lower().startswith("set"):
            t_in = elem[4:].strip()
            
    for elem in word:
        elem2 = elem.lower()
        for stat in STATEMENTS:
            if elem2.startswith(stat):
                if flag == 0:
                    flag = 1
                    t_in2 = t_in
                else:
                    t_in2 = t_out
                                    
        if elem.lower().startswith("keep"):
            resultat+=keep(elem) + "\n"
        if elem.lower().startswith("drop"):
            resultat+=drop(elem) + "\n"
        if elem.lower().startswith("rename"):
            resultat+=rename(elem) + "\n"
            
        for key, val in SAS_FUNCT.items():
            if key in elem2:
                if flag == 0:
                    flag = 1
                    t_in2 = t_in
                else:
                    t_in2 = t_out
                resultat+=val(elem) + "\n"
        
    return resultat