# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:59:11 2022

@author: kevin
"""

import re

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
        var2[i] = re.sub("Ӫ", ") | (" + t_in + "['", var2[i])
        var2[i] = re.sub("Ā", ") & (" + t_in + "['", var2[i])
        var2[i] = re.sub("Ē", "']==", var2[i])
        var2[i] = re.sub("Ԗ", "']<=", var2[i])
        var2[i] = re.sub("Ԡ", "']>=", var2[i])
        var2[i] = re.sub("Ŝ", "']>", var2[i])
        var2[i] = re.sub("Ī", "']<", var2[i])
        var2[i] = re.sub("Đ", "']!=", var2[i])  
            
    if not " Ӫ " in var and not " Ā " in var:
        resultat = t_out + "=" + t_in + "[" + t_in + "['" +  "".join(var2) + "]"
    else:
        resultat = t_out + "=" + t_in + "[(" + t_in + "['" +  "".join(var2) + ")]"

    resultat = resultat.replace(t_in + "['(","(" + t_in + "['")
    return resultat


code = """
DATA tab; 
	set tab;
    if COUNTRY="USA";
    if COUNTRY = "USA" then usa=1;
    else usa=0;
	if TEAM="CLE" then MODA="Winner";
	else if (TEAM="GSW" or TEAM="OKC") or TEAM="ORL" then MODA="Tie";
	else MODA="Loser";
RUN;
"""

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

resultat =""

for elem in word:
    elem = elem.replace("else if", "@")
    CONDITION = {"if ":3, "@":2}
    #IF
    for cond, n in CONDITION.items():
        if elem.lower().startswith(cond):
            var = elem[n:]        
            #IF.....THEN.....       
            if " then " in var.lower():
                var_then = re.split(" then | THEN ", var)
                #IF condition avant THEN
                b_then = var_then[0]
                b_then = re.sub(" or | OR | oR | Or ", " Ӫ ", b_then)
                b_then = re.sub(" and | AND | And | ANd | aND | aNd | AnD "," Ā ", b_then)
                b_then = re.sub("<=| le | LE | Le | lE ", " Ԗ ", b_then)
                b_then = re.sub(">=| ge | GE | Ge | gE ", " Ԡ ", b_then)
                b_then = re.sub("<| lt | LT | Lt | lT ", " Ī ", b_then)
                b_then = re.sub(">| gt | GT | Gt | gT ", " Ŝ ", b_then)
                b_then = re.sub(" ne | NE | Ne | eN ", " Đ ", b_then)
                b_then = re.sub("=| eq | EQ | eQ | Eq "," Ē ", b_then)
                b_then = re.sub(" in | IN | In | iN ", "'].isin", b_then)
                b_then = re.split(" ", b_then)
            
                for i in range(0,len(b_then)):
                    b_then[i] = re.sub("Ӫ", ") | (" + t_in + "['", b_then[i])
                    b_then[i] = re.sub("Ā", ") & (" + t_in + "['", b_then[i])
                    b_then[i] = re.sub("Ē", "']==", b_then[i])
                    b_then[i] = re.sub("Ԗ", "']<=", b_then[i])
                    b_then[i] = re.sub("Ԡ", "']>=", b_then[i])
                    b_then[i] = re.sub("Ŝ", "']>", b_then[i])
                    b_then[i] = re.sub("Ī", "']<", b_then[i])
                    b_then[i] = re.sub("Đ", "']!=", b_then[i])
                #IF condition après THEN
                modalite = var_then[1]
                modalite = re.split(" = |=", modalite)
                new_var = modalite[0]
                moda = modalite[1]
                
                if "['" + new_var + "']" not in resultat:
                    resultat += t_out + "['" + new_var + "'] = np.where((" + t_in + "['" + "".join(b_then) + "), " + moda + ", '')\n"
                elif "['" + new_var + "']" in resultat: 
                    resultat += t_out + "['" + new_var + "'] = np.where((" + t_in + "['" + "".join(b_then) + "), " + moda + ", " + t_out + "['" + new_var + "'])\n"
    
            #IF....;  
            elif " then " not in var.lower():
                resultat += where(elem,3) + "\n"
            

    #ELSE
    if elem.lower().startswith("else "):
        var_else = elem[5:]
        modalite = re.split(" = |=", var_else)
        new_var = modalite[0]
        moda = modalite[1]
        
        if "['" + new_var + "']" not in resultat:
            resultat += "idk"
        elif "['" + new_var + "']" in resultat:
            resultat += t_out + "['" + new_var + "'] = np.where((" + t_in + "['" + new_var + "'])=='', " + moda + ", " + t_out + "['" + new_var + "'])\n"
        
    resultat = resultat.replace(t_out + "['(","(" + t_out + "['")

        

        