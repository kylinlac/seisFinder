import os,sys,time,datetime,stat
import struct
import multiprocessing as mp2

def mseed_btime2pydatetime(btime0):
	year=int(btime0[0])
	nDay=int(btime0[1])
	y0=year-1
	dt0=datetime.datetime(y0,12,31)
	td=datetime.timedelta(days=nDay)
	dt1=dt0+td

	dt9=datetime.datetime(dt1.year,dt1.month,dt1.day,int(btime0[2]),int(btime0[3]),int(btime0[4]),int(btime0[6])*100)
	return dt9

#xx	
class mseed_data_record():
	#only data
	def __init__(self):
		dataDiff=[]
		dataVal=[]
		dataTime=[]
		dataTimeFlag=[]
		x0=0
		x1=0
		#dataBtime
		#dataOption
		#dataFirst
	
class mseed_record_parser:
	def parse(self,recordBin):
		#m_recordBin=recordBin
		self.m_InfoLevel=0
		dataDiff=[]
		dataVal=[]
		dataTime=[]
		dataTimeFlag=[]
	
		#frame0
		sFrame=recordBin[:64]
		(dataBtime,dataOption,dataFirst)=self._parse_frame0(sFrame)
		if self.m_InfoLevel>0:
			print '='*4,(dataFirst),"="*4
		if self.m_InfoLevel>1:
			print 'btime,samplenum:',dataBtime,dataOption
		
		self.time0=mseed_btime2pydatetime(dataBtime)
		#print self.time0.strftime('%Y-%m-%d %H:%M:%S %f')
		#if self.time0<dtMin:
		#	return ([],[],[],[],False)
		#if self.time0>dtMax:
		#	return ([],[],[],[],False)

		#frame1
		sFrame=recordBin[64:128]
		dataBuff=self._parse_frame1(sFrame)
		dataDiff.extend(dataBuff)
		
		#frame2-7
		for i in xrange(2,8): #512/64=8
			sFrame=recordBin[i*64:(i+1)*64]
			(dataBuff,n1)=self._parse_frame(sFrame)
			if n1==0:
				pass
			else:
				dataDiff.extend(dataBuff)
		if self.m_InfoLevel>1:
			print "x0,xn:",x0,xn
			print "datacount(read,get):",dataOption[0],len(dataDiff)
			
		#value from diff
		if len(dataDiff)>0 :
			v=self.x0
			dataVal.append(self.x0)
			dataTime.append(self.time0)
			dataTimeFlag.append('b')
			for i in xrange(1,len(dataDiff)):
				v+=dataDiff[i]
				dataVal.append(v)
				dataTimeFlag.append("m")				
				#hits=100,btime step=10000/hits=100,microseconds step=10000
				msc=10000*i
				msv=msc%1000000
				sv=msc/1000000
				td=datetime.timedelta(seconds=sv,microseconds=msv)	
				dt1=self.time0+td
				dataTime.append(dt1)
			dataTimeFlag[len(dataDiff)-1]='e'
			
		##!!
		#must match for data count
		if len(dataDiff)!=dataOption[0]:
			print "data count from parsing error(fromFile,parse):",dataOption[0],len(dataDiff)
			sys.exit()	
		
		return (dataDiff,dataVal,dataTime,dataTimeFlag,True)
	
	
	def _frame_getW0Ck(self,w0):
		w0ck=[]
		w0b=bin(w0)
		bn=len(w0b)-2 #remove 0b
		ck='0'*(32-bn)+w0b[2:]
		for i in range(0,16):
			w0ck.append(ck[i*2:(i+1)*2])
		return w0ck	
	
	
	def _parse2_Dnib4Ck11(self,val):
		vals=[]
		h2=(val>>30)&0x3
		nv=0; bits=0
		if h2==0: #6bit*5
			bits=6;	nv=5; m1 = 0x0000003f
		
		if h2==1: #5bit*6
			bits=5;	nv=6;	m1 = 0x0000001f
			
		if h2==2: #4bit*7
			bits=4;	nv=7;	m1 = 0x0000000f;
			
		for i in range(0,nv):
			vals.append((val>>(bits*i))&m1)
		
		for i in range(len(vals)):
			if vals[i]>(2**bits)/2:
				vals[i]=vals[i]-(2**bits)
		
		##print valW,bin(valW)
		vals.reverse()
		##print "##(dnib-11)h2,vals:",h2,vals	
		return vals	  			
			
			
	def _parse2_Dnib4Ck10(self,val):
		vals=[]
		h2=(val>>30)&0x3
		nv=0; bits=0
		if h2==1: #30bit*1    ?? ==1
			bits=30;	nv=1;	m1 = 0x3fffffff
			
			#print "30bit:",val,bin(val)
			#sys.exit()
		
		if h2==2: #15bit*2
			bits=15;	nv=2;		m1 = 0x00007fff
			
		if h2==3: #10bit*3
			bits=10;	nv=3;		m1 = 0x000003ff;
			
		for i in range(0,nv):
			vals.append((val>>(bits*i))&m1)
		
		#sign
		for i in xrange(len(vals)):
			if vals[i]>(2**bits)/2:
				vals[i]=vals[i]-(2**bits)
			
		##print valW,bin(valW)
		vals.reverse()
		##print "##(dnib-10)h2,vals:",h2,vals
		return vals
		
		
	def _parse2_Byte1x4(self,val):
		vals=[]
		bits=8;		nv=4;		m1 = 0x000000ff;
			
		for i in xrange(0,nv):
			vals.append((val>>(bits*i))&m1)
		
		for i in xrange(len(vals)):
			if vals[i]>(2**bits)/2:
				vals[i]=vals[i]-(2**bits)
		
		##print valW,bin(valW)
		vals.reverse()
		##print "byte1x4",vals
		return vals	

	
	def _parse_package(self,valW,ck):
		vals0=[]
		if ck=='00':
			pass
			#print "ck=0"
			#sys.exit()
			
		if ck=='01': #1byte*4
			vals0=self._parse2_Byte1x4(valW)
		'''
			#ok,ok, same as cpp code
			sFmt='>bbbb'   #sFmt_byte1='>bbbb'
			valBin=struct.pack('>i',valW) 
			vals=struct.unpack(sFmt,valBin)
			vals0=list(vals)
			print valW
			print "ck,vals",ck,vals
		'''	
		if ck=='10': 	
			vals0=self._parse2_Dnib4Ck10(valW)
		if ck=="11":
			vals0=self._parse2_Dnib4Ck11(valW)
		return vals0
	
		
	#ok
	def _parse_frame0(self,sFrame):
		lineFlag=sFrame[:8]
		lineData=sFrame[8:]

		sSta=lineData[:5]
		sPos=lineData[5:7]
		sChn=lineData[7:10]
		sNet=lineData[10:12]

		sFmtBTime='>HHBBBBH'
		sFmtDataHeader='>HhhBBBBiHH'
		hdrDataBtime=lineData[12:22]
		hdrDataOption=lineData[22:40]
		dataBtime=struct.unpack(sFmtBTime,hdrDataBtime)
		dataOption=struct.unpack(sFmtDataHeader,hdrDataOption)
		return (dataBtime,dataOption,{'sta':sSta,'pos':sPos,'chn':sChn,'net':sNet,'flag':lineFlag})
		
	#ok	
	def _parse_frame1(self,sFrame):
		dataBuff=[]
		Wn=struct.unpack('>Iii'+'i'*13,sFrame)
		w0=Wn[0]
		self.x0=Wn[1]
		self.xn=Wn[2]
		w0ck=self._frame_getW0Ck(w0)
		#print 'w0ck:',w0ck
		#print 'Wn:',Wn
		
		for i in xrange(3,16):
			vals=self._parse_package(Wn[i],w0ck[i])
			if not vals:
				pass
			else:
				dataBuff.extend(vals)
		return dataBuff

		
	def _parse_frame(self,sFrame):
		dataBuff=[]
		Wn=struct.unpack('>I'+'i'*15,sFrame)
		w0=Wn[0]
		#maybe not exist data
		if w0>0 :	
			w0ck=self._frame_getW0Ck(w0)
			#print 'w0',w0ck
			#print 'Wn:',Wn
			
			for i in xrange(1,16):
				vals=self._parse_package(Wn[i],w0ck[i])
				if not vals:
					pass
				else:
					dataBuff.extend(vals)

			return (dataBuff,1)	
		else:
			return (dataBuff,0)
	

class mseed_reader:
	'''
	seed file read/write. 2013-06-20 by WangBin.
	'''
	
	#ok
	def read(self,sFile):
		self.m_mseedfile=sFile
		#try
		f=open(sFile,'rb')
		self.dataBin_all=f.read()
		f.close()
		
		self.g_dataDiff=[]
		self.g_dataVal=[]
		self.g_dataTime=[]
		self.g_dataTimeFlag=[]
		self.read_bin_ok=True
		return True
	
		
	def parseData(self):
		self.m_InfoLevel=0
		idxData=0
		blocksize=512
		self.g_dataDiff=[]
		self.g_dataVal=[]		
		self.g_dataTime=[]
		self.g_dataTimeFlag=[]
		
		while 1:
			recordBin=self.dataBin_all[blocksize*idxData:blocksize*(idxData+1)] #seed=4096,mseed=512
			if not recordBin:
				print "the end..."	
				break;
			
			if recordBin[6]=='D':				
				mrs=mseed_record_parser()
				(dataDiff,dataVal,dataTime,dataTimeFlag,result)=mrs.parse(recordBin)
				
				if result==True:
					self.g_dataDiff.extend(dataDiff)
					self.g_dataVal.extend(dataVal)
					self.g_dataTime.extend(dataTime)
					self.g_dataTimeFlag.extend(dataTimeFlag)
						
			idxData=idxData+1
		
		self.parse_ok=True		
		if self.m_InfoLevel==0:
			print "record,data count:",idxData,len(self.g_dataDiff)
	
	def _export_hour(self,sFile,sOutDir):
		if len(self.g_dataVal)<=0:
			return

		dt0=datetime.datetime.now()
                dd1={}		
		sfs=sFile.split(".")
		#sSubDir="h/%s.%s.%s"%(sfs[0],sfs[1],sfs[3]); #YN.KMI.BHE
		sSubDir="%s.%s.%s"%(sfs[0],sfs[1],sfs[3]); #YN.KMI.BHE
		#sSubDir=""
		if os.path.exists(sOutDir+sSubDir)==False:
			os.mkdir(sOutDir+sSubDir)

                sYjh=self.g_dataTime[0].strftime("%Y.%j.%H")
                #nDay=self.g_dataTime[0].day
                nHour=self.g_dataTime[0].hour
                sKey=".".join([sfs[0],sfs[1],sfs[3],sYjh])
		for v in xrange(len(self.g_dataVal)):
                        #nDay2=self.g_dataTime[v].day
                        nHour2=self.g_dataTime[v].hour
                        #if (nDay != nDay2) :
                        if (nHour!=nHour2):
			    sYjh=self.g_dataTime[v].strftime('%Y.%j.%H')
                            sKey=".".join([sfs[0],sfs[1],sfs[3],sYjh])
                            nHour=nHour2

			# ok sLine=self.g_dataTime[v].strftime("%Y-%m-%d %H.%M.%S %f")+" "+str(self.g_dataVal[v])+"\n"
			#ms=self.g_dataTime[v].strftime("%f")
                        sLine=str(self.g_dataVal[v])+"\n"
			#sLine=self.g_dataTime[v].strftime("%M,%S")+" "+ms[:2]+" "+str(self.g_dataVal[v])+"\n"
			#sKey="%s.%s.%s.%s"%(sfs[0],sfs[1],sfs[3],sYjh)
                        #sKey=".".join([sfs[0],sfs[1],sfs[3],sYjh])
			if sKey in dd1:
				dd1[sKey].append(sLine)
			else:
				dd1[sKey]=[sLine,]
		print "hour: ",len(dd1)

                dt1=datetime.datetime.now()
                
		#ks=dd1.keys()
		for k1 in dd1: #ks
			#print k1
			fo1=open(sOutDir+sSubDir+"/"+k1,"a")
			fo1.writelines(dd1[k1])
			fo1.close()	
                dt2=datetime.datetime.now()
                print dt0
                print dt1,dt1-dt0
                print dt2,dt2-dt1

   	

def exportText(sPathFile,sOutDir):
  msFile=sPathFile
  mseed=mseed_reader()
  mseed.read(msFile)
  mseed.parseData()
  sFile=os.path.basename(sPathFile)
  #print sFile
  #mseed._export_minute(sFile,sOutDir) 

  mseed._export_hour(sFile,sOutDir)

	
def getFiles(sRootDir,sYearMonth):
  #sCmd='find /home/syc/bx/0w/ -name "%s.%s*%s*%s*" | sort '%(sNet,sSta,sLine,sYear)
  sCmd='find %s%s/ -name "*.00.B*" | sort '%(sRootDir,sYearMonth)
  print sCmd
  fs=os.popen(sCmd).read().splitlines()
  return fs
	

if __name__=="__main__":
  print "miniseed to text ..."

  sRoot="/home/syc/bx1/"
  
  if len(sys.argv)<2:
    print "xxxx -- miss parameter ..."
    sys.exit()

  dt0=datetime.datetime.now()
  sYearMonth=sys.argv[1]
  fs=getFiles(sRoot,sYearMonth)
  fs.sort()
  sOutDir=sRoot+sYearMonth+"/d/"
  for i in xrange(len(fs)):
    pf=fs[i]
    print pf
    exportText(pf,sOutDir)

  dt1= datetime.datetime.now()
  print
  print len(fs)
  print dt0
  print dt1
  print "end..."

