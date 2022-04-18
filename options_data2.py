# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:15:58 2022

@author: alexa
"""
#=====================================================================================
#                       RENAME
#=====================================================================================


def data_rename(first,code):
    #Sépare le code en list et met tout en minuscule
    word = code.lower().split(";")
    
    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Boucle qui permet de récupérer la table de sortie et entrée
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
    
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    
    
    #Récupérer les variables de l'instruction rename
    for elem in word:
        if elem.startswith("rename"):
            var = elem[7:]
            list_var = var.split(" ")
    
    
    resultat_rename1 = ""
    resultat_rename1 += sortie_tab + "#" + "first table" +".rename(columns#{'" + "','".join(list_var) + "'})"
    resultat_rename1 = resultat_rename1.replace("=","':'")
    resultat_rename1 = resultat_rename1.replace("#","=")
     
    resultat_rename2 = ""
    resultat_rename2 += sortie_tab + "#" + "not first table" +".rename(columns#{'" + "','".join(list_var) + "'})"
    resultat_rename2 = resultat_rename2.replace("=","':'")
    resultat_rename2 = resultat_rename2.replace("#","=")
    if first == 1:
        return resultat_rename1
    else:
        return resultat_rename2


#=====================================================================================
#                       WHERE
#=====================================================================================

def data_where(first,code):
    word = code.lower().split(";")
    
    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Boucle qui permet de récupérer la table de sortie et entrée
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    
    #Récupérer les variables de l'instruction DROP
    for elem in word:
        if elem.startswith("where"):
            var = elem[5:]
            list_var = var.split()
    
    resultat_where1 = ""
    resultat_where1 += sortie_tab + "#" + "first table" +".loc["+entree_tab+"['" + "'".join(list_var) + "]" 
    
    resultat_where1 = resultat_where1.replace("#","=")
    resultat_where1 = resultat_where1.replace("''","'")
    resultat_where1 = resultat_where1.replace("'='","']==")
    resultat_where1 = resultat_where1.replace("'>'","']>")
    resultat_where1 = resultat_where1.replace("'>='","']>=")
    resultat_where1 = resultat_where1.replace("'<'","']<")
    resultat_where1 = resultat_where1.replace("'<='","']<=")
    resultat_where1 = resultat_where1.replace("and",",[")
    
    resultat_where2 = ""
    resultat_where2 += sortie_tab + "#" + "not first table" +".loc["+entree_tab+"['" + "'".join(list_var) + "]"     
    resultat_where2 = resultat_where2.replace("#","=")
    resultat_where2 = resultat_where2.replace("''","'")
    resultat_where2 = resultat_where2.replace("'='","']==")
    resultat_where2 = resultat_where2.replace("'>'","']>")
    resultat_where2 = resultat_where2.replace("'>='","']>=")
    resultat_where2 = resultat_where2.replace("'<'","']<")
    resultat_where2 = resultat_where2.replace("'<='","']<=")
    resultat_where2 = resultat_where2.replace("and",",[")
    if first == 1:
        return resultat_where1
    else:
        return resultat_where2


#=====================================================================================
#                       DROP
#=====================================================================================


def data_drop(first,code):
    #Sépare le code en list et met tout en minuscule
    word = code.lower().split(";")
    
    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Boucle qui permet de récupérer la table de sortie et entrée
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    
    #Récupérer les variables de l'instruction DROP
    for elem in word:
        if elem.startswith("drop"):
            var = elem[5:]
            list_var = var.split()
    
    resultat_drop1 = ""
    resultat_drop1 += sortie_tab + "=" + "first table" +".drop(columns=['" + "','".join(list_var) + "'])"
    resultat_drop2 = ""
    resultat_drop2 += sortie_tab + "=" + "not first table" +".drop(columns=['" + "','".join(list_var) + "'])"
    
    if first == 1:
        return resultat_drop1
    else:
        return resultat_drop2

#=====================================================================================
#                       KEEP
#=====================================================================================

def data_keep(first,code):
    #Sépare le code en list et met tout en minuscule
    word = code.lower().split(";")

    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Récup table entree
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
            
    #Récup table sortie
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    
    #Récupérer les variables de l'instruction KEEP
    for elem in word:
        if elem.startswith("keep"):
            var = elem[5:]
            list_var = var.split()
    
    #Résultat
    
    resultat_keep1 = ""
    resultat_keep1 += sortie_tab + "=" + "first table" +"[['" + "','".join(list_var) + "']]"
    resultat_keep2 = ""
    resultat_keep2 += sortie_tab + "=" + "not first table" +"[['" + "','".join(list_var) + "']]"

    if first == 1:
        return resultat_keep1
    else:
        return resultat_keep2


#=====================================================================================
#                       IF 
#=====================================================================================


def data_if(first,code):
    code2= code.replace("else if","elif")
    code3 = code2.replace("<=",' IQ ')
    word = code3.replace(">=",' SQ ')
    word = word.lower().split(";")
    
    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Boucle qui permet de récupérer la table de sortie et entrée
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    
            
    for elem in word:
        if elem.startswith("if"):
            var_if = elem[3:]
            
    list_var = var_if.split("then")       
    for i in range(0,len(list_var)-1):
        list_var[i] = list_var[i].strip()
        chaine_var = list_var[0]
        if '<' in chaine_var:
            chaine_var = chaine_var.split("<")
            signe = '<'
        if '>' in chaine_var:
            chaine_var = chaine_var.split(">")
            signe = '>'
        if '=' in chaine_var:
            chaine_var = chaine_var.split("=")
            signe = '=='
        if 'iq' in chaine_var:
            chaine_var = chaine_var.split("iq")
            signe = '<='
        if 'sq' in chaine_var:
            chaine_var = chaine_var.split("sq")
            signe = '>='
        
        old_var = chaine_var[0]
        modalite_if = chaine_var[1]
        chaine_var2 = list_var[1].split("=")
        new_var = chaine_var2[0]
        modalite_if2 = chaine_var2[1]
    
    if "elif" in code2:
        for elem in word:
            if elem.startswith("elif"):
                var_else_if = elem[4:]
                list_var_else_if =var_else_if.split("then")
                chaine_var_else_if = list_var_else_if[0]
                if '<' in chaine_var_else_if:
                    chaine_var_else_if = chaine_var_else_if.split("<")
                    signe_elif = '<'
                if '>' in chaine_var_else_if:
                    chaine_var_else_if = chaine_var_else_if.split(">")
                    signe_elif = '>'
                if '=' in chaine_var_else_if:
                    chaine_var_else_if = chaine_var_else_if.split("=")
                    signe_elif = '=='
                if 'iq' in chaine_var_else_if:
                    chaine_var_else_if = chaine_var_else_if.split("iq")
                    signe_elif = '<='
                if 'sq' in chaine_var_else_if:
                    chaine_var_else_if = chaine_var_else_if.split("sq")
                    signe_elif = '>='
                
                modalite_else_if = chaine_var_else_if[1]
                
                chaine_var_else_if2 = list_var_else_if[1].split("=")
                modalite_else_if2 = chaine_var_else_if2[1]
    
    if "else" in code2:
        for elem in word:
            if elem.startswith("else"):
                var_else = elem[5:]
                list_var_else = var_else.split("=")
                modalite_else = list_var_else[1]
            
    #if /else if /else  
    if "elif" in code2 and "else" in code2:      
        resultat1 = ""
        resultat1 += "def condition(x):\n"
        resultat1 += "    if (x " + signe + modalite_if +"):\n"
        resultat1 += "        return " + modalite_if2 + "\n"
        resultat1 += "    elif (x " +  signe_elif +  modalite_else_if +"):\n "
        resultat1 += "        return " + modalite_else_if2 +"\n"
        resultat1 += "    else:\n"
        resultat1 += "        return " + modalite_else +"\n"
        resultat1 +=  sortie_tab + "['"+ new_var +"'] =" + "first table" + "['" + old_var +"'].apply(condition)"
                
        resultat1_1 = ""
        resultat1_1 += "def condition(x):\n"
        resultat1_1 += "    if (x " + signe + modalite_if + ") :\n"
        resultat1_1 += "        return " + modalite_if2 + "\n"
        resultat1_1 += "    elif (x" +  signe_elif +  modalite_else_if + "):\n "
        resultat1_1 += "        return " + modalite_else_if2 + "\n"
        resultat1_1 += "    else:\n"
        resultat1_1 += "        return " + modalite_else + "\n"
        resultat1_1 +=  sortie_tab + "['"+ new_var +"'] =" + "not first table" + "['" + old_var +"'].apply(condition)"
    
    #if /else if
    if "elif" in code2:
        resultat2 = ""
        resultat2 += "def condition(x):\n"
        resultat2 += "    if (x " + signe + modalite_if +"):\n"
        resultat2 += "        return " + modalite_if2 + "\n"
        resultat2 += "    elif (x " +  signe_elif +  modalite_else_if +"):\n "
        resultat2 += "        return " + modalite_else_if2 +"\n"
        resultat2 +=  sortie_tab + "['"+ new_var +"'] =" + "first table" + "['" + old_var +"'].apply(condition)"
                
        resultat2_2 = ""
        resultat2_2 += "def condition(x):\n"
        resultat2_2 += "    if (x " + signe + modalite_if + ") :\n"
        resultat2_2 += "        return " + modalite_if2 + "\n"
        resultat2_2 += "    elif (x" +  signe_elif +  modalite_else_if + "):\n "
        resultat2_2 += "        return " + modalite_else_if2 + "\n"
        resultat2_2 +=  sortie_tab + "['"+ new_var +"'] =" + "not first table" + "['" + old_var +"'].apply(condition)"
        
    #if/ else
    if "else" in code2:
        resultat3 = ""
        resultat3 += "def condition(x):\n"
        resultat3 += "    if (x " + signe + modalite_if +"):\n"
        resultat3 += "        return " + modalite_if2 + "\n"
        resultat3 += "    else:\n"
        resultat3 += "        return " + modalite_else +"\n"
        resultat3 +=  sortie_tab + "['"+ new_var +"'] =" + "first table" + "['" + old_var +"'].apply(condition)"
                
        resultat3_3 = ""
        resultat3_3 += "def condition(x):\n"
        resultat3_3 += "    if (x " + signe + modalite_if + ") :\n"
        resultat3_3 += "        return " + modalite_if2 + "\n"
        resultat3_3 += "    else:\n"
        resultat3_3 += "        return " + modalite_else + "\n"
        resultat3_3 +=  sortie_tab + "['"+ new_var +"'] =" + "not first table" + "['" + old_var +"'].apply(condition)"
        
    count_else =0
    count_elseif =0
    for elem in word:
        if "elif" in elem:
            count_elseif +=1
        if "else" in elem:
            count_else +=1
    
    
    if count_else == 1 and count_elseif ==1 and first == 1:
        return resultat1
    elif count_else == 1 and count_elseif ==1 and first !=1:
        return resultat1_1
    elif count_else ==0 and count_elseif ==1 and first == 1:
        return resultat2
    elif count_else == 0 and count_elseif ==1 and first !=1:
        return resultat2_2
    elif count_else ==1 and count_elseif ==0 and first ==1:
        return resultat3
    elif count_else == 1 and count_elseif ==0 and first !=1:
        return resultat3_3

        
