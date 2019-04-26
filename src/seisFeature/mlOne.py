
import os
#import sys
import datetime

import pickle
import zipfile

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import cartopy.crs as ccrs
from matplotlib.ticker import AutoMinorLocator

import pylab as pl

#import pandas as pd
import numpy as np
#import pandas as pd


#--------------------------------------------
#sfml1
#1965-01-02,08:24:00.00, 26.800, 100.900,999, 2.5,
#0          1            2       3       4    5

#sfml2
#1965,01,02,08,24,00.00, 26.800, 100.900,  0, 2.5
#0   ,1 ,2 ,3 ,4 ,5    ,6      ,7       ,8  ,9


#scdFields={'fieldYear' : 0,'fieldMonth' : 1,'fieldDay':2,'fieldHour':3,'fieldMinute':4,
#'fieldSecond':5,'fieldLon':6,'fieldLat':7,'fieldMs':8,'fieldDepth':9}
scdFields={'fieldYear' : 0,'fieldMonth' : 1,'fieldDay':2,'fieldHour':3,'fieldMinute':4,
'fieldSecond':5,'fieldLat':6,'fieldLon':7,'fieldDepth':8,'fieldMs':9}

#def ml_Timing_count(mStep=0.1,sSuffix="10",bShowFigure=True,bSaveFigure=True,bSaveData=True):
def ml_Count_mag(data1,mStep=0.1,sSuffix="01",bShowFigure=True,bSaveFigure=True,bSaveData=True):
    '''
	震级区间内的地震数量，
	'''
    ms=[]
    dcs=[]
    
	#建立分档x
    mmin=0.0
    mmax=10.0
    vc=(mmax)/mStep+1
    #for i in range(mmin,mmax+mStep,mStep):
    #  ms.append(i)
    #  dcs.append(0)
    ms = pl.linspace(mmin, mmax,vc) 
    for i in range(len(ms)):
      dcs.append(0)
    
    print(len(ms),ms)
    print( len(dcs),dcs)
    
    idx=0
    #m0=0.0
    for d1 in data1:
      idx=int(float(d1[scdFields['fieldMs'] ])/mStep)
      #dcs[idx-m0]=dcs[idx-m0]+1
      dcs[idx]=dcs[idx]+1
    
    print( sum(dcs),dcs)

	#绘图支持中文
    plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
    plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题	
	
    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    plt.figure(figsize=(xin,yin))
    
    plt.plot(ms,dcs)
    plt.xticks([x for x in range(11)])  #x标记step设置为1
    plt.xlabel(u'震级',fontsize=16)
    plt.ylabel(u'数量',fontsize=16) #?不能标注中文
    plt.savefig('out/one_Count_m_'+sSuffix+'.png', dpi = 72)
    
    res=[]
    for i in range(len(ms)):
        res.append(str(ms[i])+','+str(dcs[i])+'\n')
    
    f2=open("out/one_Count_ms_"+sSuffix+".res.txt","w")
    f2.writelines(res)
    f2.close()

    
  
def ml_Count_year(data1):
    years=[]
    dcs=[]
    
    ymin=int(data1[0][0])
    ymax=int(data1[-1][0])
    for i in range(ymin,ymax+1):
      years.append(i)
      dcs.append(0)
      
    print(len(years),years)
    print(len(dcs),dcs)
    
    idx=0
    year0=ymin
    for d1 in data1:
      idx=int(d1[ scdFields['fieldYear'] ])
      dcs[idx-year0]=dcs[idx-year0]+1
    
    print(sum(dcs),dcs)
    
    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    pl.plot(years,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('year',fontsize=16)
    pl.savefig('out/one_Count_year.png', dpi = 72)
    
    res=[]
    for i in range(len(years)):
        res.append(str(years[i])+','+str(dcs[i])+'\n')
    
    f2=open("out/one_Count_year.res.txt","w")
    f2.writelines(res)
    f2.close()    
    
    
    
def ml_Count_month(data1):
    months=[]
    dcs=[]

    ymin=1
    ymax=12
    for i in range(ymin,ymax+1):
      months.append(i)
      dcs.append(0)
      
    print(len(months),months)
    print(len(dcs),dcs)
    
    idx=0
    for d1 in data1:
      idx=int(d1[scdFields['fieldMonth']])
      dcs[idx-1]=dcs[idx-1]+1
    
    print(sum(dcs),dcs)

    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    #ok
    pl.plot(months,dcs)
    #ok
    #pl.bar(years,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('month',fontsize=16)
    #ok
    #pl.show()
    pl.savefig('out/one_Count_month.png', dpi = 72)
    
    res=[]
    for i in range(len(months)):
        res.append(str(months[i])+','+str(dcs[i])+'\n')
    
    f2=open("out/one_Count_month.res.txt","w")
    f2.writelines(res)
    f2.close()        
            
    
    
def ml_Count_day(data1):
    months=[]
    dcs=[]

    ymin=1
    ymax=31
    for i in range(ymin,ymax+1):
      months.append(i)
      dcs.append(0)
      
    print(len(months),months)
    print(len(dcs),dcs)
    
    idx=0
    for d1 in data1:
      idx=int(d1[scdFields['fieldDay']])
      dcs[idx-1]=dcs[idx-1]+1
    
    print(sum(dcs),dcs)

    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    pl.plot(months,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('day',fontsize=16)
    pl.gca().lines[0].set_color('r')
    pl.savefig('out/one_Count_day.png', dpi = 72)
    
    res=[]
    for i in range(len(months)):
        res.append(str(months[i])+','+str(dcs[i])+'\n')
    
    f2=open("out/one_Count_day.res.txt","w")
    f2.writelines(res)
    f2.close()        
                
    
    
def ml_Count_hour(data1):
    months=[]
    dcs=[]

    ymin=1
    ymax=24
    for i in range(ymin,ymax+1):
      months.append(i)
      dcs.append(0)
      
    print(len(months),months)
    print(len(dcs),dcs)
    
    idx=0
    for d1 in data1:
      idx=int(d1[ scdFields['fieldHour'] ])
      dcs[idx-1]=dcs[idx-1]+1
    
    print(sum(dcs),dcs)

    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    pl.plot(months,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('hour',fontsize=16)
    pl.gca().lines[0].set_color('r')
    pl.savefig('out/one_Count_hour.png', dpi = 72)
    
    res=[]
    for i in range(len(months)):
        res.append(str(months[i])+','+str(dcs[i])+'\n')
    
    f2=open("out/one_Count_hour.res.txt","w")
    f2.writelines(res)
    f2.close()     
    
    