import os,sys
import datetime

sys.path.append("../src")
from edkit import ml,one_stats

#sDataPath="D:\prjs_github\seisFinder\data"
sDataPath="../data"
sCurrPath=sys.path[0]


outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)

data1b=ml.mlFilter_sfml2_m(data1,4.9)
dt1=datetime.datetime(2000,1,1,0,0,0)
dt2=datetime.datetime(2004,1,1,0,0,0)
data1c=ml.mlFilter_sfml2_datetime(data1b,dt1,dt2)

datams=ml.ml_Abstract_sfml2_mag(data1c)

print("mean: ",one_stats.sfStats_mean(datams))
print("std: ",one_stats.sfStats_std(datams))
print("var: ",one_stats.sfStats_var(datams))
print("min: ",one_stats.sfStats_min(datams))
print("max: ",one_stats.sfStats_max(datams))
print("count: ",one_stats.sfStats_count(datams))
print("median: ",one_stats.sfStats_median(datams))
print("skew: ",one_stats.sfStats_skew(datams))
print("kurt: ",one_stats.sfStats_kurt(datams))


