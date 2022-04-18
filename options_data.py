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
    print(sortie_tab)
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    print(entree_tab)
    
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


data_rename(1,"""    DATA table_1                  ;    set table  ;
rename name=nom height=taille weight=poids;
keep prix vente moy ;
DROp age sex var3   var4;
if age > 30 then output         ;

run;
""")
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
    print(sortie_tab)
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    print(entree_tab)
    
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


data_where(1,"""
    data table1; set table;
    keep age sex var3 var4;
    where sex = 'male' and age >=40 and var4 <=30; 
    run;
    """)
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
    print(sortie_tab)
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    print(entree_tab)
    
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

data_drop(1,"""    DATA tab1                 ;    set tab  ;
rename name=nom;
drop age sexe taille poids origine etudiant actif  ;
if age > 30 then output         ;
run;
""")
data_keep(1,"""    DATA tab1                 ;    set tab  ;
rename name=nom;
keep age sexe taille poids origine etudiant actif  ;
if age > 30 then output         ;
run;
""")


#=====================================================================================
#                       IF 
#=====================================================================================


code = """
    data table1; set table;
    keep age sex var3 var4;
    if sex='male' then sexe = 'homme';else if sex='female' then sexe= 'femme';else sexe ="inconnu"; 
    run;
    """
def data_if(first,code):
    code2  = code.replace("else if","elif")
    word= code.replace("else if","elif")
    word = word.lower().split(";")
    
    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Boucle qui permet de récupérer la table de sortie et entrée
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
    print(sortie_tab)
    
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
    print(entree_tab)
    
            
    for elem in word:
        if elem.startswith("if"):
            var_if = elem[3:]
            
            list_var = var_if.split("then")       
    for i in range(0,len(list_var)-1):
        list_var[i] = list_var[i].strip()
        chaine_var = list_var[0].split("=")
        old_var = chaine_var[0]
        modalite_if = chaine_var[1]
        chaine_var2 = list_var[1].split("=")
        new_var = chaine_var2[0]
        modalite_if2 = chaine_var2[1]
    
    if "elif" in code2:
        for elem in word:
            if elem.startswith("elif"):
                var_else_if = elem[7:]
                list_var_else_if =var_else_if.split("then")
                chaine_var_else_if = list_var_else_if[0].split("=")
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
        resultat1 += sortie_tab +"['"+new_var+"']=" + "first table"+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +") else (" + modalite_else_if2 + "if (x==" + modalite_else_if + ") else"+ modalite_else + "))"
        resultat1_1 = ""
        resultat1_1 += sortie_tab +"['"+new_var+"']=" + "not first table" +"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +") else (" + modalite_else_if2 + "if (x==" + modalite_else_if + ") else"+ modalite_else + "))"

    #if /else if
    if "elif" in code2:
        resultat2 = ""
        resultat2 += sortie_tab +"['"+new_var+"']=" + "first table"+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +") else (" + modalite_else_if2 + "if (x==" + modalite_else_if + ")"
        resultat2_2 = ""
        resultat2_2 += sortie_tab +"['"+new_var+"']=" + "not first table"+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +") else (" + modalite_else_if2 + "if (x==" + modalite_else_if + ")"

    #if/ else
    if "else" in code2:
        resultat3 = ""
        resultat3 += sortie_tab +"['"+new_var+"']=" + "first table"+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +")  else"+ modalite_else + "))"
        resultat3_3 = ""
        resultat3_3 += sortie_tab +"['"+new_var+"']=" + "not first table"+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +")  else"+ modalite_else + "))"

    count_else =0
    count_elseif =0
    for elem in word:
        if "elif" in elem:
            count_elseif +=1
        if "else" in elem:
            count_else +=1
    
    
    print(count_else)
    print(count_elseif)
    if count_else == 1 and count_elseif ==1 and first == 1:
        return(resultat1)
    elif count_else == 1 and count_elseif ==1 and first !=1:
        return(resultat1_1)
    elif count_else ==0 and count_elseif ==1 and first == 1:
        return(resultat2)
    elif count_else == 0 and count_elseif ==1 and first !=1:
        return(resultat2_2)
    elif count_else ==1 and count_elseif ==0 and first ==1:
        return(resultat3)
    elif count_else == 1 and count_elseif ==0 and first !=1:
        return(resultat3_3)


        
data_if(1,"""
    data table1; set table;
    keep age sex var3 var4;
    if sex='male' then sexe = 'homme';elif  sex='male' then sexe = 'homme';else sexe = 'inconnu';
    run;
    """)