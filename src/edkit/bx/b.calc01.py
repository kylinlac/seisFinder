import sys,os,time,datetime
import numpy as np

def getFeature(ovs,sName):
    #ovs=np.ones(len(vs),np.integer)
    #for i in xrange(len(vs)):
    #    ovs[i]=vs[i]    
    r=0.0
    if sName=="mean" :
        r=ovs.mean()
    elif sName=="std":
        r=ovs.std()
    elif sName=="var":
        r=ovs.var()
    elif sName=="min":
        r=ovs.min()
    elif sName=="max":
        r=ovs.max()
    elif sName=="count":
        r=len(ovs)
    else:
        r=0.0

    return str(r)


def readFile(fn):
    '''
    0.6s
    
    vs=open(fn,"rt").read().splitlines()
    print fn
    #return vls
    ovs=np.ones(len(vs),np.integer)
    for i in xrange(len(vs)):
        ovs[i]=vs[i]
    return ovs
	'''	
	ovs=np.loadtxt(fn)
	print fn
	return ovs
	
def getFiles(sHit,sNet,sSta,sLine):
    sCmd="find ./%s/%s.%s.%s/ -type f -name '%s.*' | sort " % (sHit,sNet,sSta,sLine,sNet)
    print sCmd
    pfs=os.popen(sCmd).read().splitlines()
    return pfs


if __name__=="__main__":
    #sFn="./PZH.BHZ/PZH.BHZ.2016.365.dat01"
    if len(sys.argv)<6:
      print "miss file name"
      sys.exit()

    sNet=sys.argv[1]
    sSta=sys.argv[2]
    sLine=sys.argv[3]
    sHit=sys.argv[4]
    sName=sys.argv[5]

    #sFo="%s.%s.%s.%s_%s" % (sNet,sSta,sLine,sHit,sName)
    #print sFo
    pfs=getFiles(sHit,sNet,sSta,sLine)

    dt0=datetime.datetime.now()

    #res=[ os.path.basename(sFn)+","+getFeatures(readFile(sFn),sName)+"\n"  for sFn in pfs ]

    sns=sName.split(",")
    print sns
    #sys.exit()

    dds={}
    for sFn in pfs:
        ovs=readFile(sFn)
        for i in xrange(len(sns)):
            sName=sns[i]
            r=getFeature(ovs,sName);
            sVal=os.path.basename(sFn)+","+r+"\n"
            if sName in dds:
                dds[sName].append(sVal)
            else:
                dds[sName]=[]
                dds[sName].append(sVal)

    for i in xrange(len(sns)):
        sName=sns[i]
        sFo="%s.%s.%s.%s_%s" % (sNet,sSta,sLine,sHit,sName)
        print sFo

        fo=open(sFo,"wt")
        fo.writelines(dds[sName])
        fo.close()

    dt1=datetime.datetime.now()
    print
    print dt0,dt1,dt1-dt0
    

