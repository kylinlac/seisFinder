import os,sys
#import datetime

sys.path.append("../src")
from edkit import qz


#sDataPath="D:\prjs_github\seisFinder\data"
sDataPath="../data"
sCurrPath=sys.path[0]

zipFile=os.path.join(sDataPath,"qz_sfqz1.zip")

sfqz1File="DYU_60_212_51001_5_2121.sfqz1"
data1=qz.qz_Read_sfml1_inZip(zipFile,sfqz1File)
print("rows: ",len(data1[0]))
#print(data1[:2])
print(data1[0][0])
print(data1[1][0])
print(data1[0][-1])
print(data1[1][-1])
qz_outFile_draw="out_qz\qz_draw_DYU_60_212_51001_5_2121.png"
qz.qzDraw__easy(data1,qz_outFile_draw)


sfqz1File="DYU_60_212_51001_5_2122.sfqz1"
data1=qz.qz_Read_sfml1_inZip(zipFile,sfqz1File)
print("rows: ",len(data1[0]))
#print(data1[:2])
print(data1[0][0])
print(data1[1][0])
print(data1[0][-1])
print(data1[1][-1])
qz_outFile_draw="out_qz\qz_draw_DYU_60_212_51001_5_2122.png"
qz.qzDraw__easy(data1,qz_outFile_draw)






