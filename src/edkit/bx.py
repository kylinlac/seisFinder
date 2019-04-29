import os
#import sys
import datetime

import csv
import math

import pickle
import zipfile

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import cartopy.crs as ccrs
from matplotlib.ticker import AutoMinorLocator

#import pandas as pd
import numpy as np
#import pandas as pd


#--------------------------------------------
#tool


#合肥,AH,HEF,117.142,31.824,77,100,CTS-1E,EDAS-24IP
def ml_Read_Net_Station():
  #os.path.dirname(os.path.realpath(__file__))
  #fn='net-sta.csv'
  fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"bx_net-sta.csv")
  f=open(fn,'rt')
  ns=f.read().splitlines()  
  f.close()
  netsta=[ns1.split(',') for ns1 in ns]  
  #print(netsta)
  return netsta


def ml_getNets():
    nsd=ml_Read_Net_Station()
    n=[ns1[1] for ns1 in nsd]
    n1=set(n) #remove duplate
    n=list(n1)
    n.sort()
    #print(n)
    return n


def ml_getStations():
    nsd=ml_Read_Net_Station()
    n=[ns1[1]+"."+ns1[2] for ns1 in nsd]
    n1=set(n) #remove duplate
    n=list(n1)
    n.sort()
    #print(n)
    return n


'''
def ml_getStations_byNets(sNets):
  #BJ|SH
  nsNet=[]
  nsSta=[]
  #nsDis=[]
  #os.path.dirname(os.path.realpath(__file__))
  #fn='net-sta.csv'
  fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"bx_net-sta.csv")
  f=open(fn,'rb')
  drs=csv.reader(f,delimiter=',')
  sNet=sNets.split('|')
  print(sNet)    

  for r1 in drs:
    s1=r1[1]
    if s1 in sNet:
        nsNet.append(r1[1])
        nsSta.append(r1[2])
        #nsDis.append(0.0)
  f.close()
  #print(type(drs)) #_csv.reader
  #print(drs)    
  
  return (nsNet,nsSta)
'''

def ml_getStations_byNets(sNets):
  #BJ|SH
  nsd=ml_Read_Net_Station()
  sNet=sNets.split('|')
  #print(sNet)    
  n=[]
  for ns1 in nsd:
    n1=ns1[1]
    s1=ns1[2]
    if n1 in sNet:
        n.append(n1+"."+s1)
  return n

#塔寺,BU,TAS,115.493,40.0836,1276.17,100,BBVS-60,EDAS-24GN
# 0   1  2   3       4       5       6
def ml_getStations_byArea(lon1=100.0,lat1=30.0,lon2=110.0,lat2=40.0):
  nsd=ml_Read_Net_Station()
  #print(sNet)    
  n=[]
  for ns1 in nsd:
    n1=ns1[1]
    s1=ns1[2]
    lon=float(ns1[3])
    lat=float(ns1[4])
    alt=float(ns1[5])
    if lon1<=lon<=lon2 and lat1<=lon<=lon2:
        n.append([n1,s1,lon,lat,alt])
  return n

    
def ml_getStations_byCircle(lon0,lat0,r0):
  nsd=ml_Read_Net_Station()
  #print(sNet)    
  n=[]
  for ns1 in nsd:
    n1=ns1[1]
    s1=ns1[2]
    lon=float(ns1[3])
    lat=float(ns1[4])
    alt=float(ns1[5])
    dis1=math.sqrt((lon0-lon)*(lon0-lon)+(lat0-lat)*(lat0-lat))
    dis2=dis1*111.11    
    if dis2<=r0:
        n.append([n1,s1,lon,lat,alt,dis2])
  return n
    
   
def ml_Stations_getNameCn(sta):
  nsd=ml_Read_Net_Station()
  n=[]
  for sta1 in sta:
    for ns1 in nsd:
      name1=ns1[1]+"."+ns1[2]
      if name1==sta1:
        n.append(ns1[0])
  return n
 
def ml_Stations_getPosition(sta):
  nsd=ml_Read_Net_Station()
  n=[]
  for sta1 in sta:
    for ns1 in nsd:
      name1=ns1[1]+"."+ns1[2]
      if name1==sta1:
        n.append([ns1[3],ns1[4],ns1[5]])
  return n
    
#--------------------------------------------
#miniseed    
    


#--------------------------------------------
#seed    

    
    
#--------------------------------------------
#sac
    
    
#--------------------------------------------
