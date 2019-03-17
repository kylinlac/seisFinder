import os,sys,datetime
import csv
import math

#def getNetSta_center_radius(lon0,lat0,r0):
def getNetSta_cr(lon0,lat0,r0):
  nsNet=[]
  nsSta=[]
  nsDis=[]
  fn='net-sta.csv'
  f=open(fn,'rb')
  drs=csv.reader(f,delimiter=',')

  for r1 in drs:
    lon=float(r1[3])
    lat=float(r1[4])
    s1=math.sqrt((lon0-lon)*(lon0-lon)+(lat0-lat)*(lat0-lat))
    s2=s1*111.11
    if s2<r0:
        #print r1[1],r1[2],s2
        nsNet.append(r1[1])
        nsSta.append(r1[2])
        nsDis.append(s2)
  f.close()
  return (nsNet,nsSta,nsDis)


def getNetSta_net(sNets):
  nsNet=[]
  nsSta=[]
  nsDis=[]
  fn='net-sta.csv'
  f=open(fn,'rb')
  drs=csv.reader(f,delimiter=',')
  sNet=sNets.split('|')
  print sNet
  for r1 in drs:
    s1=r1[1]
    if s1 in sNet:
        nsNet.append(r1[1])
        nsSta.append(r1[2])
        nsDis.append(0.0)
  f.close()
  return (nsNet,nsSta,nsDis)
