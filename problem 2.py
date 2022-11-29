#Name: Monowar Hossain Saikat
#Lamar ID: L20488191

#Loading libraries:
import os
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

#Defining path
path = 'C:\\Users\\User\\OneDrive\\Desktop\\mock'
os.chdir (path) 

a=pd.read_csv('nst-est2019-02.csv')
print(a)


dataArray = np.genfromtxt('nst-est2019-02.csv', delimiter=',', names=True)





