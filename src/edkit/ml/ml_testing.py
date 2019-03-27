'''
ml testing

'''

import os,sys

import ml

sDataPath="D:\prjs_github\seisFinder\data"

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
dataMs6=ml.mlLoad_Stock_ms6(sDataPath)
print(dataMs6)
'''


#ml_Convert_csv_to_sfml2("0001.EQ09_ChinaML2.CSV","ml01_1965_2018.sfml2")
#linesep=\r\n

#error：gbk codec----> gbk -> utf8
#ml_Convert_csv_to_sfml2("china_ml_t01.csv","ml01_1965_2018.sfml2")

        
####running...
#883603-->880219-->870996 -> 867673 (--> 868478)
#ml_Convert_csv_to_sfml2("china_ml.csv","ml_1965_2018.sfml2")


        
####running...

#ml_Draw_file2png("ml_1965_2018.sfml2")

#testing_ML_Draw_01()
    
#testing_GIS_Draw_01()   
#testing_GIS_Draw_02()
        
#testing_ML_Draw_02()   
#testing_ML_Draw_03()    

#testing_ML_Draw_04_chuandian(4.9+0.05)
#testing_ML_Draw_gis_04_chuandian(4.9+0.05,60,150,0,70)

#testing_ML_Draw_mt_01(4.9)    
#testing_ML_Draw_mt_02(4.9)     





