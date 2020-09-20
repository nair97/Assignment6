#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:10:50 2020

@author: meerarakesh09
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',15) # this limit maximum numbers of rows

def read_data(infileName):
    AO = np.loadtxt('monthly.ao.index.b50.current.ascii')
    AO[0:2]
    AO.shape
    dates = pd.date_range('1950-01', periods=AO.shape[0], freq='M')
    dates
    dates.shape
    AO = Series(AO[:,2], index=dates)
    AO
    AO.plot()
    AO['1980':'1990'].plot()
    AO['1960']
    
    NAO = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
    dates_NAO = pd.date_range('1950-01', periods=NAO.shape[0], freq='M')
    NAO = Series(NAO[:,2], index=dates_NAO)
    NAO.index
    AONAO = DataFrame({'AO' : AO, 'NAO' : NAO})
    AONAO.plot(subplots=True)
    AONAO['NAO']
    AONAO.mean()
    AO_mm = AO.resample("A").mean()
    AO_mm.plot(style='g--')
    AO_mm = AO.resample("A").median()
    AO_mm.plot()
    AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
    AO_mm['1900':'2020'].plot(subplots=True)
    AO_mm['1900':'2020'].plot()
    AO_mm
    AONAO.rolling(window=12, center=False).mean().plot(style='-g')
    AONAO.AO.rolling(window=120).corr(other=AONAO.NAO).plot(style='-g')
    AONAO.corr()
     
    plt.close()
    