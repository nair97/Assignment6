#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:03:52 2020

@author: meerarakesh09
"""

# computing the daily mean flow, highest flow and monthly flow of Wabash river discharge
# import required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame, Panel

def read_data( inFileName ):
    # open the data file and read contents, retuns a dataframe
    dataDF = pd.read_table(inFileName, header=None, delimiter='\t', 
                           skiprows=26,usecols=[2,4], 
                           names=["datetime","Discharge"]
                           )
    #setting the index column to datetime 
    dataDF['datetime']= pd.to_datetime(dataDF['datetime'])
    #return the dataframe
    return dataDF.set_index('datetime')

def get_daily_mean_flow( dataDF ):
    # calculate daily mean value, returns a new dataframe
    
    return dataDF.resample('D').mean()

  
def get_highest_flow( dataDF, Nvals):
    # identify the Nval highest value, returns a new dataframe with Nvals rows
    return dataDF.nlargest(Nvals, columns=['Discharge'],keep='all').rename(columns={'Discharge':'Highest Flow'})
     
def get_monthly_mean_flow( dataDF ):
    # calculate monthly mean value, returns a new dataframe
    
    return dataDF.resample('M').mean()

def plot_streamflow( dataDF ):
    # create plots of the time series data
    
    # plot for daily average streamflow
    daily_flow = get_daily_mean_flow(dataDF)
    daily_flow.plot(figsize=(7,4),style='g--')# plotting figure size and display style
    plt.xlabel('Date', fontsize=10)# naming x-axis
    plt.ylabel('Discharge-cubic ft/sec', fontsize=10)# naming y-axis
    plt.title("Wabash river discharge daily mean flow", fontsize=12)# naming the title
    plt.savefig('WR daily average streamflow.pdf')# save the plot
    
    #plot for top 10 highest avearge streamflow
    highest_flow = get_highest_flow(daily_flow,10)
    highest_flow.plot(figsize=(7,4), style = 'b*')# plotting figure size and display style
    plt.xlabel('Date', fontsize=10)# naming x-axis
    plt.ylabel('Discharge-cubic ft/sec', fontsize=10)# naming y-axis
    plt.title("Wabash river discharge top 10 highest daily average flow", fontsize=12)# naming the title
    plt.savefig('WR top 10 highest average streamflow.pdf')# save the plot
  
    #plot for daily discharge and highest flow data with symbols in subplots
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(daily_flow,c='b',label='Daily discharge',fillstyle='none')
    ax1.plot(highest_flow,c='r',marker="*",label='Highest flow')#plotting highest flow with marker
    plt.xlabel('Date', fontsize=10)# naming x-axis
    plt.ylabel('Discharge-cubic ft/sec', fontsize=10)# naming y-axis
    plt.title("Wabash river daily discharge and highest flow data", fontsize=12)# naming the title
    #plot legend
    plt.legend(loc='upper right')
    #save the plot
    plt.savefig('WR daily discharge and highest flow data.pdf')
    
    #plot for monthly average streamflow
    monthly_flow = get_monthly_mean_flow(daily_flow)
    monthly_flow.plot(figsize=(7,4),style='r--')# plotting figure size and display style
    plt.xlabel("Date", fontsize=10)# naming x-axis
    plt.ylabel("Discharge-cubic ft/sec", fontsize=10)# naming y-axis
    plt.title("Wabash river discharge monthly average flow", fontsize=12)# naming the title
    plt.savefig('WR monthly average streamflow.pdf')#save the plot
    
    #display plots
    plt.show()
    #close the plots
    plt.close()
    
# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    # define filename
    inFileName = 'WabashRiver_Discharge_20150317-20160324.txt'
    
    # read in data file
    dataDF = read_data( inFileName )
    
    # plots of time series data
    plot_streamflow( dataDF )