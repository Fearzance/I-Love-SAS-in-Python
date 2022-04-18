import re

exemple = """
data table1 ; set table; 
keep age sex var3 var4;
"""
exemple2 = """
    data table1; set table;
    keep age sex var3 var4;
    run;
    """
def nom_table_entree(text):
    words = re.split("[= (;\s]",text)
    words = [ w for w in words if w != '' ]
    return words[3]

def nom_table_sortie(text):
    words = re.split("[= (;\s]",text)
    words = [ w for w in words if w != '' ]
    return words[1]

#def option_keep(text):
#    words = re.split("[= (;\s]",text)
#    words = [ w for w in words if w != '' ]
#    if words[4].lower() == 'keep':
#        var = [elem for elem in words[5:]]
#        return 



# def keep(text):
#     words = re.split("[= (;\s]",text)
#     words = [ w for w in words if w != '' ]
#     p = words.index("keep") 
#     if words[p].lower() == 'keep':
#         var = [elem for elem in words[p+1:-1]]



        
nom_table_entree(text=exemple)
nom_table_sortie(text=exemple)


def trad(text, debug=False):
    
    # words = re.split("[= (;\s]",text)
    # words = [ w for w in words if w != '' ]
    # p = words.index("keep") 
    # if words[p].lower() == 'keep':
    #     var = [elem for elem in words[p+1:-1]]
    words = exemple.split("[= (;\s]")
    words = exemple.splitlines()
    words = [ w for w in words if w != '' ]
    for i in words:   
        if not i.startswith('keep'):
            words.remove(i)
            words = " ".join(words)
            
    characters = ";"
    
    for x in range(len(characters)):
        words = words.replace(characters[x],"")
    words = words.replace("keep ","")
    if words.startswith(" "):
        words = words.lstrip()
    
    var = words.split(" ")
 
    #on récupère le nom du dataset entree
    entree = nom_table_entree(text=exemple)
    #on récupère le nom du dataset entree
    sortie = nom_table_sortie(text=exemple)
    
 
#Join sur la liste / boucle    
    if len(var) == 2:
        code  = ""
        code += sortie + "=" + entree + "['" + var[len(var)-2]+"'" + ",'" + var[len(var)-1]+ "'" + "]"
        print(code)
    elif len(var) == 3:
        code  = ""
        code += sortie + "=" + entree + "[" +"'" + var[len(var)-3]+"'" + ",'" + var[len(var)-2]+"'" + "," + "'" + var[len(var)-1]+ "'" + "]"
        print(code)
    elif len(var) == 4:
        code  = ""
        code += sortie + "=" + entree + "['" + var[len(var)-4]+"','" + var[len(var)-3]+"','" + var[len(var)-2]+"'" + "," + "'" + var[len(var)-1]+ "'" + "]"
        print(code)
    elif len(var) == 5:
        code  = ""
        code += sortie + "=" + entree + "[" +"'" + var[len(var)-5]+"'"+"'" + var[len(var)-4]+"'"+"'" + var[len(var)-3]+"'" +"'" + var[len(var)-2]+"'" + "," + "'" + var[len(var)-1]+ "'" + "]"
        print(code)


trad(text=exemple)



def exem(text)

#Brouillon
words = exemple.split("[= (;\s]")
words = exemple.splitlines()
words = [ w for w in words if w != '' ]
for i in words:   
    if not i.startswith('keep'):
        words.remove(i)
        words = " ".join(words)
        
characters = ";"
for x in range(len(characters)):
    words = words.replace(characters[x],"")
    
words = words.replace("keep ","")
if words.startswith(" "):
    words = words.lstrip()

var = words.split(" ")


#Dataframe
import pandas 
import numpy
ar = numpy.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]])
df = pandas.DataFrame(ar, index = ['a1', 'a2', 'a3'], columns = ['A', 'B', 'C', 'D'])
print(df)

def age_grp_if(x): 
    if (x < 2) :
        return 'young age'
    elif (x < 3.5):
        return 'middle age'
    else:
        return 'old age'

age_group = df.copy()
age_group['age_grp_if'] = age_group['A'].apply(age_grp_if)
age_group.head()

table12=df.assign(E=3)
df['A']==1.1
table12=df.loc[df['A']>=2]
if df['A']==1.1:
    print(table12=df.assign(E=3))
else:
    table12=df.lassign(E=5)    
elif df.loc[df['A']==3]:
    table12=df.lassign(E=4)
else:
    table12=df.lassign(E=5)
print(table12)
                 
df2 = df.drop(columns=['A','B','D'])
print(df2)

from DATA import data_rename
data_rename(code)

#Code If

def data_if(code):
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
        if elem.startswith("if"):
            var = elem[3:]
            list_var = var.split()
    
    resultat = ""
    resultat += sortie_tab + "#" + entree_tab +".loc["+entree_tab+"['" + "'".join(list_var) + "]" 
    
    resultat = resultat.replace("#","=")
    resultat = resultat.replace("''","'")
    resultat = resultat.replace("'=","']==")
    resultat = resultat.replace("'>","']>")
    resultat = resultat.replace("'>=","']>=")
    resultat = resultat.replace("'<","']<")
    resultat = resultat.replace("'<=","']<=")
    resultat = resultat.replace("and",",[")
    return(resultat)

data_if("""
    data table1; set table;
    keep age sex var3 var4;
    if sex = 'male' and age >=40 and var4 <=30;
    run;
    """)
#Brouillon if
code = """
    data table1; set table;
    keep age sex var3 var4;
    if sex = 'male' and age >40 and var4 <30;
    run;
    """
#Brouillon if else
if sex='male' then sexe = 'homme'; else if sex = 'female' then sexe = 'femme';else sexe = 'inconnu' ; :
    
import pandas 
import numpy
ar = numpy.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]])
df = pandas.DataFrame(ar, index = ['a1', 'a2', 'a3'], columns = ['A', 'B', 'C', 'D'])
print(df)

#option1
def age_grp_if(x): 
    if (x < 2) :
        return 'faible'
    elif (x < 3.5):
        return 'moyen'
    else:
        return 'fort'    
age_group = df.copy()
age_group['age_grp_if'] = age_group['A'].apply(age_grp_if)
age_group.head()

#☺option 2
age_group['age_grp_lambda'] = age_group['A'].apply(
    lambda x : 'homme'  if (x =='male') else (
               'femme' if (x == 'female') else 'inconnu'))
age_group.head()

table1[' sexe ']=table['sex'].apply(
    lambda x : 'homme'if (x=='male') else ( 
               'femme'if (x== 'female' ) else 'inconnu'))
#♣Brouillon

code = """
    data table1; set table;
    keep age sex var3 var4;
    if sex='male' then sexe = 'homme'; else sexe = 'inconnu' ; 
    run;
    """
code2 = code.replace("else if","alexouu")
word= code.replace("else if","alexouu")
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

#Récupérer les variables de l'instruction DROP
for elem in word:
    count_if =0
    if elem.startswith("if"):
        count_if+=1
    else:
        count_if +=0
        
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

if "alexouu" in code2:
    for elem in word:
        if elem.startswith("alexouu"):
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
list_ds = ['else', 'elif']     
if "elif" in code2 and "else" in code2:  
    resultat = ""
    resultat += sortie_tab +"['"+new_var+"']=" + entree_tab+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +") else (" + modalite_else_if2 + "if (x==" + modalite_else_if + ") else"+ modalite_else + "))"
    print(resultat)
    
#if /else if
if "elif"  in code2:  
    resultat2 = ""
    resultat2 += sortie_tab +"['"+new_var+"']=" + entree_tab+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +") else (" + modalite_else_if2 + "if (x==" + modalite_else_if + ")"
    print(resultat2)
#if/ else
if "else" in code2:
    resultat3 = ""
    resultat3 += sortie_tab +"['"+new_var+"']=" + entree_tab+"['" +old_var +"'].apply(lambda x :" + modalite_if2 + "if (x==" + modalite_if +")  else"+ modalite_else + "))"
    print(resultat3)

test = " ".join(word)
count_else =0
count_elseif =0
if "alexouu" in test:
    count_elseif +=1
elif "else" in test:
    count_else +=1

print(count_else)
print(count_elseif)
if count_else == 1 and count_elseif ==1:
    print(resultat)
elif count_else ==0 and count_elseif ==1:
    print(resultat2)
elif count_else ==1 and count_elseif ==0:
    print(resultat3)
    
if ('else'and not'if') in test:
    print("yes")
else:
    print("no")
    
for elem in word:
    count_1 =0
    count_2 =0
    count_3 =0
    if ((elem.startswith("else")) and not (elem.startswith("alexouu"))):
        count_3 +=1
    elif ((elem.startswith("alexouu")) and not (elem.startswith("else"))):         
        count_2 +=1
    else:   
        count_1 +=1
        
if count_1==1 and count_2 ==0 and count_3==0:
    print(resultat)
elif count_1==0 and count_2 ==1 and count_3==1:
    print(resultat2)
else:
    print(resultat3)
    
print(count_3)
print(count_2)
print(count_1)
#Avec liste   
list_for_elseif=['if','else if']    
list_for_else = ['if','else']   
po = ['ljkjsqd','else if fd',"else"] 
for elem in list_for_elseif:
    compteur_else =0 
    compteur_elseif=0
    if elem in list_for_elseif):       
        compteur_elseif+=1
    else:
        print('pas ok')
print(compteur_elseif)
    
"else" in list_for_else
   
for elem in word:
    if ((elem.startswith("else") in list_for_else) and not (elem.startswith("else if") in list_for_elseif)):
        print(resultat3)
    elif ((elem.startswith("else if") in list_for_elseif) and (elem.startswith("else") not in list_for_elseif)):         
        print(resultat2)
    elif ((elem.startswith("else") in list_for_else) and  (elem.startswith("else if"))):   
        print(resultat)

test = """ if;  else if blab ; else dkspq ; run;"""
liste_test = test.lower().split(";")
for i in range(0,len(liste_test)):
      liste_test[i] = liste_test[i].strip()
      
for elem in liste_test:
    if ((elem.startswith("else")in list_for_else)) :
        print(resultat)
    else:
        print("non")
        
import sys 
sys.path.append(r"C:\Users\alexa\Desktop\I Love SAS in Python\code_python_traducteur_draft\Programmes mémoire")

from _p_print import p_print
from DATA2 import data_where
data_where("""data table; set table1;
           where age >=40;
           run;
           """)
from Fonctions import tab_out, tab_in
tab_out(code)


code2=code.lower()

code = """    DATA table_1                  ;    set table  ;
 rename name=nom height=taille weight=poids;
 keep prix vente moy ;
 DROp age sex var3   var4;
 where age > 30          ;
 if sex = 'female' then sexe= 'femme' ; else if  sex = 'male' then sexe = 'homme';
 run;
 """   
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




for elem in word:
    if elem.startswith("where"):
        var = elem[5:]
        list_var = var.split()

resultat_where1 = ""
resultat_where1 += sortie_tab + "#" + "first table" +".loc["+entree_tab+"['" + "'".join(list_var) + "]" 

resultat_where1 = resultat_where1.replace("#","=")
resultat_where1 = resultat_where1.replace("''","'")
resultat_where1 = resultat_where1.replace("'=","']==")
resultat_where1 = resultat_where1.replace("'>'","']>")
resultat_where1 = resultat_where1.replace("'>=","']>=")
resultat_where1 = resultat_where1.replace("'<","']<")
resultat_where1 = resultat_where1.replace("'<=","']<=")
resultat_where1 = resultat_where1.replace("and",",[")

resultat_where2 = ""
resultat_where2 += sortie_tab + "#" + "not first table" +".loc["+entree_tab+"['" + "'".join(list_var) + "]"     
resultat_where2 = resultat_where2.replace("#","=")
resultat_where2 = resultat_where2.replace("''","'")
resultat_where2 = resultat_where2.replace("'=","']==")
resultat_where2 = resultat_where2.replace("'>","']>")
resultat_where2 = resultat_where2.replace("'>=","']>=")
resultat_where2 = resultat_where2.replace("'<","']<")
resultat_where2 = resultat_where2.replace("'<=","']<=")
resultat_where2 = resultat_where2.replace("and",",[")
if first == 1:
    return resultat_where1
else:
    return resultat_where2
