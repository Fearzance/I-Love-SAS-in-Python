# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:21:56 2022

@author: Alexandre HUANG & Kevin KAMALANATHAN
"""
#-------------------------------------------------------------------------------------
#This program includes the data function which allows to translate a data step, 
#it can translate DROP, KEEP, WHERE, IF ELSE IF ELSE and RENAME statements.
#-------------------------------------------------------------------------------------


#=====================================================================================
#Les IMPORTS
#=====================================================================================

import sys 
sys.path.append(r"C:\Users\kevin\Documents\Mémoire\Mémoire M2\2_Programmes")

from Fonctions import tab_out, tab_in
from options_data import data_drop, data_keep, data_rename, data_where, data_if


def data(code):
#Initialization of some variables
    
    code = code.lower()
    option_if =0
    option_drop = 0
    option_keep = 0
    option_rename = 0
    option_where = 0
    
    
    word = code.lower().split(";")
    
    #Remove spaces for each element of words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #We get the input and output table
    sortie_tab = tab_out(code)
    entree_tab = tab_in(code)
    
    #We retrieve all the options present in the code
    if "drop" in code:
        option_drop = 1
    
    
    if "keep" in code:
        option_keep = 1
    
    
    if "rename" in code:
        option_rename = 1
    
    
    if "where" in code:
        option_where =1
        
    if "if" in code:
        option_if =1
    
    
    if option_drop == 1:
        if "resultat" in locals():
            resultat = resultat + "\n" + data_drop(2,code)
        else:
            resultat = data_drop(1,code) 
            
    if option_keep ==1:
        if "resultat" in locals():
            resultat = resultat + "\n" + data_keep(2,code)
        else:
            resultat = data_keep(1,code)
    
            
    if option_where ==1:
        if "resultat" in locals():
            resultat = resultat + "\n" + data_where(2,code)
        else:
            resultat = data_where(1,code)
    
            
    if option_rename ==1:
        if "resultat" in locals():
            resultat = resultat + "\n" + data_rename(2,code)
        else:
            resultat = data_rename(1,code)
    
    if option_if ==1:
        if "resultat" in locals():
            resultat = resultat + "\n" + data_if(2,code)
        else:
            resultat = data_if(1,code)
    
    resultat = resultat.replace("first", entree_tab)
    resultat = resultat.replace("last", sortie_tab)
    return resultat

#EXAMPLE
    
code = """    DATA table5                 ;    set table2 ;
rename name=nom height=taille weight=poids;
keep prix vente moy ;
DROp age sex var3   var4;
where age = "12"     ;
if sex = 'female' then sexe= 'femme' ; else sexe = 'homme';
run;
"""
result = data(code)
print(result)