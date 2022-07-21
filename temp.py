
code = """DATA TABLE1; set    table;
     
        keep kev alex;
        drop kevin;
        keep chacal;
        rename chacal = keke alex =alexandre ;
        RUN;"""
        

option = ["keep","drop","rename"]



def keep(elem):
    
    global resultat
    var = elem[5:]
    resultat = t_out + "=" + t_in2 +"[['" + "','".join(var.split()) + "']]"
    
    return resultat

def drop(elem):
    global resultat
    var = elem[5:]
    resultat = t_out + "=" + t_in2 +".drop(columns=['" + "','".join(var.split()) + "'])"

    return resultat

def rename(elem):
    global resultat
    elem = elem.replace(" = ","=")
    elem = elem.replace(" =","=")
    elem = elem.replace("= ","=")
    var = elem[7:]
    resultat = t_out + "#" + t_in2 +".rename(columns:{'" + "','".join(var.split()) + "'})"
    resultat = resultat.replace("#","=")
    return resultat



def traductor (code):    
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
        if elem.lower().startswith("rename"):
              resultat+=rename(elem) + "\n"      
              
    return resultat

print(traductor(code))

