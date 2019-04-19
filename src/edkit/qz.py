

import os
import datetime

import pickle
import zipfile
import codecs
#import fnmatch

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import cartopy.crs as ccrs
#import pandas as pd
import numpy as np


#--------------------------------------------

def qz_Convert_csv_to_sfml2(inFile,outFile):
  pass

  
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
                        
                        
                        
                        
                        

