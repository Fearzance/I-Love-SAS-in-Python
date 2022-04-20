#----------------------------------#
#           FUNCTIONS              #
#----------------------------------#

# GET THE OUTPUT TABLE NAME
def tab_out(code):
    word = code.lower().split(";")

    #Separate the code into list and put everything in lowercase
    for i in range(0,len(word)):
          word[i] = word[i].strip()
    
    #Loop that retrieves the output table
    for elem in word:
        if elem.startswith("data"):
            sortie_tab = elem[5:]
    
    return sortie_tab

# GET THE INPUT TABLE NAME
def tab_in(code):
    word = code.lower().split(";")

    #Separate the code into list and put everything in lowercase
    for i in range(0,len(word)):
          word[i] = word[i].strip()
          
    #Loop that retrieves the input table
    for elem in word:
        if elem.startswith("set"):
            entree_tab = elem[4:]
            
    return entree_tab