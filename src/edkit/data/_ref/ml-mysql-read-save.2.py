import os,sys,time
import glob
import shutil
import MySQLdb

import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  

def mailSeis(sInfo):
	str=sInfo
	print "mail: ",sInfo
	
	sender = 'wb@cea-ies.ac.cn'  
	receiver = 'wjb801@wo.com.cn'  
	subject =str  #'24-day'  
	smtpserver = 'mail.cea-ies.ac.cn'  
	username = 'wb@cea-ies.ac.cn'  
	password = 'zxc091MNB'  
	  
	msg = MIMEText('A New Earthquake is coming ...','text','utf-8')
	msg['Subject'] = Header(subject, 'utf-8')  
	  
	smtp = smtplib.SMTP()  
	smtp.connect('mail.cea-ies.ac.cn')  
	smtp.login(username, password)  
	smtp.sendmail(sender, receiver, msg.as_string())  
	smtp.quit() 

	
def mailSeis2(sInfo):
	str=sInfo
	print "mail: ",sInfo
	
	sender = 'wb@seis.ac.cn'  
	receiver = 'wjb801@wo.com.cn'  
	subject =str  #'24-day'  
	smtpserver = 'mail.seis.ac.cn'  
	username = 'wb@seis.ac.cn'  
	password = 'zxc091MNB'  
	  
	msg = MIMEText('A New Earthquake is coming ...','text','utf-8')
	msg['Subject'] = Header(subject, 'utf-8')  
	  
	smtp = smtplib.SMTP()  
	smtp.connect('mail.seis.ac.cn')  
	smtp.login(username, password)  
	smtp.sendmail(sender, receiver, msg.as_string())  
	smtp.quit() 

	
def parseSeis(sXmlFile):
	#print "xml...",sXmlFile
	sData=open(sXmlFile,'rt').read()
	#print sData
	
	#network
	#ok
	idx0=sData.find('NETWORK')
	idx1=sData.find('/',idx0)
	sNet=sData[idx0:idx1]
	#print sNet
	
	#catlog 
	idx0=sData.find('CATLOG')
	idx1=sData.find('/',idx0)
	sCat=sData[idx0:idx1]
	#print idx0,idx1
	#print sCat
	
	#sc_id
	idx0=sCat.find('Cata_id')
	idx1=sCat.find(' ',idx0)
	sId=sCat[(idx0+9):(idx1-1)]
	#print sId
	
	#sc_datetime2
	idx0=sCat.find('O_time')
	idx1=sCat.find(' ',idx0)
	sDt2=sCat[(idx0+8):(idx1-1)]
	#print sDt2
	
	#sc_lat
	idx0=sCat.find('Lat')
	idx1=sCat.find(' ',idx0)
	sLat=sCat[(idx0+5):(idx1-1)]
	#print sLat
	
	#sc_lon
	idx0=sCat.find('Lon')
	idx1=sCat.find(' ',idx0)
	sLon=sCat[(idx0+5):(idx1-1)]
	#print sLon
		
	#sc_depth
	idx0=sCat.find('Depth')
	idx1=sCat.find(' ',idx0)
	sDepth=sCat[(idx0+7):(idx1-1)]
	#print sDepth

	#sc_m
	idx0=sCat.find('M=')
	idx1=sCat.find(' ',idx0)
	sM=sCat[(idx0+3):(idx1-1)]
	#print sM

	#sc_place
	idx0=sCat.find('Location_cname')
	idx1=sCat.find(' ',idx0)
	sPlace=sCat[(idx0+16):(idx1-1)]
	#print sPlace
	
	#** m value must big than 2.9
	#check out
	return (sId,sDt2,sLon,sLat,sM,sDepth,sPlace)

def datetimeFormat(sDt2):
	#20150425204406.440
	#2015-04-25 20:44:06.440
	sDt='%s-%s-%s %s:%s:%s'%(sDt2[0:4],sDt2[4:6],sDt2[6:8],sDt2[8:10],sDt2[10:12],sDt2[12:])
	return sDt
	
def readSeis():
	print "read ..."
	fs=glob.glob('*.1');
	print 'xmls: ',len(fs)
	#print fs	
	
	db = MySQLdb.connect("localhost","root","sycWEB1234","syc_web",charset ='utf8')
	#db = MySQLdb.connect("10.16.160.222","root","sycWEB1234","syc_web",charset ='utf8')
	cursor = db.cursor()	
	
	for fn1 in fs:
		print 'xml: ',fn1 
		#time.sleep(2) #ok
		#print fn1
		sId,sDt2,sLon,sLat,sM,sDepth,sPlace=parseSeis(fn1)

		print "%s,%s"%(sId,sM)		
		if sM<'1.0' :
			print "error..."
			print ""
			sErrorFile='_error/%s' % fn1
			shutil.move(fn1,sErrorFile)			
			continue
		#else:
			#print "save %s,%s"%(sId,sM)
			#print ""
			
		#print type(sPlace)
		
		sDt=datetimeFormat(sDt2)
		#print sDt
		
		#ok
		#sPlace2=unicode(sPlace,'gbk')
		#ok
		sPlace2=sPlace.decode('gbk')		
		#print type(sPlace2)
		#sPlace3=sPlace2.encode('utf8')
		#print type(sPlace3) #it is str. why??
		
		#check
		sql2="select scid,sc_id from tb_seis where sc_id='%s'" % (sId)
		cursor.execute(sql2)
		#data=cursor.fetchone()
		rows=cursor.fetchall()
		if len(rows)>0:
			print "skip: duplicate ..."
			for row in rows:
				print row			
			print ''
			
			sErrorFile='_more/%s' % fn1
			shutil.move(fn1,sErrorFile)			
					
			continue
		else:
			print "new..."
				
		#ok, chinese name is ok
		sql = "INSERT INTO tb_seis(sc_id,sc_datetime,sc_datetime2,sc_lon,sc_lat,sc_m,sc_depth,sc_place,sc_geom) \
		VALUES('%s','%s','%s',%s,%s,%s,%s,'%s',GeomFromText(\'POINT\(%s %s\)\') )" % (sId,sDt,sDt2,sLon,sLat,sM,sDepth,sPlace2,sLon,sLat)
		#sql.decode('utf8')

		#print sql
		
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()		

		print "save to db: %s,%s"%(sId,sM)			
		
		sOldFile='_old/%s' % fn1
		shutil.move(fn1,sOldFile)
		
		#sInfo="%s,Ms%s,%s"%(sDt2,sM,sPlace2)
		#mailSeis2(sInfo)				
		
		print ''
		print ''
		
	db.close()			
	
	
if __name__=="__main__":
	readSeis()
	
	
	