#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:47:35 2020

@author: meerarakesh09
"""

# import required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame, Panel

# user defined functions
def read_data( inFileName ):
    # open the data file and read contents, retuns a dataframe
    dataDF = pd.read_table(inFileName, header=None,delimiter='\t', skiprows=26,usecols=[2,4], names=['Datetime','Discharge'])
    return dataDF

def get_daily_mean_flow( dataDF ):
    # calculate daily mean value, returns a new dataframe
    dates = pd.date_range(start='2015-03-17', periods=dataDF.shape[0],freq='15min')
    
    daily_flow = Series(dataDF['Discharge'].values, index = dates).resample('D').mean() 
    
    return daily_flow

def get_highest_flow( dataDF, Nvals ):
    # identify the Nval highest value, returns a new dataframe with Nvals rows
    highest_flow = dataDF.sort_values(by = 'Discharge', ascending=False)[:Nvals]
    return highest_flow
    
def get_monthly_mean_flow( dataDF ):
    # calculate monthly mean value, returns a new dataframe
    monthly_flow = dataDF.resample('M').mean()
    return monthly_flow

def plot_streamflow( dataDF ):
    # create plots of the time series data
    daily_flow = get_daily_mean_flow(dataDF)
    daily_flow.plot(figsize=(10,5),style='g--')
    plt.title('Wabash river discharge daily mean flow')
    plt.xlabel('Discharge-cubic ft/sec')
    plt.ylabel('Date')
    plt.legend(['Daily mean flow'],loc = 'upper right')
    plt.savefig('Wabash river discharge daily average flow.pdf')
    plt.show()
    plt.close()
    
    highest_flow = get_highest_flow(dataDF)
    highest_flow.plot(figsize=(10,5),style='b--')
    plt.title('Wabash river discharge top 10 highest daily average flow')
    plt.xlabel('Date')
    plt.ylabel('Discharge-cubic ft/sec')
    plt.legend(['Highest flow'],loc = 'upper right')
    plt.savefig('Wabash river discharge top 10 highest average streamflow.pdf')
    plt.show()
    plt.close()
    
    monthly_flow = get_monthly_mean_flow(dataDF)
    monthly_flow.plot(figsize=(10,5),style='r+')
    plt.title('Wabash river discharge monthly average flow')
    plt.xlabel('Date')
    plt.ylabel('Discharge-cubic ft/sec')
    plt.legend(['Monthly avg flow'],loc = 'upper right')
    plt.savefig('Wabash river discharge monthly average streamflow.pdf')
    plt.show()
    plt.close()
# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    # define filename
    inFileName = 'WabashRiver_Discharge_20150317-20160324.txt'
    
    # read in data file
    dataDF = read_data( inFileName )
    
    print('Daily average streamflow of Wabash river discharge \n')
    outfileName = 'Wabash river discharge daily average flow.pdf'
    get_daily_mean_flow(outfileName)
    
    print('The top 10 highest average streamflow of Wabash river discharge \n')
    outfileName = 'Wabash river discharge top 10 highest average streamflow.pdf'
    get_highest_flow(dataDF,outfileName)
    
    print('Monthly average streamflow of Wabash river discharge \n')
    outfileName = 'Wabash river discharge monthly average streamflow.pdf'
    get_monthly_mean_flow(outfileName)
    
    # create plots of time series data
    plot_streamflow( dataDF )