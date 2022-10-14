# -*- coding: utf-8 -*-


#1.kutuphaneler
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('koordinat2.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)
koordinat = veriler.iloc[:,1:4].values
print(koordinat)
sonucx = pd.DataFrame(data=veriler.iloc[:,1:2].values, index = range(37), columns = ['x'])
sonucy = pd.DataFrame(data=veriler.iloc[:,2:3].values, index = range(37), columns = ['y'])
sonucz = pd.DataFrame(data=veriler.iloc[:,3:4].values, index = range(37), columns = ['z'])
#print(sonuc1)
sonuc3 = pd.DataFrame(data = veriler.iloc[:,0:1].values, index = range(37), columns = ['frame'])
print(sonuc3)
#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
s=pd.concat([sonucx,sonucy,sonucz], axis=1)
print(s)
#x_train, x_test,y_train,y_test = train_test_split(sonuc3,sonuc1,test_size=0.33, random_state=0)

x_train, x_test,y_train,y_test = train_test_split(sonuc3,s,test_size=0.33, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

a=plt.plot(x_train,y_train,'bo',label='koordinatx',color='green')
b=plt.plot(x_test,regressor.predict(x_test),label='tahmin')

plt.title("Koordinat for every Frame")
plt.xlabel("Frame")
plt.ylabel("Koordinat")
plt.legend(b,a)
plt.savefig('resultt_multi.png')
plt.show()