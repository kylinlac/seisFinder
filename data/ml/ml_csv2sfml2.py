# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:39:30 2019

@author: wjb
"""

#import os,sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import cartopy.crs as ccrs
import pandas as pd

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

def ml_Read_check(infile):
    poss=[]
    with open(infile) as f1:
        data1=f1.readlines()
        
        for i,v in enumerate(data1):
            vs=v.split(',')
            print(i,vs)
            lon=float(vs[7])
            lat=float(vs[6])
            print(lon,lat)
    
    return poss


def ml_Draw_file2png(infile):
    #poss=[]
    with open(infile) as f1:
        data1=f1.readlines()
        lons=[float(d.split(",")[7]) for d in data1]
        lats=[float(d.split(",")[6]) for d in data1]
        shsi=[float(d.split(",")[9])*5 for d in data1]
        #poss=zip(lons,lats)    
        
        '''
        for i,v in enumerate(data1):
            vs=v.split(',')
            print(i,vs)
            lon=float(vs[7])
            lat=float(vs[6])
            print(lon,lat)
        '''
    
    #print(list(poss)[:10])
    #return poss
        
        #ok
        #p1=plt.plot(lons,lats,'ro')
        #plt.setp(p1,markersize=1) #plt default value isnot 1
        #plt.setp(p1,markerfacecolor='C0')             
        #plt.savefig("p1.png")

        plt.scatter(lons,lats,shsi)
        plt.savefig("p2.png")


def ml_Read(infile):
    with open(infile) as f1:
        data1=f1.readlines()
        data2=[d.split(",") for d in data1] #include \n
        return data2
    
    nd=[]
    return nd;
    

def testing_ML_Draw_xy_01():
    data1=ml_Read("ml_1965_2018.sfml2")
    if data1 :
        lons=[float(d[7]) for d in data1]
        lats=[float(d[6]) for d in data1]
        shsi=[float(d[9])*5 for d in data1]
        
        #plt.figure()
        #plt.subplot(111, projection="aitoff")
        
        plt.scatter(lons,lats,shsi,c='yellow',alpha=0.5,edgecolors='red')
        #plt.legend()
        plt.grid(True)      
        plt.xlabel('lon')
        plt.ylabel('lat')
        plt.title('China EarthQuake')
        
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)        
        #plt.savefig("testing_ML_Draw_01.png")
        plt.savefig("testing_ML_Draw_01b.png")
  
    
def testing_GIS_Draw_01():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    ax.set_global()

    ax.stock_img()
    ax.coastlines()

    ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.PlateCarree())
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.Geodetic())    
    plt.savefig("testing_GIS_Draw_01.png")
    
    
def testing_GIS_Draw_02():   
    plt.figure(figsize=(6, 3))
    ax = plt.axes(projection=ccrs.Mollweide(central_longitude=105.0))
    ax.coastlines(resolution='110m')   
    ax.gridlines()    
    plt.savefig("testing_GIS_Draw_02.png")
    
    
def testing_ML_Draw_gis_02():
    data1=ml_Read("ml_1965_2018.sfml2")
    if data1 :
        lons=[float(d[7]) for d in data1]
        lats=[float(d[6]) for d in data1]
        shsi=[float(d[9])*5 for d in data1]
        
  
        fig = plt.figure(figsize=(50, 25))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson(central_longitude=105.0))
    
        # make the map global rather than have it zoom in to
        # the extents of any plotted data
        ax.set_global()
    
        ax.stock_img()
        ax.coastlines()
    
        #ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())
        #ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.PlateCarree())
        #ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.Geodetic())   
        ax.scatter(lons,lats,shsi,c='yellow',alpha=0.5,edgecolors='red', transform=ccrs.PlateCarree())
        
        
        plt.savefig("testing_ML_Draw_02.png")
    
    
def testing_ML_Draw_gis_03(xi=60,xx=150,yi=0,yx=70):
    data1=ml_Read("ml_1965_2018.sfml2")
    if data1 :
        lons=[float(d[7]) for d in data1]
        lats=[float(d[6]) for d in data1]
        shsi=[float(d[9])*5 for d in data1]
        
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        ax.set_extent([xi-1, xx+1, yi-1, yx+1], crs=ccrs.PlateCarree())   
        ax.stock_img()     
        ax.scatter(lons,lats,shsi,c='yellow',alpha=0.5,edgecolors='red', transform=ccrs.PlateCarree())              
        plt.savefig("testing_ML_Draw_gis_03.png")
    
 
def testing_ML_Draw_gis_04_chuandian(mx=0,xi=90,xx=115,yi=15,yx=35):
    data1=ml_Read("ml_1965_2018.sfml2")
    if data1 :
        data2=[d for d in data1 if float(d[7])>xi and float(d[7])<xx and float(d[6])>yi and float(d[6])<yx and float(d[9])>mx ]
        print("count: ",len(data1),len(data2))
    
        lons=[float(d[7]) for d in data2]
        lats=[float(d[6]) for d in data2]
        shsi=[float(d[9])*10 for d in data2]
        
        #data2=list(zip(lons,lats,shsi))
        
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        ax.set_extent([xi-1, xx+1, yi-1, yx+1], crs=ccrs.PlateCarree())    
        ax.stock_img()    
        ax.scatter(lons,lats,shsi,c='yellow',alpha=0.5,edgecolors='red', transform=ccrs.PlateCarree())             
        plt.savefig("testing_ML_Draw_gis_04.png")
    
    
def testing_ML_Draw_mt_01(mx=0,xi=90,xx=115,yi=15,yx=35):
    data1=ml_Read("ml_1965_2018.sfml2")
    if data1 :
        data2=[d for d in data1 if float(d[7])>xi and float(d[7])<xx and float(d[6])>yi and float(d[6])<yx and float(d[9])>mx ]
        print("count: ",len(data1),len(data2))
    
        #lons=[float(d[7]) for d in data2]
        #lats=[float(d[6]) for d in data2]
        shsi=[float(d[9]) for d in data2]
              
        fig = plt.figure(figsize=(24, 8))
        xs=range(len(shsi))
        #plt.bar(xs,shsi,width=0.1) ok
        plt.vlines(xs,[0],shsi,color='blue') #[3]=ymin,shsi=ymax
        
        plt.savefig("testing_ML_Draw_mt_01.png")
        
    
def testing_ML_Draw_mt_02(mx=0,xi=90,xx=115,yi=15,yx=35):
    data1=ml_Read("ml_1965_2018.sfml2")
    if data1 :
        data2=[d for d in data1 if float(d[7])>xi and float(d[7])<xx and float(d[6])>yi and float(d[6])<yx and float(d[9])>mx ]
        print("count: ",len(data1),len(data2))
    
        #lons=[float(d[7]) for d in data2]
        #lats=[float(d[6]) for d in data2]
        shsi=[float(d[9]) for d in data2]
        dts=[mdate.datetime.datetime(int(d[0]),int(d[1]),int(d[2]),int(d[3]),int(d[4]),int(float(d[5]))) for d in data2]
        ''' debug
        for i,v in enumerate(data2):
            v5=int(float(v[5]))
            print(v)
            print(i,v5)
        '''
        fig = plt.figure(figsize=(50, 8))
        ax = fig.add_subplot(1, 1, 1)
        #fig.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
        ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))#设置时间标签显示格式
        #plt.bar(xs,shsi,width=0.1) ok
        plt.vlines(dts,[0],shsi,color='blue') #[3]=ymin,shsi=ymax
        #plt.xticks(freq='1year')
        #plt.xticks(pd.date_range(dts[0],dts[-1],freq='Y'))
        '''
        dt1=mdate.datetime.datetime(1960,1,1,0,0,0)
        dt2=mdate.datetime.datetime(2020,1,1,0,0,0)
        plt.xticks(pd.date_range(dt1,dt2,freq='Y'))
        '''
        dt12=[mdate.datetime.datetime(y,1,1,0,0,0) for y in range(1960,2020) ]
        plt.xticks(dt12)
        plt.xticks(rotation=60)
        plt.savefig("testing_ML_Draw_mt_02.png")
        
        
####running...
#883603-->880219-->870996 -> 867673 (--> 868478)
#ml_Convert_csv_to_sfml2("china_ml.csv","ml_1965_2018.sfml2")

#ml_Draw_file2png("ml_1965_2018.sfml2")

#testing_ML_Draw_01()
    
#testing_GIS_Draw_01()   
#testing_GIS_Draw_02()
        
#testing_ML_Draw_02()   
#testing_ML_Draw_03()    

#testing_ML_Draw_04_chuandian(4.9+0.05)
#testing_ML_Draw_gis_04_chuandian(4.9+0.05,60,150,0,70)

#testing_ML_Draw_mt_01(4.9)    
testing_ML_Draw_mt_02(4.9)      