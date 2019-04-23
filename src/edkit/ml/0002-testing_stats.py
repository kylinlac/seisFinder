import os,sys
import datetime

sys.path.append("..")

import ml

sDataPath="D:\prjs_github\seisFinder\data"
sCurrPath=sys.path[0]


outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)
data1b=ml.mlFilter_sfml2_m(data1,4.9)
dt1=datetime.datetime(2000,1,1,0,0,0)
dt2=datetime.datetime(2004,1,1,0,0,0)
data1c=ml.mlFilter_sfml2_datetime(data1b,dt1,dt2)
datams=ml.ml_Abstract_sfml2_mag(data1c)
print("mean: ",ml.mlCalc_Stats_mean(datams))
print("std: ",ml.mlCalc_Stats_std(datams))
print("var: ",ml.mlCalc_Stats_var(datams))
print("min: ",ml.mlCalc_Stats_min(datams))
print("max: ",ml.mlCalc_Stats_max(datams))
print("count: ",ml.mlCalc_Stats_count(datams))
print("median: ",ml.mlCalc_Stats_median(datams))
print("skew: ",ml.mlCalc_Stats_skew(datams))
print("kurt: ",ml.mlCalc_Stats_kurt(datams))


