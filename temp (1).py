
option = ["keep","drop","substr","rename"]

#KEEP
def keep(elem):
    global resultat
    var = elem[5:]
    resultat = t_out + "=" + t_in2 +"[['" + "','".join(var.split()) + "']]"
    return resultat

#DROP
def drop(elem):
    global resultat
    var = elem[5:]
    resultat = t_out + "=" + t_in2 +".drop(columns=['" + "','".join(var.split()) + "'])"
    return resultat

#RENAME
def rename(elem):
    global resultat
    elem = elem.replace(" = ","=")
    elem = elem.replace(" =","=")
    elem = elem.replace("= ","=")
    var = elem[7:]
    resultat = t_out + "#" + t_in2 +".rename(columns:{'" + "','".join(var.split()) + "'})"
    resultat = resultat.replace("#","=")
    return resultat

#SUBSTR
def substr(elem):
    global resultat
    substr_contains = elem.split("=")
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
    if N == '1':
        resultat = t_out + '["' + new_var + '"] = ' + t_in2 + '["' + old_var + '"].str[:'+ length +']'
        return resultat
    if N != '1':
        N =str(int(N)-1)
        resultat = t_out + '["' + new_var + '"] = ' + t_in2 + '["' + old_var + '"].str[' + N +':'+ length +']'
        return resultat

    
    
def traductor(code):    
    global t_in2
    global t_out
    
    resultat=''
    flag=0
    word = code.split(";")
    
    #Separate the code into list and put everything in lowercase
    for i in range(0,len(word)):
          word[i] = word[i].strip()
          
    for elem in word:
        if elem.lower().startswith("data"):
            t_out = elem[5:].strip()
          
    #Loop that retrieves the input table
    for elem in word:
        if elem.lower().startswith("set"):
            t_in = elem[4:].strip()
            
    for elem in word:
        for opt in option:
            if elem.startswith(opt):
                if flag == 0:
                    flag = 1
                    t_in2 = t_in
                else:
                    t_in2 = t_out
                    

        if elem.lower().startswith("keep"):
            resultat+=keep(elem) + "\n"
        if elem.lower().startswith("drop"):
            resultat+=drop(elem) + "\n"
        if  "substr" in elem:
            resultat+=substr(elem) + "\n"
        if elem.lower().startswith("rename"):
            resultat+=rename(elem) + "\n"
            
    return resultat

