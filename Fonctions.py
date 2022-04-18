#----------------------------------#
#           FONCTIONS              #
#----------------------------------#

# RECUPERE LE NOM DE LA TABLE D'ENTREE
def tab_out(code):
    word = code.lower().split(";")

    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Récup table sortie
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
    
    return sortie_tab

# RECUPERE LE NOM DE LA TABLE DE SORTIE
def tab_in(code):
    word = code.lower().split(";")

    #Enlève les espaces pour chaque éléments de words
    for i in range(0,len(word)):
          word[i] = word[i].strip()
          
    #Récup table entree
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
            
    return entree_tab