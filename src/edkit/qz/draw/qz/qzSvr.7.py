import os,sys,time,datetime
import MySQLdb
from SOAPpy import *
import glob
import stat

import tornado.ioloop
import tornado.web

def getDataFromDb(db0,spi0,sDate0,sDate1,sRnd0):
  conn=MySQLdb.connect(host='10.16.160.221',user='root',passwd='sycWEB1234',db='syc_dyu',port=33306)
  cur=conn.cursor()

  sSql="select date0,value0 from qz_01dyu_53001_2_4112 where date0>='"+sDate0+"' and date0<'"+sDate1+"' order by date0"
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


def drawGnuplot(file1,sRnd0):
  sOut="set output '"+file1+".png'\n"
  sDraw="plot '"+file1+"' using 1:7 with line title '53001-2-4112'\n"
  cmdLines=["set xdata time\n","set timefmt '%Y %m %d %H %M %S'\n","set format x '%Y-%m-%d'\n","set title 'dyu01-53001-2-4112'\n","set xtics rotate by -45\n","set terminal png size 800,300 font 'arial,8'\n",sOut,sDraw]
  sGps="./dyu01/"+sRnd0+".gps"
  f=open(sGps,"w")
  f.writelines(cmdLines)
  f.close()
  #os.system("gnuplot "+sGps)
  sCmd1="gnuplot "+sGps
  sCmd2="touch ./dyu01/"+sRnd0+".ok"
  sShell="./dyu01/"+sRnd0+".sh"
  f=open(sShell,"w")
  f.write(sCmd1)
  f.write("\n")
  f.write(sCmd2)
  f.close()
  os.chmod(sShell,stat.S_IXOTH)
  os.system(sShell)

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
    #fs0=getFiles("./"+sDb)
    #for i in range(len(fs0)):
    #  drawGnuplot(fs0[i],sRnd)
    #  #os.remove(fs0[i])
    sDataFile="./dyu01/dyu01-53001_2_4112."+sRnd+".dat";
    drawGnuplot(sDataFile,sRnd)
    print "end"

	
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



