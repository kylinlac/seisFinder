# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:39:30 2019

@author: wjb
"""

#import os,sys


'''
def ml_Convert_csv_to_sfml2__easy(inFile,outFile):
    yjob=False
    with open(inFile,mode='r', encoding='UTF-8') as f1:
        data1=f1.readlines()
        #nlc=os.linesep
        #ok
        #data2=[d.rstrip(nlc) for d in data1]
        #ok
        #data2=[','.join(d.rstrip(nlc).replace("-",",").replace(":",",").split(",")[:10]) for d in data1]
        data2=[','.join(d.replace("-",",").replace(":",",").split(",")[:10])+"\n" for d in data1]
        
        #for d1 in data2:
        #    print(d1)
            
            #data1=yes,data2=not
            #if d1[-1]=="\n":
            #    print("yes")

        with open(outFile,"w") as f2:
            f2.writelines(data2)
            ##f2.close()
        
        yjob=True
        print("ok")
    
    if yjob == False:
        print("error to break")
'''
def ml_Convert_csv_to_sfml2(inFile,outFile):
    yjob=False
    data0=[]
    idx=0
    idxEdit=0
    with open(inFile,mode='r', encoding='UTF-8') as f1:
        data1=f1.readlines()
        #data2=[d.replace("-",",").replace(":",",").split(",")[:10] for d in data1]
 
        for i,d1 in enumerate(data1):
            #1965-01-02,08:24:00.00, 26.800, 100.900,999, 2.5,
            #0          1            2       3       4    5
            
            d1s=d1.split(',')
            if len(d1s)<6 :
                idx+=1
                continue
            
            if d1s[5].strip()=='':
                print("m-empty",d1s)
                idx+=1
                continue
            
            #skip -0.0
            m=float(d1s[5])
            if m< 0.1:
                idx+=1
                print("m<0",d1s)
                continue
                        
            lon=float(d1s[3])
            lat=float(d1s[2])
            #print(d1,d1s)
            #print(lon,lat)
            
            if lon<10: #10
                idx+=1
                print("lon<60",d1s)
                continue
            if lon>170: #140
                idx+=1
                print("lon>140",d1s)
                continue
            if lat<0: 
                idx+=1
                print("lat<0",d1s)
                continue
            if lat >70:
                idx+=1
                print("lat>70",d1s)
                continue

            d1a=d1.replace("-",",").replace(":",",").split(",")[:10]
            d2=",".join(d1a)+"\n"   
            
            if d1s[4].strip() in ('','999'):
                print("*depth-999,empty",d1s)
                idxEdit+=1                
                d1a[8]='  0'
                d2=",".join(d1a)+"\n"

            #hour
            if int(float(d1a[3])) >23:
                print("*seconds>=60",d1s)
                idxEdit+=1
                d1a[3]='  23'
                d2=",".join(d1a)+"\n"
            #min
            if int(float(d1a[4])) >59:
                print("*seconds>=60",d1s)
                idxEdit+=1
                d1a[4]=' 59'
                d2=",".join(d1a)+"\n"
            #sec
            if int(float(d1a[5])) >59:
                print("*seconds>=60",d1s)
                idxEdit+=1
                d1a[5]=' 59'
                d2=",".join(d1a)+"\n"
            
            data0.append(d2)
            
        
        yjob=True
        print("ok: *edit,delete ",idxEdit,idx)

    with open(outFile,"w") as f2:
        f2.writelines(data0)
        ##f2.close()
    
    if yjob == False:
        print("error to break")
        

#ml_Convert_csv_to_sfml2("0001.EQ09_ChinaML2.CSV","ml01_1965_2018.sfml2")
#linesep=\r\n

#error：gbk codec----> gbk -> utf8
#ml_Convert_csv_to_sfml2("china_ml_t01.csv","ml01_1965_2018.sfml2")

        
####running...
#883603-->880219-->870996 -> 867673 (--> 868478)
ml_Convert_csv_to_sfml2("china_ml.csv","ml_1965_2018.sfml2")

