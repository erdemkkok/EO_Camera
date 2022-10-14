#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


def ML():
    veriler = pd.read_csv('koordinat.csv')
    #pd.read_csv("veriler.csv")


    #veri on isleme
    aylar = veriler[['Frame']]
    #test
    print(aylar)

    satislar = veriler[['Kuzey']]
    print(satislar)


    #verilerin egitim ve test icin bolunmesi
    from sklearn.model_selection import train_test_split
    x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)
    '''
    #verilerin olceklenmesi
    from sklearn.preprocessing import StandardScaler


    sc = StandardScaler()
    X_train = sc.fit_transform(x_train)
    X_test = sc.fit_transform(x_test)
    Y_train = sc.fit_transform(y_train)
    Y_test = sc.fit_transform(y_test)
    '''
    # model inşası (linear regression)
    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(x_train,y_train)

    tahmin = lr.predict(x_test)

    x_train = x_train.sort_index()
    y_train = y_train.sort_index()
    model=sm.OLS(lr.predict(x_train),x_train)
    print(model.fit().summary())
    plt.plot(x_train,y_train)
    plt.plot(x_test,lr.predict(x_test))

    plt.title("KOordinat for every Frame")
    plt.xlabel("Frame")
    plt.ylabel("KOordinat")
    plt.savefig('resultt.png')
    return tahmin