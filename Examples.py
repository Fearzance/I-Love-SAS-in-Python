# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:21:56 2022

@author: Alexandre HUANG & Kevin KAMALANATHAN
"""
#------------------------------------------------------------------------------------------
# This program includes the "TRANSLATOR" function which allows to translate a DATA step, 
# For the moment, it can translate DROP, KEEP, WHERE, IF ELSE IF ELSE and RENAME statements 
# and also SUBSTR function.
#------------------------------------------------------------------------------------------


#=============================================================================================
# Import of functions from the Function_analyzer program allowing the translation of SAS codes
#=============================================================================================

import sys

#------------------------------------------------------------------------
# Put your path in order to access the python programs Functions_analyzer
#------------------------------------------------------------------------
sys.path.append(r"C:\Users\alexa\Desktop\I Love SAS in Python\code_python_traducteur_draft\Programmes mémoire")

from Functions_analyzer import data_drop, data_keep, data_rename, data_where, data_if, tab_out, tab_in, translator, proc_freq,proc_means 



#============================
# EXAMPLES FOR DATA STATEMENT
#============================

# Example with DROP statement
print(translator("""
                 Data table_1; set table_0;
                 drop age sex name;
                 Run;"""))

# Example with KEEP statement
print(translator("""
                 Data table_1; set table_0;
                 keep age sex name;
                 Run;"""))
                 
# Example with WHERE statement
print(translator("""
                 Data table_1; set table_0;
                 where age>=10;
                 Run;"""))

print(translator("""
                 Data table_1; set table_0;
                 where name="val-de-marne";
                 Run;"""))
                 
print(translator("""
                 Data table_1; set table_1;
                 where name="val-de-marne" and population=100000;
                 Run;"""))
                 
# Example with IF - ELSE IF - ELSE statement
print(translator("""
                 Data table_1; set table_0;
                 if sex = "female" then sexe= "femme" ; 
                 else if sex= "male" then sexe = "homme";
                 else sexe = "inconnu";
                 Run;
                 """))
                 
print(translator("""
                 Data table_1; set table_1;
                 if price <= 100 then dummy_price = 0 ; 
                 else if price > 200 then dummy_price = 1;
                 else dummy_price = 2;
                 Run;
                 """))
                 
print(translator("""
                 Data table_1; set table_0;
                 if sex = "female" then sexe= "femme" ; 
                 else sexe = "homme";
                 Run;
                 """))

print(translator("""
                 Data table_1; set table_0;
                 if sex = "female" then sexe= "femme" ; 
                 else if sex= "male" then sexe = "homme";
                 Run;
                 """))
                 
# Example with RENAME statement
print(translator("""
                 Data table_1; set table_0;
                 rename name=nom height=taille weight=poids;
                 Run;
                 """))
                 
# Example with SUBSTR function
print(translator("""
                 DATA table2;set table1;
                 new_name = substr(name,6);
                 RUN;
                 """))
                 
#----------------------------------------------                
# You can also combine the different statements
#----------------------------------------------

# Example with all statements
print(translator("""
                DATA table5; set table2 ;
                RENAME name=nom height=taille weight=poids;
                KEEP prix vente moy ;
                DROP age sex var3   var4;
                where age = "12";
                IF sex ='female' THEN sexe='femme'; 
                ELSE sexe='homme';
                new_name = substr(name,6);
                RUN;
                """))

#============================
# EXAMPLES FOR PROC STATEMENT
#============================

#----------------------------
# Example with for PROC FREQ
#----------------------------

print(proc_freq("""
                proc freq   data = class ;
                table sex  ;
                run;
                """))
                
#Example with contingency table
print(proc_freq("""
                proc freq   data = class ;
                table sex*age  ;
                run;
                """))
                
#----------------------------
# Example with for PROC MEANS
#----------------------------
print(proc_means("""
                 proc means   data = cars  ;
                 var invoice age ;
                 run;
                 """))
#Example with class 
print(proc_means("""
                 proc means   data = cars  ;
                 class model ;
                 var invoice age ;
                 run;
                 """))
#Example with nmiss
print(proc_means("""
                 proc means   data = cars nmiss ;
                 class model;
                 var invoice age ;
                 run;
                 """))