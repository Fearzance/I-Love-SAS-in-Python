
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

#Proc Means
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
    
def traductor(code):    
    global t_in2
    global t_out
    
    global table
    global var_means
    global var_class
    
    global var_freq
    
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
        
        
            
    #Proc steps
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
        #means
        for elem in word:
            if elem.startswith("var"):
                var = elem[3:]
                var_means = var.strip()
                var_means = var_means.split(" ")
                
        for elem in word:
            if elem.startswith("class"):  
                var = elem[5:]
                var_class = var.strip()
                
        #freq
        for elem in word:
            if elem.startswith("table"):
                var = elem[5:]
                var_freq = var.strip()
                
        
    for elem in word:
        if elem.startswith("proc means"):
            resultat += proc_means(elem) + "\n"
   
    for elem in word:
        if elem.startswith("proc freq"):
            resultat += proc_freq(elem) + "\n"
    
    return resultat

code = """
Data test ; set por;
drop age ;
run ;
proc means   data = cars nmiss ;
                 class model;
                 var invoice age ;
                 run;
proc freq   data = class ;
                table sex*age ;
                run;
"""
print(traductor(code))
