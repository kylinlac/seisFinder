import os,sys,time,datetime
import MySQLdb
from SOAPpy import *

import matplotlib
matplotlib.use('agg')
#matplotlib.style.use('ggplot')

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

import tornado.ioloop
import tornado.web

endpoint="http://www.ncepe.ac.cn:8080/sycdws/index.php?r=qz/quote&ws=2"
ns="http://tenyears.cn"

def wsData(db0,spi0,days):
  ser=SOAPProxy(endpoint,namespace=ns)
  data1=ser.qz_getData_days(db0,spi0,days,"20160125130230")
  if len(data1)>0 :
    f=open("./"+db0+"/"+db0+"-"+spi0+".dat","wt")
    f.write(data1)
    f.close()
    print "save data..."
  else:
    print "miss data..."

def wsDown(db0,spi0,date0,date1):
  ser=SOAPProxy(endpoint,namespace=ns)
  data1=ser.qz_getData_v2(db0,spi0,date0,date1,"not","used")
  if len(data1)>0 :
    f=open("./"+db0+"/"+db0+"-"+spi0+".dat2","wt")
    f.write(data1)
    f.close()
    print "save data 2 ..."
  else:
    print "miss data 2 ..."

def getDataFromDb(db0,spi0,sDate0,sDate1,sRnd0):
  conn=MySQLdb.connect(host='10.16.160.221',user='root',passwd='sycWEB1234',db='syc_dyu',port=33306)
  cur=conn.cursor()

  sSql="select date0,value0 from qz_01dyu_53001_2_4112 where date0>'"+sDate0+"' and date0<'"+sDate1+"' order by date0"
  count=cur.execute(sSql)
  res0=cur.fetchall()
  cur.close()
  conn.close()

  sFile='./dyu01/dyu01-53001_2_4112.'+sRnd0+'.dat'
  if os.path.exists(sFile+".png") :
    os.remove(sFile+".png")
  f=open(sFile,"w")
  for i in range(count):
    dataLine=[]
    dt0=res0[i][0]
    data0=res0[i][1]
    dataList=data0.split(' ')
    if len(dataList)==1440 :
      for j in range(1440):
        if dataList[j]=="NULL": 
          continue
        dt1=dt0+datetime.timedelta(minutes=j)
        dataLine.append(dt1.strftime("%Y %m %d %H %M %S ")+dataList[j]+"\n")
      f.writelines(dataLine)
  f.close()
  print "data exported ..."


def draw1(file1):
  f=open(file1,"rt")
  d1=f.readlines()
  f.close()

  #print "drawing ",file1

  dts=[]
  data1=[]
  for i in range(len(d1)):
    d1a=d1[i].split(' ')

    if len(d1a)<7 :
      continue

    if d1a[6]=="\n":
      continue

    if d1a[6]=="null\n":
      continue

    if d1a[6]=="NULL\n":
      continue

    if d1a[6]=="Null\n":
      cointinue

    #print d1a
    dt0=pd.Timestamp(datetime.datetime(int(d1a[0]),int(d1a[1]),int(d1a[2]),int(d1a[3]),int(d1a[4]),int(d1a[5])))
    dts.append(dt0)
    data1.append(float(d1a[6]))
    #print dt0

  dc=len(dts)
  if dc<=0:
    return

  ts1=pd.Series(data1,dts)
  matplotlib.pyplot.figure()
  ts1.plot(figsize=(7,3),fontsize=9,linewidth=0.5)
  #plt.xlabel("time")  #ok,but extent to windows
  plt.ylabel("value")
  #plt.title(file1)

  date_format=matplotlib.dates.DateFormatter('%Y-%m-%d')
  ax=plt.gca()
  #ax.xaxis.set_major_formatter(date_format)  

  plt.savefig(file1+".png")
  #print "drawing ",file1
  #print dt0
  plt.cla()
  plt.clf()

def getFiles(sDir):
  fs=glob.glob(sDir+"/dyu*.dat")
  #print fs
  return fs	
	
class indexHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello,Qz Data Graph ...")

class qzHandler(tornado.web.RequestHandler):
  def get(self,rps):
    #self.write("spi@date0@date1@01",rps)
    print "data begin"
    wsData("dyu01","53001_2_4112",60)
    #wsDown("dyu01","53001_2_4112","2015-01-01","2015-01-31")
    print "data end"
	
    print "graph begin"
    fs0=getFiles("./dyu01")
    for i in range(len(fs0)):
      draw1(fs0[i])
    print "graph end"
	
class qz2Handler(tornado.web.RequestHandler):
  def get(self,rps):
    self.write("get data to draw from redis: "+rps)
    ps=rps.split("@")
    sDb=ps[3]
    sDate0=ps[1]
    sDate1=ps[2]
    sSpi=ps[0]
    sRnd=ps[4]
    print sDb,sDate0,sDate1,sSpi,sRnd
    #wsData(sDb,sSpi,10)
    getDataFromDb(sDb,sSpi,sDate0,sDate1,sRnd)
    fs0=getFiles("./"+sDb)
    for i in range(len(fs0)):
      draw1(fs0[i])
      os.remove(fs0[i])
    print "end"
    self.write("end")

	
application=tornado.web.Application([
(r"/",indexHandler),
(r"/qz/([0-9]{5}_[0-9]_[0-9]{4}@20[0-1][0-9]{,2}-[0-9]{,2}@20[0-1][0-9]-[0-9]{,2}-[0-9]{,2}@dyu01)",qzHandler),
#(r"/qz2/([0-9]{5}-[0-9]-[0-9]{4}@20[0-1][0-9]{,2}-[0-9]{,2}@20[0-1][0-9]-[0-9]{,2}-[0-9]{,2}@dyu01)",qz2Handler),
(r"/qz2/(.+)",qz2Handler),
])

if __name__=="__main__":
  print "launch web 8081 ..."
  application.listen(8081)
  tornado.ioloop.IOLoop.instance().start()



