import os,sys
import datetime

sys.path.append("..")

import ml

sDataPath="D:\prjs_github\seisFinder\data"
sCurrPath=sys.path[0]


outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)
print(len(data1))

data1c=ml.mlFilter_sfml2_lonlat(data1,90,110,20,35)
print(len(data1c))
ml_heatmap_count_10="out\ml_heatmap_count10-scyn.png"
ml.mlDraw_Heatmap_count(data1c,ml_heatmap_count_10,90,110,1,20,35,1)
ml_heatmap_count_05="out\ml_heatmap_count05-scyn.png"
ml.mlDraw_Heatmap_count(data1c,ml_heatmap_count_05,90,110,0.5,20,35,0.5)

