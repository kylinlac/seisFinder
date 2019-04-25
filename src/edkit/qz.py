

import os
import datetime

#import pickle
import zipfile
import codecs
#import fnmatch

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import cartopy.crs as ccrs
from matplotlib.ticker import AutoMinorLocator

#import pandas as pd
import numpy as np


#--------------------------------------------
 
def qz_Convert_Merger_90(rootDir,outDir):
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        #print(d1)               
        d0=os.path.join(rootDir,d1)        
        sSfqz1=os.path.join(outDir,d1+".sfqz1")
        ##sSfqz2=os.path.join(outDir,d1+".sfqz2")
        #print(d0)
        print(sSfqz1)
        ##print(sSfqz2)
        
        fs=os.listdir(d0)
        
        with open(sSfqz1,"wt") as fpo:
            fs.sort()
            for f1 in fs:
                f0=os.path.join(d0,f1)
                print(f0)

                dts=f1.split(".")[0].split("-")[2].split("_")
                #print(dts)
                #continue
                dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),0,0,0)
                #sdt0=dt0.strftime("YYYY-MM-DD HH:mm:ss")
                sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
                
                with open(f0,"rt") as fp:
                    vs=fp.read()
                    #print(vs)
                    if vs.count("NULL")>0 : #find>0 xx
                        continue
                    if vs.count("ALLNULL")>0 :
                        continue
               
                    sOut=sdt0+" "+vs+"\n"
                    fpo.write(sOut)
                
                #break = 1 day
                                  
        #break #= 1 point


def qz_Convert_Merger_60(rootDir,outDir):
    hitCount=24
    
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        d0=os.path.join(rootDir,d1)        
        sSfqz1=os.path.join(outDir,d1+".sfqz1")
        print(sSfqz1)
        
        fs=os.listdir(d0)
        
        with open(sSfqz1,"wt") as fpo:
            fs.sort()
            for f1 in fs:
                f0=os.path.join(d0,f1)
                print(f0)

                dts=f1.split(".")[0].split("-")[2].split("_")
                
                with open(f0,"rt") as fp:
                    vs=fp.read()
                    vss=vs.split(" ")
                    #print(len(vss))
                    #break
                    if len(vss) != hitCount:
                        continue
                    
                    for i,vss1 in enumerate(vss):
                        if vss1.count("NULL")>0 : #find>0 xx
                            continue
                        if vss1.count("ALLNULL")>0 :
                            continue

                        dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),i,0,0)
                        sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
                   
                        sOut=sdt0+" "+vss1+"\n"
                        fpo.write(sOut)
                        



def qz_Convert_Merger_10(rootDir,outDir):
    hitCount=60*24
    
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        d0=os.path.join(rootDir,d1)        
        sSfqz1=os.path.join(outDir,d1+".sfqz1")
        print(sSfqz1)
        
        fs=os.listdir(d0)
        
        with open(sSfqz1,"wt") as fpo:
            fs.sort()
            for f1 in fs:
                f0=os.path.join(d0,f1)
                print(f0)

                dts=f1.split(".")[0].split("-")[2].split("_")
                
                #with open(f0,"rt") as fp:
                with codecs.open(f0,"r","utf-8") as fp:
                    vs=fp.read()
                    vss=vs.split(" ")
                    #print(len(vss))
                    #break
                    if len(vss) != hitCount:
                        continue
                    
                    for i,vss1 in enumerate(vss):
                        if vss1.count("NULL")>0 : #find>0 xx
                            continue
                        if vss1.count("ALLNULL")>0 :
                            continue
                        if vss1.count("非数字")>0 :
                            continue                        

                        dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),0,0,0)+datetime.timedelta(minutes=i)
                        sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
                   
                        sOut=sdt0+" "+vss1+"\n"
                        fpo.write(sOut)




def qz_Convert_Merger_02(rootDir,outDir):
    hitCount=60*60*24
    
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        d0=os.path.join(rootDir,d1)        
        sSfqz1=os.path.join(outDir,d1+".sfqz1")
        print(sSfqz1)
        
        fs=os.listdir(d0)
        
        with open(sSfqz1,"wt") as fpo:
            fs.sort()
            for f1 in fs:
                f0=os.path.join(d0,f1)
                print(f0)

                dts=f1.split(".")[0].split("-")[2].split("_")
                
                #with open(f0,"rt") as fp:
                with codecs.open(f0,"r","utf-8") as fp:
                    vs=fp.read()
                    vss=vs.split(" ")
                    #print(len(vss))
                    #break
                    if len(vss) != hitCount:
                        continue
                    
                    for i,vss1 in enumerate(vss):
                        if vss1.count("NULL")>0 : #find>0 xx
                            continue
                        if vss1.count("ALLNULL")>0 :
                            continue
                        if vss1.count("非数字")>0 :
                            continue                        

                        dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),0,0,0)+datetime.timedelta(seconds=i)
                        sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
                   
                        sOut=sdt0+" "+vss1+"\n"
                        fpo.write(sOut)



   
def qz_Convert_Add_90(rootDir,outDir):
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        #print(d1)               
        d0=os.path.join(rootDir,d1)        
        
        fs=os.listdir(d0)        
        fs.sort()
        for f1 in fs:
            f0=os.path.join(d0,f1)
            print(f0)
            sSfqz1=os.path.join(outDir,d1,f1+".sfqz1") #has .txt
            print(sSfqz1) 
            subDir=os.path.join(outDir,d1)
            if os.path.exists(subDir)==False:
                os.makedirs(subDir)
                        
            dts=f1.split(".")[0].split("-")[2].split("_")
            #print(dts)
            #continue
            dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),0,0,0)
            #sdt0=dt0.strftime("YYYY-MM-DD HH:mm:ss")
            sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
            
            with open(sSfqz1,"wt") as fpo:
                with open(f0,"rt") as fp:
                    vs=fp.read()
                    #print(vs)
                    if vs.count("NULL")>0 : #find>0 xx
                        continue
                    if vs.count("ALLNULL")>0 :
                        continue
               
                    sOut=sdt0+" "+vs+"\n"
                    fpo.write(sOut)
                
                #break = 1 day
                                  
        #break #= 1 point


def qz_Convert_Add_60(rootDir,outDir):
    hitCount=24
    
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        #print(d1)               
        d0=os.path.join(rootDir,d1)        
        
        fs=os.listdir(d0)        
        fs.sort()
        for f1 in fs:
            f0=os.path.join(d0,f1)
            print(f0)
            sSfqz1=os.path.join(outDir,d1,f1+".sfqz1") #has .txt
            print(sSfqz1) 
            subDir=os.path.join(outDir,d1)
            if os.path.exists(subDir)==False:
                os.makedirs(subDir)
                        
            dts=f1.split(".")[0].split("-")[2].split("_")
                                          
            with open(sSfqz1,"wt") as fpo:                
                with open(f0,"rt") as fp:
                    vs=fp.read()
                    vss=vs.split(" ")
                    if len(vss) != hitCount:
                        continue
                    
                    for i,vss1 in enumerate(vss):
                        if vss1.count("NULL")>0 : #find>0 xx
                            continue
                        if vss1.count("ALLNULL")>0 :
                            continue
    
                        dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),i,0,0)
                        sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
                   
                        sOut=sdt0+" "+vss1+"\n"
                        fpo.write(sOut)
                                                 
        #break #= 1 point


def qz_Convert_Add_01(rootDir,outDir):
    hitCount=60*24
   
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        #print(d1)               
        d0=os.path.join(rootDir,d1)        
        
        fs=os.listdir(d0)        
        fs.sort()
        for f1 in fs:
            f0=os.path.join(d0,f1)
            print(f0)
            sSfqz1=os.path.join(outDir,d1,f1+".sfqz1") #has .txt
            print(sSfqz1) 
            subDir=os.path.join(outDir,d1)
            if os.path.exists(subDir)==False:
                os.makedirs(subDir)
                        
            dts=f1.split(".")[0].split("-")[2].split("_")
                                          
            with open(sSfqz1,"wt") as fpo:                
                #with open(f0,"rt") as fp:
                with codecs.open(f0,"r","utf-8") as fp:                    
                    vs=fp.read()
                    vss=vs.split(" ")
                    if len(vss) != hitCount:
                        continue
                    
                    for i,vss1 in enumerate(vss):
                        if vss1.count("NULL")>0 : #find>0 xx
                            continue
                        if vss1.count("ALLNULL")>0 :
                            continue
                        if vss1.count("非数字")>0 :
                            continue                        
                        
    
                        dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),0,0,0)+datetime.timedelta(minutes=i)
                        sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
                   
                        sOut=sdt0+" "+vss1+"\n"
                        fpo.write(sOut)



def qz_Convert_Add_02(rootDir,outDir):
    hitCount=60*60*24
   
    ds=os.listdir(rootDir) #point=dir
    for d1 in ds:
        #print(d1)               
        d0=os.path.join(rootDir,d1)        
        
        fs=os.listdir(d0)        
        fs.sort()
        for f1 in fs:
            f0=os.path.join(d0,f1)
            print(f0)
            sSfqz1=os.path.join(outDir,d1,f1+".sfqz1") #has .txt
            print(sSfqz1) 
            subDir=os.path.join(outDir,d1)
            if os.path.exists(subDir)==False:
                os.makedirs(subDir)
                        
            dts=f1.split(".")[0].split("-")[2].split("_")
                                          
            with open(sSfqz1,"wt") as fpo:                
                #with open(f0,"rt") as fp:
                with codecs.open(f0,"r","utf-8") as fp:                    
                    vs=fp.read()
                    vss=vs.split(" ")
                    if len(vss) != hitCount:
                        continue
                    
                    for i,vss1 in enumerate(vss):
                        if vss1.count("NULL")>0 : #find>0 xx
                            continue
                        if vss1.count("ALLNULL")>0 :
                            continue
                        if vss1.count("非数字")>0 :
                            continue                        
                        
    
                        dt0=datetime.datetime(int(dts[0]),int(dts[1]),int(dts[2]),0,0,0)+datetime.timedelta(seconds=i)
                        sdt0=dt0.strftime("%Y-%m-%d %H:%M:%S")
                   
                        sOut=sdt0+" "+vss1+"\n"
                        fpo.write(sOut)



#--------------------------------------------
# date_string = "2018-11-30 13:53:59"
# datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

'''
def qz_Read_sfqz1_xxxx(infile):
    data1=[]    
    with open(infile) as f1:
        data1=f1.read().splitlines()
    return data1
'''

'''                       
def qz_Read_sfml1_inZip_0(zipFile,sfqz1File):
    zf=zipFile
    zfd="qz"
    #dfn="DYU_60_212_51001_5_2121.sfqz1"
    dfn=sfqz1File

    azip=zipfile.ZipFile(zf)
    ml2=azip.read(zfd+"/"+dfn).decode('utf-8')
    
    data1=ml2.splitlines(False) #True=keep n/rn,False=delete n/rn
    data2=[d.split(" ") for d in data1] #include \n
    return data2    
'''


def qz_Read_sfqz1(infile):
    data2=[[],[]]    
    #no_data=("999.000","9999.000","99999.0000","999999.0000")
    no_data=("999.000","9999.000","99999.0000","999999.0000","9999","99999","999999")
    with open(infile) as f1:
        data1=f1.read().splitlines()
        
        dt2=[]
        val2=[]
        for d in data1:
            ds=d.split(" ")
            if ds[2] in no_data:
                continue
            
            dt2.append(datetime.datetime.strptime(ds[0]+" "+ds[1], "%Y-%m-%d %H:%M:%S"))
            val2.append(float(ds[2]))
        data2=[dt2,val2]
        
    return data2
                   
     
def qz_Read_sfqz1_inZip(zipFile,sfqz1File):
    zf=zipFile
    zfd="qz"
    #dfn="DYU_60_212_51001_5_2121.sfqz1"
    dfn=sfqz1File

    azip=zipfile.ZipFile(zf)
    ml2=azip.read(zfd+"/"+dfn).decode('utf-8')
    
    data1=ml2.splitlines(False) #True=keep n/rn,False=delete n/rn
    #data2=[d.split(" ") for d in data1] #include \n
    
    #ok
    #data2=[ [datetime.datetime.strptime(d.split(" ")[0]+" "+d.split(" ")[1], "%Y-%m-%d %H:%M:%S"),d.split(" ")[2]] for d in data1] 
    dt2=[]
    val2=[]
    for d in data1:
        ds=d.split(" ")
        dt2.append(datetime.datetime.strptime(ds[0]+" "+ds[1], "%Y-%m-%d %H:%M:%S"))
        val2.append(float(ds[2]))
    
    # 2 col
    data2=[dt2,val2]
    return data2    
                        
 
#--------------------------------------------

   
def qzDraw__easy(data1,outFile):
    #full year
    if data1 :   
        fig = plt.figure(figsize=(15, 5))
        ax = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))#设置时间标签显示格式
        #plt.vlines(data1[0],[0],data1[1],color='blue') #[3]=ymin,shsi=ymax
        plt.plot(data1[0],data1[1])#,color='r')
         
        year1=int(data1[0][0].year)
        year2=int(data1[0][-1].year)+1
        
        if (year2-year1)>=10 :        
            dt12=[mdate.datetime.datetime(y,1,1,0,0,0) for y in range(year1,year2) ]
            plt.xticks(dt12)
            plt.xticks(rotation=-90)
            plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.20)

        '''
        if 3<(year2-year1)<10 :
            dt12=[]
            #dt13=[]
            for y in range(year1,year2):
                dt12.append(mdate.datetime.datetime(y,1,1,0,0,0))
                #dt13.append(mdate.datetime.datetime(y,7,1,0,0,0))
                dt12.append(mdate.datetime.datetime(y,7,1,0,0,0))
            plt.xticks(dt12)
            plt.xticks(rotation=0)
            #plt.xticks(dt13)
            #ax.xaxis.grid(True,which='major')
            #ax.xaxis.grid(True,which='minor')
        '''
        if 3<(year2-year1)<10 :
            minorLocator=AutoMinorLocator()
            ax.xaxis.set_minor_locator(minorLocator)
            
            plt.tick_params(which='both',width=2)
            plt.tick_params(which='major',length=7)
            plt.tick_params(which='minor',length=4,color='r')
            plt.subplots_adjust(left=0.05, right=0.97, top=0.95, bottom=0.10)
            

        if (year2-year1)<=3 :
            dt12=[]
            for y in range(year1,year2):
                dt12.append(mdate.datetime.datetime(y,1,1,0,0,0))
                dt12.append(mdate.datetime.datetime(y,4,1,0,0,0))
                dt12.append(mdate.datetime.datetime(y,7,1,0,0,0))
                dt12.append(mdate.datetime.datetime(y,10,1,0,0,0))

            plt.xticks(dt12)
            plt.xticks(rotation=0)
            plt.subplots_adjust(left=0.03, right=0.97, top=0.95, bottom=0.08)            
            
        #plt.savefig("testing_ML_Draw_mt_02.png")
        plt.savefig(outFile)
    else:
        print("no data ...")        
                        
                        
                        

