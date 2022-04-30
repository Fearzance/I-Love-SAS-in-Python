# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:35:11 2022

@author: alexa
"""
code = """  proc freq   data = class ;
table sex*age  ;
run;
"""

def proc_freq(code):
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
      
            
    #Récupère les variables concernées par le freq        
    for elem in word:
        if elem.startswith("table"):
            var = elem[5:]
            var_freq = var.strip()
          
    #Table de contingence?
    if "*" not  in var_freq:
        resultat1 = ""
        resultat1 += "datax =" + table +"['" +var_freq +"']" +".value_counts(dropna = False)" +"\n" + "datay = pandas.DataFrame({'"+var_freq + "': datax.index, 'Frequency': datax.values,'Percent': ((datax.values/datax.values.sum())*100).round(2),'Cumulative Frequency': datax.values.cumsum(),'Cumulative Percent': ((datax.values.cumsum()/datax.values.sum())*100).round(2)})"
        return(resultat1)
        
    else:
        cross_var = var_freq.split("*")
        resultat2 = ""
        resultat2 += """
def frequency(ds, vars):
    if len(vars) > 1:
        c1 = ds[vars[0]]
        c2 = []
        for i in range(1,len(vars)):
            c2.append(ds[vars[i]])
        dfs = []
        dfs.append(pd.crosstab(c1,c2).unstack().reset_index().rename(columns={0:'Count'}))
        dfs.append(pd.crosstab(c1,c2, normalize='all').unstack().reset_index().rename(columns={0:'Percent'}))
        dfs.append(pd.crosstab(c1,c2, normalize='columns').unstack().reset_index().rename(columns={0:'Column Percent'}))
        dfs.append(pd.crosstab(c1,c2, normalize='index').unstack().reset_index().rename(columns={0:'Row Percent'}))
        dfs = [df.set_index(vars) for df in dfs]
        df = dfs[0].join(dfs[1:]).reset_index()
        return df
            """
        resultat2 += "\n" +"frequency(" + table + ",['"+ "','".join(cross_var) + "'])"    
        return(resultat2)
    
print(proc_freq(code))



