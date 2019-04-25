import os,sys,datetime
import multiprocessing as mp
import file_miniseed

#ok
#sys.path.append('D:\prjs_all\my_app\prjs_edk')

def exportTrack(sTrack,sInDir,sOutDir,sNet,sSta,dtMin,dtMax,sRnd0):
  #sFmt='./wave/%d/%s/%s/'+sTrack+".D/%s.%s.00."+sTrack+".D.%d.%s" #'./wave/2016/SC/CD2/'+sTrack+".D/SC.CD2.00."+sTrack+".D.2016.330"
  #sFmt='c:/pub/pyRds/bx.0/wave/%d/%s/%s/'+sTrack+".D/%s.%s.00."+sTrack+".D.%d.%s" #'./wave/2016/SC/CD2/'+sTrack+".D/SC.CD2.00."+sTrack+".D.2016.330"  
  sFmt=sInDir+'/%d/%s/%s/'+sTrack+".D/%s.%s.00."+sTrack+".D.%d.%s" 
  msFile0=sFmt % (dtMin.year,sNet,sSta,sNet,sSta,dtMin.year,dtMin.strftime("%j"),)
  msFile1=sFmt % (dtMax.year,sNet,sSta,sNet,sSta,dtMax.year,dtMax.strftime("%j"),)
  print msFile0
  print msFile1
  #return
  #msFile='./wave/2016/SC/CD2/'+sTrack+".D/SC.CD2.00."+sTrack+".D.2016.330"
  #sOutFile="./web/"+sRnd+"."+sTrack+".dat";
  sOutFile=sOutDir+"/"+sRnd0+"."+sTrack+".dat";
  #print sOutFile
  #ok
  #mseed=pyedk.bx.fmt.miniseed.mseed_reader()
  mseed=file_miniseed.mseed_reader()
  dt1=datetime.datetime.now()
  print sTrack
  print "begin: ",dt1
  mseed.read(msFile0)
  dt2=datetime.datetime.now()
  print "read finish ...",dt2-dt1
  #mseed.parseData()
  dtMin1=dtMin-datetime.timedelta(seconds=30)
  mseed.parseData(dtMin1,dtMax)
  dt3=datetime.datetime.now()
  print "parse finish...",dt3-dt2
  mseed._export_part(sTrack,sOutFile,dtMin,dtMax,sRnd0) 
  dt4=datetime.datetime.now()
  print "export finish...",dt4-dt3
  
  if msFile0==msFile1 :
    pass
  else:
	  mseed2=file_miniseed.mseed_reader()
	  mseed2.read(msFile1)
	  dtMin1=dtMin-datetime.timedelta(seconds=30)
	  mseed2.parseData(dtMin1,dtMax)
	  mseed2._export_part_append(sTrack,sOutFile,dtMin,dtMax,sRnd0)    
  
  print "end:",sTrack  

def bxGet(sInDir,sOutDir,sNet,sSta,sDt0,sDt1,sOutFilePrefix):
    sRnd=sOutFilePrefix
    print sNet,sSta,sDt0,sDt1,sRnd

    sFmt='%Y-%m-%d_%H:%M:%S'
    dt0a=datetime.datetime.strptime(sDt0,sFmt);
    dt1a=datetime.datetime.strptime(sDt1,sFmt);
    #BJ(+08)->UTC
    dt0=dt0a-datetime.timedelta(hours=8)
    dt1=dt1a-datetime.timedelta(hours=8)
    print str(dt0),str(dt1)
    #return

    #sInDir='c:/pub/pyRds/bx.0/wave'
    #sOutDir='c:/pub/pyRds/bx.0/web'
    exportTrack("BHZ",sInDir,sOutDir,sNet,sSta,dt0,dt1,sRnd)	
    exportTrack("BHE",sInDir,sOutDir,sNet,sSta,dt0,dt1,sRnd)	
    exportTrack("BHN",sInDir,sOutDir,sNet,sSta,dt0,dt1,sRnd)	
	
    ''''
    p1=mp.Process(target=exportTrack,args=("BHZ",sNet,sSta,dt0,dt1,sRnd))
    p2=mp.Process(target=exportTrack,args=("BHE",sNet,sSta,dt0,dt1,sRnd))
    p3=mp.Process(target=exportTrack,args=("BHN",sNet,sSta,dt0,dt1,sRnd))
	
    p1.start()
    p2.start()
    p3.start()
    '''
	
    print "end all ..."


def bxGet_old(rps):
    ps=rps.split("@") #SC@CD2@2016-11-25_22:25:01@2016-11-25_23:45:01@rnd
    sNet=ps[0]	
    sSta=ps[1]
    sDt0=ps[2]
    sDt1=ps[3]	
    sRnd=ps[4]
    print sNet,sSta,sDt0,sDt1,sRnd

    sFmt='%Y-%m-%d_%H:%M:%S'
    dt0a=datetime.datetime.strptime(sDt0,sFmt);
    dt1a=datetime.datetime.strptime(sDt1,sFmt);
    #BJ(+08)->UTC
    dt0=dt0a-datetime.timedelta(hours=8)
    dt1=dt1a-datetime.timedelta(hours=8)
    print str(dt0),str(dt1)
    #return

    sInDir='c:/pub/pyRds/bx.0/wave'
    sOutDir='c:/pub/pyRds/bx.0/web'
    exportTrack("BHZ",sInDir,sOutDir,sNet,sSta,dt0,dt1,sRnd)	
    exportTrack("BHE",sInDir,sOutDir,sNet,sSta,dt0,dt1,sRnd)	
    exportTrack("BHN",sInDir,sOutDir,sNet,sSta,dt0,dt1,sRnd)	
    ''''
    p1=mp.Process(target=exportTrack,args=("BHZ",sNet,sSta,dt0,dt1,sRnd))
    p2=mp.Process(target=exportTrack,args=("BHE",sNet,sSta,dt0,dt1,sRnd))
    p3=mp.Process(target=exportTrack,args=("BHN",sNet,sSta,dt0,dt1,sRnd))
	
    p1.start()
    p2.start()
    p3.start()
    '''
	
    print "end all ..."

#if __name__=="__main__":
	#ok
	#bxGet("SC@CD2@2016-11-25_14:25:30@2016-11-25_15:35:31@1234")
#	bxGet("SC@CD2@2016-11-25_14:00:00@2016-11-25_14:20:00@1234")

def about():
  print "get miniseed data from 204 style file tree ..."

