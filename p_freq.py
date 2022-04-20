# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:35:11 2022

@author: alexa
"""
code = """  proc freq   data = class ;
table sex  ;
run;
"""
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
        
for elem in word:
    if elem.startswith("table"):
        var = elem[5:]
        var_freq = var.strip()

resultat1 = ""
resultat1 += "datax =" + table +"['" +var_freq +"']" +".value_counts(dropna = False)" +"\n" + "datay = pandas.DataFrame({'"+var_freq + "': datax.index, 'Frequency': datax.values,'Percent': ((datax.values/datax.values.sum())*100).round(2),'Cumulative Frequency': datax.values.cumsum(),'Cumulative Percent': ((datax.values.cumsum()/datax.values.sum())*100).round(2)})"
print(resultat1)
