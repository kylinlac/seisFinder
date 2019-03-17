import MySQLdb
import sys,os,datetime,time

def getData(sType,sSta,sPoint,sCode,sSample,sDate0,sDate1,sOutDir):
  sSql="select date0,value0 from qz_%s%s_%s_%s_%s where date0>='%s' and date0<'%s' order by date0" %(sSample,sType,sSta,sPoint,sCode,sDate0,sDate1)
  sPathFile="%s/%s%s-%s_%s_%s.dat" % (sOutDir,sType,sSample,sSta,sPoint,sCode)
  getData1(sSql,sPathFile,1440)

  conn=MySQLdb.connect(host='10.16.160.221',user='root',passwd='sycWEB1234',db='syc_dyu',port=33306)
  cur=conn.cursor()
  
  #count=cur.execute("select date0,value0 from qz_01dyu_53001_2_4112 where date0>='"+sDate0+" ' and date0<'"+sDate1+"' order by date0")
  count=cur.execute(sSql)
  
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
  #sFile="./dyu01/dyu01-53001_2_4112.dat"

  if sSample=="01" :
    getData01(res0,count,sPathFile,60*24)
  
  if sSample=="02" :
    getData01(res0,count,sPathFile,60*60*24)



def getData01(res0,count,sPathFile,nSample):
  sFile=sPathFile
  #os.remove(sFile+".png")
  f=open(sFile,"w")
  for i in range(count):
    dataLine=[]
    dt0=res0[i][0]
    #dt0=datetime.datetime.strptime(sDt0,"%Y-%m-%d")
    data0=res0[i][1]
    dataList=data0.split(' ')
    if len(dataList)==nSample :
      for j in range(nSample):
        if dataList[j]=="NULL" :
          continue
        dt1=dt0+datetime.timedelta(minutes=j)
        dataLine.append(dt1.strftime("%Y %m %d %H %M %S ")+dataList[j]+"\n")
      #print dataLine
      print dt1
      f.writelines(dataLine)

  f.close()
  print "data saved "


def getData02(res0,count,sPathFile,nSample):
  sFile=sPathFile
  #os.remove(sFile+".png")
  f=open(sFile,"w")
  for i in range(count):
    dataLine=[]
    dt0=res0[i][0]
    #dt0=datetime.datetime.strptime(sDt0,"%Y-%m-%d")
    data0=res0[i][1]
    dataList=data0.split(' ')
    if len(dataList)==nSample :
      for j in range(nSample):
        if dataList[j]=="NULL" :
          continue
        dt1=dt0+datetime.timedelta(seconds=j)
        dataLine.append(dt1.strftime("%Y %m %d %H %M %S ")+dataList[j]+"\n")
      #print dataLine
      print dt1
      f.writelines(dataLine)

  f.close()
  print "data saved "


'''
if __name__=="__main__":
  getData("2015-04-01","2016-01-1")
'''

