import os,sys
import datetime

sys.path.append("..")

import ml

sDataPath="D:\prjs_github\seisFinder\data"
sCurrPath=sys.path[0]


#SC-YN
#data1=ml.mlLoad_ml_1965(sDataPath)
outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)
print(len(data1))
data1c=ml.mlFilter_sfml2_lonlat(data1,90,110,20,35)
print(len(data1c))
ml_outFile_grid_count_20="out\ml_grid_count20-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_20,90,110,2,20,35,2)
ml_outFile_grid_count_10="out\ml_grid_count10-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_10,90,110,1,20,35,1)
ml_outFile_grid_count_05="out\ml_grid_count05-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_05,90,110,0.5,20,35,0.5)

ml_outFile_grid_count_02="out\ml_grid_count02-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_02,90,110,0.2,20,35,0.2)

ml_outFile_grid_count_01="out\ml_grid_count01-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_01,90,110,0.1,20,35,0.1)

  

#t430****
#sDataPath_t430="E:\_qsync.1\_1"
#infile_ml_1965=os.path.join(sDataPath_t430,"ml","ml_1965_2018.sfml2")
#data1=ml.ml_Read_sfml2(infile_ml_1965)

#d30****
#data1=ml.mlLoad_ml_1965(sDataPath)
#print(len(data1))

data1a=ml.mlFilter_sfml2_lonlat(data1,70,140,10,60)
print(len(data1a))

data1b=ml.mlFilter_sfml2_m(data1a,0.9)
#print(len(data1b))

ml_outFile_grid_count_20="out\ml_grid_count20.png"
ml.mlDraw_Grid_count(data1b,ml_outFile_grid_count_20,70,140,2,10,60,2)
ml_outFile_grid_count_10="out\ml_grid_count10.png"
ml.mlDraw_Grid_count(data1b,ml_outFile_grid_count_10,70,140,1,10,60,1)
ml_outFile_grid_count_05="out\ml_grid_count05.png"
ml.mlDraw_Grid_count(data1b,ml_outFile_grid_count_05,70,140,0.5,10,60,0.5)
print(len(data1b))

