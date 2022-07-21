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
sys.path.append(r"C:\Users\kevin\Documents\Mémoire\Mémoire M2\2_Programmes")

from temp import traductor



#============================
# EXAMPLES FOR DATA STATEMENT
#============================

# Example with DROP statement
print(traductor("""
                 Data table_1; set table_0;
                 drop age sex name;
                 Run;"""))

print(traductor("""
                 Data table_1; set table_1;
                 drop age sex name;
                 Run;"""))

# Example with KEEP statement
print(traductor("""
                 Data table_1; set table_0;
                 keep age sex name;
                 Run;"""))
                 
print(traductor("""
                 Data table_1; set table_1;
                 keep age sex name;
                 keep taille;
                 Run;"""))
                 
                 
# Example with RENAME statement
print(traductor("""
                 Data base; set base_k;
                 rename name=nom height=taille weight=poids;
                 rename patient = malade;
                 Run;
                 """))
                 
# Example with SUBSTR function
print(traductor("""
                 data table5;set base;
                 new_name = substr(name,6);
                 RUN;
                 """))
                 
#----------------------------------------------                
# You can also combine the different statements
#----------------------------------------------

# Example with all statements
print(traductor("""
                DATA base; SET base_k ;
                rename name=nom height=taille weight=poids;
                keep prix vente moy ;
                drop age sex var3 var4;
                new_name = substr(name,6);
                new_var = substr(var1,1,7);
                new_var2 = substr(var,3,7);
                RUN;
                """))

