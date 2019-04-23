'''
ml testing

'''

import os,sys
import datetime

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





