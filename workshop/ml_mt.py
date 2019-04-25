import os,sys
import datetime

#ok
#sys.path.append("../src/edkit")
#import ml

#ok too
sys.path.append("../src")
from edkit import ml


#sDataPath="D:\prjs_github\seisFinder\data"
sDataPath="../data"
sCurrPath=sys.path[0]

outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)
print(len(data1))

data1b=ml.mlFilter_sfml2_m(data1,4.9)
ml_outFile_mt_1="out_ml/ml_mt01.png"
ml.mlDraw_mt__easy(data1b,ml_outFile_mt_1)

dt1=datetime.datetime(2000,1,1,0,0,0)
dt2=datetime.datetime(2004,1,1,0,0,0)
data1c=ml.mlFilter_sfml2_datetime(data1b,dt1,dt2)
print(len(data1c))
print(data1c[:2])
ml_outFile_mt_1="out_ml/ml_mt02.png"
ml.mlDraw_mt__easy(data1c,ml_outFile_mt_1)