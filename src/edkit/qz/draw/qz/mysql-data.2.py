import MySQLdb
import sys,os,datetime,time

def getData(sDate0,sDate1):
  conn=MySQLdb.connect(host='10.16.160.221',user='root',passwd='sycWEB1234',db='syc_dyu',port=33306)
  cur=conn.cursor()
  
  count=cur.execute("select date0,value0 from qz_01dyu_53001_2_4112 where date0>='"+sDate0+" ' and date0<'"+sDate1+"' order by date0")
  print "rows: %s" % count
  #res1=cur.fetchone()
  #print res1
  #res3=cur.fetchmany(3)
  #print res3
  res0=cur.fetchall()
  #print res0
  cur.close()
  conn.close()

  print
  #print res0[0][0],res0[0][1]
  sFile="./dyu01/dyu01-53001_2_4112.dat"
  os.remove(sFile+".png")
  f=open(sFile,"w")
  for i in range(count):
    #print res0[i][0]
    dataLine=[]
    dt0=res0[i][0]
    #dt0=datetime.datetime.strptime(sDt0,"%Y-%m-%d")
    #print dt0
    #print type(dt0)
    data0=res0[i][1]
    dataList=data0.split(' ')
    #print dataList
    #print len(dataList)
    
    #sFile="./dyu01_53001_2_4112.dat"
    #f=open(sFile,"wt")
    if len(dataList)==1440 :
      for j in range(1440):
        if dataList[j]=="NULL" :
          continue
        dt1=dt0+datetime.timedelta(minutes=j)
        dataLine.append(dt1.strftime("%Y %m %d %H %M %S ")+dataList[j]+"\n")
      #print dataLine
      print dt1
      f.writelines(dataLine)

  f.close()
  print "data saved "

if __name__=="__main__":
  getData("2015-04-01","2016-01-1")


