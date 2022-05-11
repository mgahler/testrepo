1# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:28:00 2018

@author: Mark
"""


#Using linear regression
#https://realpython.com/linear-regression-in-python/#simple-linear-regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
from numpy import array
from sklearn.linear_model import LinearRegression

####### PLOT CAL

percent_ch4 = array([0.0,50.0,100.0])
xrange = np.arange(0,110,10)

plt.figure(figsize=(10,6))

sensor_mV = array([-5.33,52.2,89.1])  #m1 - 25
coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
pfit = poly.Polynomial(coefs)  
plt.plot(xrange, pfit(xrange), label="M1/25")   

#sensor_mV = array([2.5,65.2,97.8])  #m4 - 28
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='M4/28')   
#
#sensor_mV = array([-45.2,10.6,49.1])  # 8 - 24
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='8/24')   
#
#sensor_mV = array([19.1,73.9,110.5])  # m2 - 26
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='M2/26')   
#
#sensor_mV = array([20.0,76.2,111.4])  # m5 - 21
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='M5/21')   
#
#sensor_mV = array([-25.0,31.6,70.4])  # 9 23
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='9/23')   
#
#sensor_mV = array([34.0,88.0,123.6])  # m3 (slow) - 27 
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='M3/27')   
#
#sensor_mV = array([17.0,74.0,109.4])  # m6 - 20
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='M6/20')   
#
#sensor_mV = array([13.0,67.4,105.2])  # 10 - 29
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='10/29')   
#
#sensor_mV = array([-3.8,53.1,92.1])  # 11 - 22
#coefs = poly.polyfit(percent_ch4, sensor_mV, 2 )
#pfit = poly.Polynomial(coefs)  
#plt.plot(xrange, pfit(xrange), label='11/22')   

plt.ylabel('Sensor Response (mV)',fontsize='large')  
plt.xlabel('CH4 Concentration %',fontsize='large')  
plt.title('MP-7217-TC Calibration')
plt.legend(loc='lower right')

####### GET CURVES

#sensor_mV = array([-5.33,52.2,89.1])  #m1 - 25
#sensor_mV = array([2.5,65.2,97.8])  #m4 - 28
#sensor_mV = array([-45.2,10.6,49.1])  # 8 - 24
#sensor_mV = array([19.1,73.9,110.5])  # m2 - 26
#sensor_mV = array([20.0,76.2,111.4])  # m5 - 21
#sensor_mV = array([-25.0,31.6,70.4])  # 9 23
#sensor_mV = array([34.0,88.0,123.6])  # m3 (slow) - 27 
#sensor_mV = array([17.0,74.0,109.4])  # m6 - 20
#sensor_mV = array([13.0,67.4,105.2])  # 10 - 29
#sensor_mV = array([-3.8,53.1,92.1])  # 11 - 22


#percent_ch4 = array([0.0,50.0,100.0])
#coefs = poly.polyfit(sensor_mV, percent_ch4, 2 )
#pfit = poly.Polynomial(coefs)    # instead of np.poly1d
#xrange = np.arange(sensor_mV[0],sensor_mV[2],5)
#plt.plot(xrange, pfit(xrange), color='orange')   
#
#
#
#print(coefs)
#print(coefs[0])
#print(coefs[1])
#print(coefs[2])

#mv = 0
#mv2 = mv*mv
#conc = coefs[0] + coefs[1]*mv + coefs[2]*mv2 
#print(conc) 

