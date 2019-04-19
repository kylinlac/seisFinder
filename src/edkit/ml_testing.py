'''
ml testing

'''

import os,sys

import ml

sDataPath="D:\prjs_github\seisFinder\data"
sCurrPath=sys.path[0]


'''
#ok
infile_ml_1965=os.path.join(sDataPath,"ml","ml_1965_2018.sfml2")
outfile_ml_1965=os.path.join(sDataPath,"ml","ml_1965_2018.pkl")
data1=ml.ml_Read_sfml2(infile_ml_1965)
ml.ml_Dump_list2file(data1,outfile_ml_1965)
'''


'''
#ok
outfile_ml_1965=os.path.join(sDataPath,"ml","ml_1965_2018.pkl")
data1=ml.ml_Load(outfile_ml_1965)
print(data1[:10])
'''


'''
#ok
data1=ml.mlLoad_ml_1965(sDataPath)
print(data1[:2])
'''


'''
#ok
data1=ml.mlLoad_ml_1965(sDataPath)
print(len(data1))
print(data1[:2])

data1a=ml.mlFilter_sfml2_m(data1,mi=4.9)
print(len(data1a))
print(data1a[:2])

data1b=ml.mlFilter_sfml2_m(data1a,mi=5.9)
print(len(data1b))
print(data1b[:2])
'''


'''
#ok
data1=ml.mlLoad_ml_1965(sDataPath)
print(len(data1))
print(data1[:2])

data1a=ml.mlFilter_sfml2_lonlat(data1,90,115,15,35)
print(len(data1a))
print(data1a[:2])
'''

'''
#ok
data1=ml.mlLoad_ml_1965(sDataPath)
print(len(data1))
print(data1[:2])
hc_outFile_1="testing\ml_hc01.png"
#ml.mlDraw_hyperCenter__easy(data1,hc_outFile_1,3)

data1b=ml.mlFilter_sfml2_m(data1,4.9)
print(len(data1b))
#print(data1b[:2])
hc_outFile_2="testing\ml_hc02.png"
ml.mlDraw_hyperCenter_withGIS__easy(data1b,hc_outFile_2,1,True)

data1a=ml.mlFilter_sfml2_lonlat(data1b,90,115,15,35)
print(len(data1a))
#print(data1a[:2])
hc_outFile_3="testing\ml_hc03.png"
ml.mlDraw_hyperCenter_withGIS__easy(data1a,hc_outFile_3,8,False,85,120,10,40)
'''

'''
#ok
data1=ml.mlLoad_ml_1965(sDataPath)
print(len(data1))

data1b=ml.mlFilter_sfml2_m(data1,4.9)
print(len(data1b))
print(data1b[:2])
ml_outFile_mt_1="testing\ml_mt01.png"
ml.mlDraw_mt__easy(data1b,ml_outFile_mt_1)
'''

'''
#t430****
#sDataPath_t430="E:\_qsync.1\_1"
#infile_ml_1965=os.path.join(sDataPath_t430,"ml","ml_1965_2018.sfml2")
#data1=ml.ml_Read_sfml2(infile_ml_1965)

#d30****
data1=ml.mlLoad_ml_1965(sDataPath)

print(len(data1))
data1a=ml.mlFilter_sfml2_lonlat(data1,70,140,10,60)
print(len(data1a))

data1b=ml.mlFilter_sfml2_m(data1a,0.9)
#print(len(data1b))

ml_outFile_grid_count_20="testing\ml_grid_count20.png"
ml.mlDraw_Grid_count(data1b,ml_outFile_grid_count_20,70,140,2,10,60,2)
ml_outFile_grid_count_10="testing\ml_grid_count10.png"
ml.mlDraw_Grid_count(data1b,ml_outFile_grid_count_10,70,140,1,10,60,1)
ml_outFile_grid_count_05="testing\ml_grid_count05.png"
ml.mlDraw_Grid_count(data1b,ml_outFile_grid_count_05,70,140,0.5,10,60,0.5)
print(len(data1b))
'''

'''
#SC-YN
data1=ml.mlLoad_ml_1965(sDataPath)
print(len(data1))
data1c=ml.mlFilter_sfml2_lonlat(data1,90,110,20,35)
print(len(data1c))
ml_outFile_grid_count_20="testing\ml_grid_count20-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_20,90,110,2,20,35,2)
ml_outFile_grid_count_10="testing\ml_grid_count10-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_10,90,110,1,20,35,1)
ml_outFile_grid_count_05="testing\ml_grid_count05-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_05,90,110,0.5,20,35,0.5)

ml_outFile_grid_count_02="testing\ml_grid_count02-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_02,90,110,0.2,20,35,0.2)

ml_outFile_grid_count_01="testing\ml_grid_count01-scyn.png"
ml.mlDraw_Grid_count(data1c,ml_outFile_grid_count_01,90,110,0.1,20,35,0.1)
'''
   
''' 
#XX
data1=ml.mlLoad_ml_1965(sDataPath)
print(len(data1))
data1c=ml.mlFilter_sfml2_lonlat(data1,90,110,20,35)
print(len(data1c))
ml_heatmap_count_10="testing\ml_heatmap_count10-scyn.png"
ml.mlDraw_Heatmap_count(data1c,ml_heatmap_count_10,90,110,1,20,35,1)
ml_heatmap_count_05="testing\ml_heatmap_count05-scyn.png"
ml.mlDraw_Heatmap_count(data1c,ml_heatmap_count_05,90,110,0.5,20,35,0.5)
'''


     
####running...
#883603-->880219-->870996 -> 867673 (--> 868478)
#ml_Convert_csv_to_sfml2("china_ml.csv","ml_1965_2018.sfml2")

''' ok
outfile_ml_1965=os.path.join(sDataPath,"ml_pkl.zip")
data1=ml.ml_Load_inZip(outfile_ml_1965)
print(data1[:10])    
'''

''' ok
outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)
print(data1[:10])    
'''


outfile_ml_1965=os.path.join(sDataPath,"ml_sfml2.zip")
data1=ml.ml_Read_sfml2_inZip(outfile_ml_1965)
print(len(data1))

data1b=ml.mlFilter_sfml2_m(data1,4.9)
print(len(data1b))
print(data1b[:2])
ml_outFile_mt_1="testing\ml_mt01.png"
ml.mlDraw_mt__easy(data1b,ml_outFile_mt_1)



