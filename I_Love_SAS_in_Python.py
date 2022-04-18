# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:13:55 2022

@author: alexa
"""

#=====================================================================================
#Les IMPORTS
#=====================================================================================

import sys 
sys.path.append(r"C:\Users\kevin\Documents\Mémoire\Mémoire M2\2_Programmes")

from Fonctions import tab_out, tab_in
from test import data_drop, data_keep, data_rename, data_where, data_if

code = """    DATA test2                  ;    set table  ;
rename name=nom height=taille weight=poids;
if age<=30 then sexe = 1 ; else if  age = 40 then sexe = 2; else sexe = 3;
run;
"""
def data(code):
#Initialisation de quelques variables
    
    code = code.lower()
    option_if =0
    option_drop = 0
    option_keep = 0
    option_rename = 0
    option_where = 0
    
    
    #Il faudra mettre une fonction def data(code):
    word = code.lower().split(";")
    
    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #On récupère la table d'entrée et de sortie
    sortie_tab = tab_out(code)
    entree_tab = tab_in(code)
    
    #On récupère toutes les options présentent dans le code
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
    
    resultat = resultat.replace("first table", entree_tab)
    resultat = resultat.replace("not first table", sortie_tab)
    return resultat

result = data(code)
print(result)
    
code = """    DATA table5                 ;    set table2 ;
rename name=nom height=taille weight=poids;
keep prix vente moy ;
DROp age sex var3   var4;
where age = "12"     ;
if sex = 'female' then sexe= 'femme' ; else sexe = 'homme';
run;
"""
