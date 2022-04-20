# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:21:56 2022

@author: Alexandre HUANG & Kevin KAMALANATHAN
"""

#------------------------------------------------------------------
# This python program translates the substr function of SAS. 
# An example is shown at the bottom of the program
#------------------------------------------------------------------

import sys
sys.path.append(r"C:\Users\kevin\Documents\Mémoire\Mémoire M2\2_Programmes")

from Fonctions import tab_out, tab_in

def substr(code):
    global entree
    global sortie

    entree = tab_in(code)
    sortie = tab_out(code)
    word = code.lower().split(";")

    #If there is the substr function, it will retrieve the different parameters of the function
    for i in range(0,len(word)):
        word[i] = word[i].strip()
        
        if "substr" in word[i]:
            substr_contains = word[i].split("=")
            new_var = substr_contains[0].strip()
            substr = substr_contains[1].strip()
            substr = substr[7:]
            substr = substr[:-1]
            list_substr = substr.split(",")
            old_var = list_substr[0].strip()
            N = list_substr[1]
            
            if len(list_substr) == 3:
                length = list_substr[2]
            else:
                length = ""
    
   #If in the function substr the position n = 1 then n = 0
    if N == '1' and (entree==sortie):
        resultat = "\n"  
        resultat += sortie + '["' + new_var + '"] = ' + entree + '["' + old_var + '"].str[:'+ length +']'
    
    
    if N == '1' and entree != sortie:
        resultat = ""
        resultat += sortie + '=' + entree + '.copy()\n'
        resultat += sortie + '["' + new_var + '"] = ' + entree + '["' + old_var + '"].str[:'+ length +']'
        
    
    if N != '1' and (entree==sortie):
        N =str(int(N)-1)
        resultat = "\n"  
        resultat += sortie + '["' + new_var + '"] = ' + entree + '["' + old_var + '"].str[' + N +':'+ length +']'
        
    if N != '1' and entree != sortie:
        N =str(int(N)-1)
        resultat = ""
        resultat += sortie + '=' + entree + '.copy()\n'
        resultat += sortie + '["' + new_var + '"] = ' + entree + '["' + old_var + '"].str[' + N + ':' + length +']'

    return resultat

#EXAMPLE
print(substr("""DATA table1;set table2;
             new_name = substr(prénom,5,8);
             run;"""))