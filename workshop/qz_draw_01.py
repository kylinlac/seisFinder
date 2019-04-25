import os,sys
#import datetime

sys.path.append("../src")
from edkit import qz


def draw1(sDir,sSfqz):
    pf=os.path.join(sDataPath,sSfqz)
    data1=qz.qz_Read_sfqz1(pf)
    print(sSfqz)
    print("rows: ",len(data1[0]))
    if len(data1[0]) <=0:
        return

    #print(data1[:2])
    print(data1[0][0])
    print(data1[1][0])
    print(data1[0][-1])
    print(data1[1][-1])
    qz_outFile_draw="out_qz/"+sSfqz+".png"
    qz.qzDraw__easy(data1,qz_outFile_draw)
    print("")


#sDataPath="D:\prjs_github\seisFinder\data"
#sDataPath="../data"
sDataPath="D:/nas_dev/data_seisfinder/qz/01"
sCurrPath=sys.path[0]

fs=os.listdir(sDataPath)
for f1 in fs:
    #pf=os.path.join(sDataPath,f1)
    #print(pf)
    draw1(sDataPath,f1)









