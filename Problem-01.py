#Name: Monowar Hossain Saikat
#Lamar ID: L20488191

#Importing libraries
import os
import numpy as np
from scipy.integrate import solve_ivp
#Defining path
path = 'C:\\Users\\User\\OneDrive\\Desktop\\mock'
os.chdir (path) 

#given value:

h=6
q=40
Cd=0.6
g=32.2
pi=3.1416
x = 32*q/(pi*pi)*Cd*Cd*g 
print(x)
#Function derivation
def fd(q,pi,Cd,g,h,D,x):
    fd= D**5-12*D**4+x
    fd1=5*D**4-48*D**3 #1st time differentiation 
    
    
    
    
    

 

