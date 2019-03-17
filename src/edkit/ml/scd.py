#地震目录处理模块
#--统计

import os,sys
import matplotlib as mpl
import pylab as pl
#from matplotlib import *

scdFields={'fieldYear' : 0,'fieldMonth' : 1,'fieldDay':2,'fieldHour':3,'fieldMinute':4,
'fieldSecond':5,'fieldLon':6,'fieldLat':7,'fieldMs':8,'fieldDepth':9}

class scdKit():

  def read(self):
    '''
	  读入文件，基于逗号分隔数据格式，秒是4位小数，例如：
	  1970,07,02,05,35,43.0000,100.700000,27.600000,3.40,0.0000
    '''
    f1=open("ms2.scd.txt")
    self.ds=f1.readlines()
    f1.close()
    #sample_list = [line+'\n' for line in sample_list]
    self.ds2=[line.rstrip('\n') for line in self.ds]
    self.ds3=[line.split(',') for line in self.ds2]    
    print( len(self.ds))
    print( self.ds[0])
    print( self.ds2[0])
    print( self.ds3[0] )   

  def plotMsCount(self,mStep=0.1,sSuffix="10",bShowFigure=True,bSaveFigure=True,bSaveData=True):
    '''
	震级区间内的地震数量，
	'''
    ms=[]
    dcs=[]
    
	#建立分档x
    mmin=0.0
    mmax=10.0
    vc=(mmax)/mStep+1
    #for i in range(mmin,mmax+mStep,mStep):
    #  ms.append(i)
    #  dcs.append(0)
    ms = pl.linspace(mmin, mmax,vc) 
    for i in range(len(ms)):
      dcs.append(0)
    
    print(len(ms),ms)
    print( len(dcs),dcs)
    
    idx=0
    #m0=0.0
    for i in range(len(self.ds)):
      #print self.ds[i]
      d1=self.ds[i].split(',')
      #ok
      #idx=int(float(d1[8])/mStep)
      idx=int(float(self.ds3[i][ scdFields['fieldMs'] ])/mStep)
      #dcs[idx-m0]=dcs[idx-m0]+1
      dcs[idx]=dcs[idx]+1
    
    print( sum(dcs),dcs)

	#绘图支持中文
    mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题	
	
    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    #ok
    pl.plot(ms,dcs)
    pl.xticks([x for x in range(11)])  #x标记step设置为1
	#plt.yticks([y for y in range(max(ys) + 1)]) 
    #pl.bar(ms,dcs, align='center') 显示效果不好
    #ok
    #pl.bar(years,dcs)
    pl.xlabel(u'震级',fontsize=16)
    pl.ylabel(u'数量',fontsize=16) #?不能标注中文
    #ok
    #pl.show()
    pl.savefig('msCount_'+sSuffix+'.png', dpi = 72)
    '''
    res=zip(ms,dcs)
    print res
    #print type(res) ok
    
    res2=[','.join(line) for line in res]    
    print res2[1]
    '''
    
    res=[]
    for i in range(len(ms)):
        res.append(str(ms[i])+','+str(dcs[i])+'\n')
    
    f2=open("msCount_"+sSuffix+".res.txt","w")
    f2.writelines(res)
    f2.close()
    
  def plotHourCount(self):
    months=[]
    dcs=[]

    ymin=1
    ymax=24
    for i in range(ymin,ymax+1):
      months.append(i)
      dcs.append(0)
      
    print(len(months),months)
    print(len(dcs),dcs)
    
    idx=0
    for i in range(len(self.ds)):
      d1=self.ds[i].split(',')
      idx=int(d1[ scdFields['fieldHour'] ])
      dcs[idx-1]=dcs[idx-1]+1
    
    print(sum(dcs),dcs)

    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    #ok
    pl.plot(months,dcs)
    #ok
    #pl.bar(years,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('hour',fontsize=16)
    pl.gca().lines[0].set_color('r')
    #ok
    #pl.show()
    pl.savefig('hourCount.png', dpi = 72)
    
    res=[]
    for i in range(len(months)):
        res.append(str(months[i])+','+str(dcs[i])+'\n')
    
    f2=open("hourCount.res.txt","w")
    f2.writelines(res)
    f2.close()     
    
  def plotDayCount(self):
    months=[]
    dcs=[]

    ymin=1
    ymax=31
    for i in range(ymin,ymax+1):
      months.append(i)
      dcs.append(0)
      
    print(len(months),months)
    print(len(dcs),dcs)
    
    idx=0
    for i in range(len(self.ds)):
      d1=self.ds[i].split(',')
      idx=int(d1[scdFields['fieldDay']])
      dcs[idx-1]=dcs[idx-1]+1
    
    print(sum(dcs),dcs)

    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    #ok
    pl.plot(months,dcs)
    #ok
    #pl.bar(years,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('day',fontsize=16)
    pl.gca().lines[0].set_color('r')
    #ok
    #pl.show()
    pl.savefig('dayCount.png', dpi = 72)
    
    res=[]
    for i in range(len(months)):
        res.append(str(months[i])+','+str(dcs[i])+'\n')
    
    f2=open("dayCount.res.txt","w")
    f2.writelines(res)
    f2.close()        
        
    
  def plotMonthCount(self):
    months=[]
    dcs=[]

    ymin=1
    ymax=12
    for i in range(ymin,ymax+1):
      months.append(i)
      dcs.append(0)
      
    print(len(months),months)
    print(len(dcs),dcs)
    
    idx=0
    for i in range(len(self.ds)):
      d1=self.ds[i].split(',')
      idx=int(d1[scdFields['fieldMonth']])
      dcs[idx-1]=dcs[idx-1]+1
    
    print(sum(dcs),dcs)

    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    #ok
    pl.plot(months,dcs)
    #ok
    #pl.bar(years,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('month',fontsize=16)
    #ok
    #pl.show()
    pl.savefig('monthCount.png', dpi = 72)
    
    res=[]
    for i in range(len(months)):
        res.append(str(months[i])+','+str(dcs[i])+'\n')
    
    f2=open("monthCount.res.txt","w")
    f2.writelines(res)
    f2.close()        
        
  
  def plotYearCount(self):
    years=[]
    dcs=[]
    '''
    for i in range(len(self.ds)):
      #print self.ds[i]
      d1=self.ds[i].split(',')
      dsyc[ d1[0] ]=0
    '''

    ymin=int(self.ds[0].split(',')[0])
    ymax=int(self.ds[len(self.ds)-1].split(',')[0])
    for i in range(ymin,ymax+1):
      years.append(i)
      dcs.append(0)
      
    print(len(years),years)
    print(len(dcs),dcs)
    
    idx=0
    year0=ymin
    for i in range(len(self.ds)):
      #print self.ds[i]
      d1=self.ds[i].split(',')
      idx=int(d1[ scdFields['fieldYear'] ])
      dcs[idx-year0]=dcs[idx-year0]+1
    
    print(sum(dcs),dcs)

    dpi=72.0
    xpixels=1024.0
    ypixels=512.0
    xin=xpixels/dpi
    yin=ypixels/dpi    
    pl.figure(figsize=(xin,yin))
    
    #ok
    pl.plot(years,dcs)
    #ok
    #pl.bar(years,dcs)
    pl.xlabel('count',fontsize=16)
    pl.ylabel('year',fontsize=16)
    #ok
    #pl.show()
    pl.savefig('yearCount.png', dpi = 72)
    
    res=[]
    for i in range(len(years)):
        res.append(str(years[i])+','+str(dcs[i])+'\n')
    
    f2=open("yearCount.res.txt","w")
    f2.writelines(res)
    f2.close()    
    
  def plotYearCount_old(self):
    dsyc={}
    '''
    for i in range(len(self.ds)):
      #print self.ds[i]
      d1=self.ds[i].split(',')
      dsyc[ d1[0] ]=0
    '''

    ymin=int(self.ds[0].split(',')[0])
    ymax=int(self.ds[len(self.ds)-1].split(',')[0])
    for i in range(ymin,ymax+1):
      #print self.ds[i]
      dsyc[i]=0
      print(i)
    
    idx=0
    for i in range(len(self.ds)):
      #print self.ds[i]
      d1=self.ds[i].split(',')
      idx=int(d1[0])
      dsyc[idx]=dsyc[idx]+1
    
    print(dsyc)



if __name__=="__main__":
  print("begin...")
  
  scd=scdKit()
  scd.read()
  
  #ok
  scd.plotYearCount()
  scd.plotMonthCount()    
  scd.plotDayCount()  
  scd.plotHourCount() 
  
  #ok: 0.1 0.2 0.5 1.0 2.0
  # not good: 0.1,0.2 plot
  scd.plotMsCount(0.5,"05")
  scd.plotMsCount(1.0,"10")
  
  
  print("end ...")
