import os,sys,time,datetime
from SOAPpy import *

endpoint="http://www.ncepe.ac.cn:8080/sycdws/index.php?r=qz/quote&ws=2"
ns="http://tenyears.cn"

class ws_reader:
	def wsData_days(db0,spi0,days,sOutFile):
	  ser=SOAPProxy(endpoint,namespace=ns)
	  data1=ser.qz_getData_days(db0,spi0,days,"20160125130230")
	  if len(data1)>0 :
		#f=open("./"+db0+"/"+db0+"-"+spi0+".dat","wt")
		f=open(sOutFile,"wt")
		f.write(data1)
		f.close()
		print "save data..."
	  else:
		print "miss data..."

	def wsData(db0,spi0,date0,date1,sOutFile):
	  ser=SOAPProxy(endpoint,namespace=ns)
	  data1=ser.qz_getData_v2(db0,spi0,date0,date1,"not","used")
	  if len(data1)>0 :
		#f=open("./"+db0+"/"+db0+"-"+spi0+".dat2","wt")
		f=open(sOutFile,"wt")
		f.write(data1)
		f.close()
		print "save data 2 ..."
	  else:
		print "miss data 2 ..."


			