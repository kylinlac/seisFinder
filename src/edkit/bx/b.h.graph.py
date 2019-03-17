import os,sys,time,datetime,stat
		

def exportGraph(sPathFile,sOutDir,sNet,sSta,sLine):
  sFile=os.path.basename(sPathFile)
  sSubDir="%s.%s.%s" %(sNet,sSta,sLine)
  sOutPathFile=sOutDir+sSubDir+"/"+sFile+".png"

  sPath=sOutDir+sSubDir
  if os.path.exists(sPath)==False:
      os.mkdir(sPath)

  #print sOutPathFile
  s1="set title '%s' font ',10' \n" % sFile
  s2="set terminal png size 900,200 font 'arial,8' \n"
  s3="set output '%s' \n" % sOutPathFile
  s4="set format x '%hs' \n"
  s5="plot '%s' with line lt rgb 'grey' title '' \n" % sPathFile
  sGps="%s%s.gps" % (sOutDir,sFile)
  fg=open(sGps,"wt")
  fg.write(s1)
  fg.write(s2)
  fg.write(s3)
  fg.write(s4)
  fg.write(s5)
  fg.close()

  sCmd="gnuplot %s" % sGps
  os.system(sCmd)

	
def getFiles(sNet,sSta,sLine,sYear):
  sCmd='find ./file_text/h/%s.%s.%s/ -name "*.%s*"'%(sNet,sSta,sLine,sYear)
  print sCmd
  fs=os.popen(sCmd).readlines()
  return fs
	

if __name__=="__main__":
  print "text to graph ..."

  if len(sys.argv)<5:
    print "xxxx -- miss parameter ..."
    sys.exit()

  dt0=datetime.datetime.now()

  sNet=sys.argv[1]
  sSta=sys.argv[2]
  if sSta =="-" :
    sSta=""
  sLine=sys.argv[3]
  sYear=sys.argv[4]
  fs=getFiles(sNet,sSta,sLine,sYear)
  fs.sort()
  sOutDir="./file_graph/h/"
  for i in xrange(len(fs)):
    pf=fs[i].strip("\n")
    print pf
    exportGraph(pf,sOutDir,sNet,sSta,sLine)

  dt1= datetime.datetime.now()
  print
  print len(fs)
  print dt0
  print dt1


