import os,sys
#import datetime

sys.path.append("..")
import mlOne
sys.path.append("../..")
import edkit.ml

#print(dir(edkit.ml)) ok

sDataPath="D:\prjs_github\seisFinder\data"
sCurrPath=sys.path[0]

outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=edkit.ml.ml_Read_sfml2_inZip(outfile_ml_1965)
print(len(data1))

mlOne.ml_Count_day(data1)
