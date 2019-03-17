import os,sys,time,datetime
import struct

class sac_reader:
	def read(self,sFile):
		f=open(sFile,'rb')
		hdrBin=f.read(632)
		
		sfmt='f'*70+'I '*40+'8s '*22+'16s';	
		hdrFmt=struct.Struct(sfmt)
		self.m_header=hdrFmt.unpack(hdrBin)
		
		npts=int(self.m_header[79])
		fmt_data='f'*npts
		dataFmt=struct.Struct(fmt_data)
		dataBin=f.read(4*npts)
		f.close()
		self.m_data=dataFmt.unpack(dataBin)
		print "data len:",len(self.m_data)
	'''
	def draw(self,sImageFile):
		npts=len(self.m_data)
		xd=range(1,npts+1)
		pylab.figure(1)
		pylab.plot(xd,self.m_data,linewidth=0.3)
		pylab.savefig(sImageFile)
	'''	
	def export_text(self,sOutFile):
		f2=open(sOutFile,"wt")
		sdataAsc=[str(x) for x in self.m_data]
		sDataAsc='\n'.join(sdataAsc)
		f2.writelines(sDataAsc)
		f2.close()
			