import sys
sys.path.append(r"C:\Users\kevin\Documents\Mémoire\Mémoire M2\2_Programmes")

from Fonctions import tab_out, tab_in

def substr(code):
    global entree
    global sortie

    entree = tab_in(code)
    sortie = tab_out(code)
    word = code.lower().split(";")

    #S'il y a la fonction substr, il va récupèrer les idfférents paramètres de la fonction
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
    
    #Si dans la fonction substr la position n = 1 alors n = 0 
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

print(substr("""DATA table1;set table2;
             new_name = substr(prénom,5,8);
             run;"""))