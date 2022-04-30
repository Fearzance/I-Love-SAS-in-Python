# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:46:05 2022

@author: alexa
"""
code = """  proc means   data = cars nmiss ;
class model ;
var invoice age ;
run;
"""
def proc_means(code):
    code2 = code.lower()
    word = code.lower().split(";")    
    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Boucle qui permet de récupérer la table 
    for elem in word:
        if elem.startswith("proc"):
            test = " ".join(elem.split())
            test = test.split("=")
            tab = test[-1]
            table = tab.strip()
            if "nmiss" in table:
                table = table.replace("nmiss"," ")
                table = table.strip()
      
            
    #peut être à supprimer (ce bloc)        
    for elem in word:
        if elem.startswith("var"):
            var = elem[3:]
            var_means = var.strip()
            var_means = var_means.split(" ")
            
    for elem in word:
        if elem.startswith("class"):  
            var = elem[5:]
            var_class = var.strip()
    
    
    if "class" in  code2:
        resultat = ""
        resultat += table + ".groupby('" + var_class + "')" +"[['"+ "','".join(var_means)+"']]"+".describe()"
        if "nmiss" in code2:
            resultat += "\n" + "nmiss=" + table + "[['"+ "','".join(var_means)+"']]"+ '.isnull().sum()' + "\n" + "print(nmiss)"
        return(resultat)
    else :
        resultat = ""
        resultat += table +"[['"+ "','".join(var_means)+"']]" + ".describe()"
        if "nmiss" in code2:
            resultat += "\n" + "nmiss=" + table + "[['"+ "','".join(var_means)+"']]"+ '.isnull().sum()' + "\n" + "print(nmiss)"
        return(resultat)

print(proc_means(code))
