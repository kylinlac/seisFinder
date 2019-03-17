import os,sys,time,datetime,stat
import struct
#import multiprocessing as mp

def mseed_btime2pydatetime(btime0):
	#only one call
	year=int(btime0[0])
	nDay=int(btime0[1])
	y0=year-1
	dt0=datetime.datetime(y0,12,31)
	td=datetime.timedelta(days=nDay)
	dt1=dt0+td

	dt9=datetime.datetime(dt1.year,dt1.month,dt1.day,int(btime0[2]),int(btime0[3]),int(btime0[4]),int(btime0[6])*100)
	return dt9

class mseed_record_parser:
	def parse(self,recordBin,dtMin,dtMax):
		#m_recordBin=recordBin
		dataDiff=[]
		dataVal=[]
		dataTime=[]
		dataTimeFlag=[]
	
		#frame0
		sFrame=recordBin[:64]
		(dataBtime,dataOption,dataFirst)=self._parse_frame0(sFrame)
		
		self.time0=mseed_btime2pydatetime(dataBtime)
		
		#if it is out of datetime range ,will return		
		if self.time0 < dtMin :
			return (dataDiff,dataVal,dataTime,dataTimeFlag,False)
		if self.time0 > dtMax:
			return (dataDiff,dataVal,dataTime,dataTimeFlag,False)
		
		##self.time0=mseed_btime2pydatetime(dataBtime)		
		#print self.time0.strftime('%Y-%m-%d %H:%M:%S %f')
		'''
		if 1==1 :
			btime0=dataBtime
			
			year=int(btime0[0])
			nDay=int(btime0[1])
			y0=year-1
			dt0=datetime.datetime(y0,12,31)
			td=datetime.timedelta(days=nDay)
			dt1=dt0+td

			dt9=datetime.datetime(dt1.year,dt1.month,dt1.day,int(btime0[2]),int(btime0[3]),int(btime0[4]),int(btime0[6])*100)
			
			self.time0=dt9
		'''
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
		for i in xrange(0,16):
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
			
		for i in xrange(0,nv):
			vals.append((val>>(bits*i))&m1)
		
		for i in xrange(len(vals)):
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
			
		for i in xrange(0,nv):
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
	
	def parseData(self,dtMin,dtMax):
		idxData=0
		blocksize=512
		self.g_dataDiff=[]
		self.g_dataVal=[]		
		self.g_dataTime=[]
		self.g_dataTimeFlag=[]
		
		#faster little		
		mrs=mseed_record_parser()	
		while 1:
			recordBin=self.dataBin_all[blocksize*idxData:blocksize*(idxData+1)] #seed=4096,mseed=512
			if not recordBin:
				#print "the end..."	
				break;
			
			if recordBin[6]=='D':				
				#mrs=mseed_record_parser()
				(dataDiff,dataVal,dataTime,dataTimeFlag,result)=mrs.parse(recordBin,dtMin,dtMax)
								
				if result==True:
					self.g_dataDiff.extend(dataDiff)
					self.g_dataVal.extend(dataVal)
					self.g_dataTime.extend(dataTime)
					self.g_dataTimeFlag.extend(dataTimeFlag)
						
			idxData=idxData+1	
		self.parse_ok=True		
		

	def _export_part(self,sTrack,sFile,dtMin,dtMax,sRnd):
		if len(self.g_dataVal)>0 :
			#value	
			idx=0
			#f4=open("./web/"+sRnd+"."+sTrack+".dat","wt")
			print sFile
			f4=open(sFile,"wt")
			for v in xrange(len(self.g_dataVal)):
			    #ok
				#f4.write(self.g_dataTimeFlag[v]+" "+self.g_dataTime[v].strftime('%Y-%m-%d %H.%M.%S %f')+" "+str(self.g_dataVal[v])+'\n')
				#f4.write(str(v)+" "+str(self.g_dataVal[v])+'\n')				
				if((self.g_dataTime[v]>=dtMin) and (self.g_dataTime[v]<dtMax)) :
				  f4.write(str(idx/100.0)+" "+str(self.g_dataVal[v])+'\n')				
				  #f4.write(self.g_dataTime[v].strftime('%Y-%m-%d %H:%M:%S.%f')+" "+str(self.g_dataVal[v])+'\n')
				  idx=idx+1
			f4.close()	

	def _export_part_append(self,sFile,sTrack,dtMin,dtMax,sRnd):
		if len(self.g_dataVal)>0 :
			idx=0			
			#f4=open("./web/"+sRnd+"."+sTrack+".dat","a")
			f4=open(sFile,"a")
			for v in xrange(len(self.g_dataVal)):
			    #ok
				#f4.write(self.g_dataTimeFlag[v]+" "+self.g_dataTime[v].strftime('%Y-%m-%d %H.%M.%S %f')+" "+str(self.g_dataVal[v])+'\n')
				#f4.write(str(v)+" "+str(self.g_dataVal[v])+'\n')				
				if((self.g_dataTime[v]>=dtMin) and (self.g_dataTime[v]<dtMax)) :
				  f4.write(str(idx/100.0)+" "+str(self.g_dataVal[v])+'\n')				
				  #f4.write(self.g_dataTime[v].strftime('%Y-%m-%d %H:%M:%S.%f')+" "+str(self.g_dataVal[v])+'\n')
				  idx=idx+1
			f4.close()	
			
