import os,sys
import datetime

sys.path.append("..")
import bx

#sDataPath="D:\prjs_github\seisFinder\data"
#sCurrPath=sys.path[0]

#zipFile=os.path.join(sDataPath,"qz_sfqz1.zip")


nsd=bx.ml_Read_Net_Station()
#print(nsd)

n=bx.ml_getNets()
#print(n)

s=bx.ml_getStations()
#print(s)

sn=bx.ml_getStations_byNets("AH|BJ")
#print(sn)
sn=bx.ml_getStations_byNets("YN|SC")
#print(sn)

sn=bx.ml_getStations_byArea()
#print(sn)

sn=bx.ml_getStations_byCircle(116.0,39.0,100.0)
#print(sn)

s=bx.ml_getStations()
cn=bx.ml_Stations_getNameCn(s)
#print(s)
#print(cn)

s=bx.ml_getStations()
pos=bx.ml_Stations_getPosition(s)
print(s)
print(pos)