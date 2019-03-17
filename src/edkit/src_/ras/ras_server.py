import time
import sys
import datetime

class rasMessage:
  'ras message class'

  def get(self):
    print 'check ...',
    print 'get ...',
    print 'move ...'
    return []
  
  def get1(self):
    print 'check ...',
    print 'get ...',
    print 'move ...'
    return ['op_double','para1','para2','para3','para4','para5']

	
class rasTask:
  'ras sub task class'
  taskName='ras task'  
  beginDatetime=datetime.datetime.now()
  
  #??
  #def __init__(self):
  #  self.beginDatetime=datetime.datetime.now()
  
  def getName(self):
    return self.taskName

  def setName(self,sName):
    self.taskName=sName
	
  def getBeginDatetime(self):
    return self.beginDatetime
	

class myTask01(rasTask):
  'my task 01 ...'

  data0=[]
  
  def __init__(self,sTaskName):
    self.setName(sTaskName)
	
  def setData(self):
    self.data0=[1,2,4,6,8,4]
    
  def run(self,sCmd):
    print 'origin data',self.data0
    print "cmd line : ",sCmd
    if(sCmd[0]=="op_double"):
      self.op_double()    

  def op_double(self):
    #data1=[x*2.0 for x in self.data0]
    #self.data0=data1
    self.data0=[x*2.0 for x in self.data0]
    print "result : ",self.data0    
	
	
class rasServer:
  'ras server class'

  #run_stage=['idle','runFunction','peekMessage']
  lifeStop=0 #default: 1 hour =3600 second
  run_stage=['message','task']

  def about(self):
    print "About pyedk ras server ... 2016.04.23"
  
  def run(self):
    'main function to run always ...'
	
	#init status	
    gRunStage=self.run_stage[0]	
    task0=myTask01("task01...")
    task0.setData();
	
    idx0=0
    while(1):
      print idx0,".",gRunStage,' - ',
	  
	  #get message
      rm=rasMessage();

      # test @@@@
      tps=[]
      if idx0==40 :
        tps=rm.get1();
      else:
        tps=rm.get();      
	  
      if len(tps)>0:
        print 'task name : ',task0.getName()
        print 'task begin datetime : ',task0.getBeginDatetime()
        task0.run(tps)
        #task0.op_double()
		
      else:
        print "skip ..."
	  
	  # formal value is 1 second
      time.sleep(1) #unit is second
      idx0=idx0+1
	  
	  #run forever
      if self.lifeStop < 1:
        continue
	  
      if idx0>self.lifeStop :
        print ''
        print 'exit:',idx0
        sys.exit()
	
	
  
  