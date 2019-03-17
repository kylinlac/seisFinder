import os,sys,time
from SOAPpy import *
import MySQLdb

#def wsData(db0,spi0,days):
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

if __name__=="__main__":
  print "begin"
  wsData("dyu01","53001_2_4112",60)
  wsDown("dyu01","53001_2_4112","2015-01-01","2015-01-31")
  print "end"

