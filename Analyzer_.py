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

#---------------------------------#
#           STATEMENTS            #
#---------------------------------#

STATEMENTS = [
    "keep",
    "drop",
    "rename",
    "where",
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
    var2 = ''
    var = elem[7:]
    for i in var.split():
        var2 += ' ' + i
    var2 = re.sub(r"= | = | =|=", "':'", var2)
    resultat = t_out + "=" + t_in2 +".rename(columns:{'" + "','".join(var2.split()) + "'})"
    return resultat

#-------WHERE
def where(elem,i):
    var = elem[i:]
    var = re.sub(" or | OR | oR | Or ", " Ӫ ", var)
    var = re.sub(" and | AND | And | ANd | aND | aNd | AnD "," Ā ", var)
    var = re.sub("<=| le | LE | Le | lE ", " Ԗ ", var)
    var = re.sub(">=| ge | GE | Ge | gE ", " Ԡ ", var)
    var = re.sub("<| lt | LT | Lt | lT ", " Ī ", var)
    var = re.sub(">| gt | GT | Gt | gT ", " Ŝ ", var)
    var = re.sub(" ne | NE | Ne | eN ", " Đ ", var)
    var = re.sub("=| eq | EQ | eQ | Eq "," Ē ", var)
    var = re.sub(" in | IN | In | iN ", "'].isin", var)
    var2 = re.split(" ", var)  
            
    for i in range(0,len(var2)):
        var2[i] = re.sub("Ӫ", ") | (" + t_in2 + "['", var2[i])
        var2[i] = re.sub("Ā", ") & (" + t_in2 + "['", var2[i])
        var2[i] = re.sub("Ē", "']==", var2[i])
        var2[i] = re.sub("Ԗ", "']<=", var2[i])
        var2[i] = re.sub("Ԡ", "']>=", var2[i])
        var2[i] = re.sub("Ŝ", "']>", var2[i])
        var2[i] = re.sub("Ī", "']<", var2[i])
        var2[i] = re.sub("Đ", "']!=", var2[i])  
            
    if not " Ӫ " in var and not " Ā " in var:
        resultat = t_out + "=" + t_in2 + "[" + t_in2 + "['" +  "".join(var2) + "]"
    else:
        resultat = t_out + "=" + t_in2 + "[(" + t_in2 + "['" +  "".join(var2) + ")]"

    resultat = resultat.replace(t_in2 + "['(","(" + t_in2 + "['")
    return resultat



#---------------------------------#
#         SAS FUNCTIONS           #
#---------------------------------#

#-------SUBSTR
def substr(elem):
    substr_contains = elem.split("=")
    new_var = substr_contains[0].strip()
    substr = substr_contains[1].strip()
    substr = re.split("[(),]", substr)
    old_var = substr[1].strip()
    n = substr[2].strip()
    if len(substr) > 3:
        length = substr[3].strip()
    else:
        length = ""
    if n == '1':
        resultat = t_out + "['" + new_var + "']=" + t_in2 + "['" + old_var + "'].str[:"+ length +"]"
    elif n != '1':
        n =str(int(n)-1)
        resultat = t_out + "['" + new_var + "']=" + t_in2 + "['" + old_var + "'].str[" + n +":"+ length +"]"
    return resultat

#-------UPCASE and LOWCASE
def up_low(elem):
    up_low_contains = elem.split("=")
    new_var = up_low_contains[0].strip()
    up_low = up_low_contains[1].strip()
    up_low = re.split("[()]", up_low)
    old_var = up_low[1].strip()
    resultat = t_out + "['" + new_var + "']=" + t_in2 + "['" + old_var + "']"
    if "lowcase(" in elem2: 
        resultat += ".str.lower()"
    elif "upcase(" in elem2:
        resultat +=  ".str.upper()" 
    return resultat

#-------PUT and INPUT
def put(elem):
    put_contains = elem.split("=")
    new_var = put_contains[0].strip()
    put = put_contains[1].strip()
    put = re.split("[()]",put)
    old_var = put[1].strip()
    old_var = old_var.split(",")
    old_var = old_var[0]
    resultat = ""
    resultat += t_out + "['" + new_var + "']=" +t_in2+"['" + old_var + "'].astype(str)"
    return resultat

def in_put(elem):
    put_contains = elem.split("=")
    new_var = put_contains[0].strip()
    put = put_contains[1].strip()
    put = re.split("[()]",put)
    old_var = put[1].strip()
    old_var = old_var.split(",")
    old_var = old_var[0]
    resultat = ""
    resultat += t_out + "['" + new_var + "']=" +t_in2+"['" + old_var + "'].astype(int)"
    return resultat

SAS_FUNCT = {
    "substr(":substr,
    "lowcase(":up_low,
    "upcase(":up_low ,
    "put(":put,
    "þ": in_put
    }


#-------PROC MEANS
def proc_means(elem):
    global resultat

    if var_class:
        
        resultat = table + ".groupby('" + var_class + "')" +"[['"+ "','".join(var_means)+"']]"+".describe()"
        if "nmiss" in elem:
            resultat += "\n" + "nmiss=" + table + "[['"+ "','".join(var_means)+"']]"+ '.isnull().sum()' + "\n" + "print(nmiss)"
        return resultat
    else :
        
        resultat = table +"[['"+ "','".join(var_means)+"']]" + ".describe()"
        if "nmiss" in elem.lower():
            resultat += "\n" + "nmiss=" + table + "[['"+ "','".join(var_means)+"']]"+ '.isnull().sum()' + "\n" + "print(nmiss)"
        return resultat
             
#-------PROC FREQ
def proc_freq(elem):
    global resultat
    
    if "*" not  in var_freq:
        
        resultat = "datax =" + table +"['" +var_freq +"']" +".value_counts(dropna = False)" +"\n" + "datay = pandas.DataFrame({'"+var_freq + "': datax.index, 'Frequency': datax.values,'Percent': ((datax.values/datax.values.sum())*100).round(2),'Cumulative Frequency': datax.values.cumsum(),'Cumulative Percent': ((datax.values.cumsum()/datax.values.sum())*100).round(2)})"
        return resultat
        
    else:
        cross_var = var_freq.split("*")
        resultat = """
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
        resultat += "\n" +"frequency(" + table + ",['"+ "','".join(cross_var) + "'])" 
        return resultat
    
#---------------------------------#
#           TRANSLATOR            #
#---------------------------------#
def translator(code): 
    global t_in
    global t_in2
    global t_out
    global elem2
    
    #Input table for PROC STEP
    global table
    global var_means
    global var_class
    
    global var_freq    
    
    resultat = ''
    flag = 0
    code = code.replace("input","þ")
    word = code.split(";")
    
    #Separate the code into list 
    for i in range(0,len(word)):
        word[i] = word[i].strip()
    
    #Loop that retrieves the output table
    t_out = ""
    for elem in word:
        if elem.lower().startswith("data"):
            t_out = elem[5:].strip()
          
    #Loop that retrieves the input table
    t_in = ""
    for elem in word:
        if elem.lower().startswith("set"):
            t_in = elem[4:].strip()
     
           
    if t_out != t_in:
        resultat = t_out + "=" + t_in + ".copy()\n"
        flag=1
    
    for elem in word:
        elem2 = elem.lower()
        #Show python code for each statements
        for stat in STATEMENTS:
            if elem2.startswith(stat):
                #
                if flag == 0:
                    flag = 1
                    t_in2 = t_in
                else:
                    t_in2 = t_out
                    
        if elem2.startswith("keep"):
            resultat += keep(elem) + "\n"
        if elem2.startswith("drop"):
            resultat += drop(elem) + "\n"
        if elem2.startswith("rename"):
            resultat += rename(elem) + "\n"
        if elem2.startswith("where"):
            resultat += where(elem,6) + "\n"

        #Show python code for each functions
        for key, val in SAS_FUNCT.items():
            if key in elem2:
                if flag == 0:
                    flag = 1
                    t_in2 = t_in
                else:
                    t_in2 = t_out 
                    
                resultat += val(elem) + "\n"
   
    #For PROC STEP
    #Name of table
    for elem in word:
        if elem.startswith("proc"):
            name_table = " ".join(elem.split())
            name_table = name_table.split("=")
            name_table = name_table[-1]
            table = name_table.strip()
            if "nmiss" in table:
                table = table.replace("nmiss"," ")
                table = table.strip()
        #List of var for proc means
        for elem in word:
            if elem.startswith("var"):
                var = elem[3:]
                var_means = var.strip()
                var_means = var_means.split(" ")
        #List of var for option class        
        for elem in word:
            if elem.startswith("class"):  
                var = elem[5:]
                var_class = var.strip()
            else:
                var_class = []
                
        #List of var for proc freq        
        for elem in word:
            if elem.startswith("table"):
                var = elem[5:]
                var_freq = var.strip()
                
    #Add in result    
    for elem in word:
        if elem.startswith("proc means"):
            resultat += proc_means(elem) + "\n"
   
    for elem in word:
        if elem.startswith("proc freq"):
            resultat += proc_freq(elem) + "\n"
            
    return resultat

print(translator(""" 
                 proc means data = yoi ;
                 var age taille ;
                 run ;
                 
                 """))
                 
