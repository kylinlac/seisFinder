import os,sys
#import datetime

sys.path.append("..")

import ml

sDataPath="D:\prjs_github\seisFinder\data"
sCurrPath=sys.path[0]


outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)
print(len(data1))


data1d=ml.mlFilter_sfml2_m(data1,4.4)
hc_outFile_1="out\ml_center01.png"
ml.mlDraw_epicenter__easy(data1d,hc_outFile_1,3)


data1b=ml.mlFilter_sfml2_m(data1,4.9)
print(len(data1b))
#print(data1b[:2])
hc_outFile_2="out\ml_center02.png"
ml.mlDraw_epicenter_withGIS__easy(data1b,hc_outFile_2,1,True)


data1a=ml.mlFilter_sfml2_lonlat(data1b,90,115,15,35)
print(len(data1a))
#print(data1a[:2])
hc_outFile_3="out\ml_center03.png"
ml.mlDraw_epicenter_withGIS__easy(data1a,hc_outFile_3,8,False,85,120,10,40)

