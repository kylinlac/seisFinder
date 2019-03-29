'''
read/load/fetch data

read: file
load: dump
fetch: mysql
get: restful
request: web service
rpc: RPC (?call)

**built in
ml_convert-*

**user api
mlRead


'''


import os
#import sys
import pickle

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import cartopy.crs as ccrs
#import pandas as pd
import numpy as np


#--------------------------------------------


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
        

#--------------------------------------


def ml_Dump_list2file(data1,outFile):
  output = open(outFile, 'wb')
  pickle.dump(data1, output)
  # Pickle the list using the highest protocol available.
  #pickle2.dump(data1, output, -1)
  output.close()

def ml_Dump_file2file(inFile,outFile):
  f1=open(inFile,"r")
  data1=f1.readlines()
  f1.close() 
  ml_Dump_list2file(data1,outFile)


def ml_Load(inFile):
  pkl_file = open(inFile, 'rb')
  data1 = pickle.load(pkl_file)
  #pprint.pprint(data1)
  #data2 = pickle.load(pkl_file)
  #pprint.pprint(data2)
  pkl_file.close()
  return data1


#--------------------------------------------------------
  
def ml_Read_sfml2(infile):
    with open(infile) as f1:
        data1=f1.readlines()
        data2=[d.split(",") for d in data1] #include \n
        return data2    
    nd=[]
    return nd;


def ml_Read_sfml2_checkOnly(infile):
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

#------------------------------------------

def mlFilter_sfml2_m(data1,mi=0,mx=10):   
    data2=[d for d in data1 if float(d[9])>mi and float(d[9])<mx]
    return data2
   
def mlFilter_sfml2_lonlat(data1,xi=59,xx=171,yi=0,yx=70):
    data2=[d for d in data1 if float(d[7])>xi and float(d[7])<xx and float(d[6])>yi and float(d[6])<yx]
    return data2
    
#------------------------------------------

'''
def mlFetch_xx(sUrl):
    data1=[]
    return data1
'''

def mlLoad_ml_1965(sPath):
    sFile=os.path.join(sPath,"ml","ml_1965_2018.pkl")        
    data1=ml_Load(sFile)
    return data1


#------------------------------------------------

def mlDraw_hyperCenter_withGIS__easy(data1,outFile,scaleSym,bGlobal,xi=60,xx=150,yi=0,yx=70):
    if data1 :   
        lons=[float(d[7]) for d in data1]
        lats=[float(d[6]) for d in data1]
        shsi=[float(d[9])*scaleSym for d in data1]
               
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        
        if bGlobal == True:
            ax.set_global()
            print("set global")
        else:
            ax.set_extent([xi-1, xx+1, yi-1, yx+1], crs=ccrs.PlateCarree())    
            
        ax.stock_img()    
        ax.scatter(lons,lats,shsi,c='yellow',alpha=0.5,edgecolors='red', transform=ccrs.PlateCarree())             
        #plt.savefig("testing_ML_Draw_gis_04.png")
        plt.savefig(outFile)
    else:
        print("not data ...")
        

def mlDraw_hyperCenter__easy(data1,outFile,scaleSym=1):
    if data1 :
        lons=[float(d[7]) for d in data1]
        lats=[float(d[6]) for d in data1]
        shsi=[float(d[9])*scaleSym for d in data1]
               
        plt.scatter(lons,lats,shsi,c='yellow',alpha=0.5,edgecolors='red')
        plt.grid(True)      
        plt.xlabel('lon')
        plt.ylabel('lat')
        #plt.title('China EarthQuake')
        
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)        
        #plt.savefig("testing_ML_Draw_01.png")
        plt.savefig(outFile)
    else:
        print("not data ...")
               
    
def mlDraw_mt__easy(data1,outFile):
    if data1 :   
        #lons=[float(d[7]) for d in data2]
        #lats=[float(d[6]) for d in data2]
        shsi=[float(d[9]) for d in data1]
        dts=[mdate.datetime.datetime(int(d[0]),int(d[1]),int(d[2]),int(d[3]),int(d[4]),int(float(d[5]))) for d in data1]

        fig = plt.figure(figsize=(20, 9))
        ax = fig.add_subplot(1, 1, 1)
        #fig.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
        ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))#设置时间标签显示格式
        #plt.bar(xs,shsi,width=0.1) ok
        plt.vlines(dts,[0],shsi,color='blue') #[3]=ymin,shsi=ymax
        
        #xxx
        #dt1=mdate.datetime.datetime(1960,1,1,0,0,0)
        #dt2=mdate.datetime.datetime(2020,1,1,0,0,0)
        #plt.xticks(pd.date_range(dt1,dt2,freq='Y'))

        dt12=[mdate.datetime.datetime(y,1,1,0,0,0) for y in range(1965,2020) ]
        plt.xticks(dt12)
        plt.xticks(rotation=90)
        #plt.savefig("testing_ML_Draw_mt_02.png")
        plt.savefig(outFile)
    else:
        print("no data ...")        
        

#def mlDraw_spatial        
def mlDraw_Grid_count(data1,outFile,xi=10,xx=170,stepLon=1,yi=0,yx=70,stepLat=1):
    #x,y=np.meshgrid(np.arange(60,140,0.5),np.rrange(0,70,0.5))
    #z=np.random.randn(x.shape[0],x.shape[1])
    #plt.contour(x,y,z)
    #plt.show()
    #10-170,0-70
    xm,ym=np.meshgrid(np.arange(xi,xx+1,stepLon),np.arange(yi,yx+1,stepLat))
    #ym,xm=np.meshgrid(np.arange(xi,xx,stepLon),np.arange(yi,yx,stepLat)) #??70,160 -> 160,70   xx
    #zm=np.zeros(xm.shape,dtype=float) xx log10(0.0)=inf
    zm=np.ones(xm.shape,dtype=float) 
    
    for i,d1 in enumerate(data1):
        lon=float(d1[7])
        lat=float(d1[6])
        #print("lon,lat: ",lon,lat)
        lonIdx=int((lon-(xi-stepLon/2))/stepLon)
        latIdx=int((lat-(yi-stepLat/2))/stepLat)
        #print("lonIdx,latIdx: ",lonIdx,latIdx)
        #zm[latIdx][lonIdx]+=0.001 xx
        zm[latIdx][lonIdx]+=1
        
    #print(zm)
    #print(zm.shape)                
    #b=plt.contourf(xm,ym,zm,10)
    zm2=np.log10(zm)    
    #plt.contourf(xm,ym,zm2,10,cmap=plt.cm.Spectral)
    #plt.contour(xm,ym,zm2,10,colors='black') ok
    plt.contourf(xm,ym,zm2,10)
    #plt.clabel(b, inline=True, fontsize=10)
    #plt.colorbar() ok
    
    fig = plt.gcf()
    fig.set_size_inches(20, 12)  
    plt.savefig(outFile)
    
    #mv=max(zm) python usage
    mv=np.max(zm2)
    print("max value: ",mv)
    #mvpos=np.where(mv)    
    #print("max value: ",mv,mvpos)


    '''    
    f1=open("t1","w");
    for lat1 in range(zm.shape[0]):
        for lon1 in range(zm.shape[1]):
            print("(lon,lat): ",lat1,lon1,zm[lat1][lon1])            
    f1.close()
    '''    
    
    
def mlDraw_Heatmap_count_XX(data1,outFile,xi=10,xx=170,stepLon=1,yi=0,yx=70,stepLat=1):
    xm,ym=np.meshgrid(np.arange(xi,xx+1,stepLon),np.arange(yi,yx+1,stepLat))
    zm=np.ones(xm.shape,dtype=float) 
    
    for i,d1 in enumerate(data1):
        lon=float(d1[7])
        lat=float(d1[6])
        lonIdx=int((lon-(xi-stepLon/2))/stepLon)
        latIdx=int((lat-(yi-stepLat/2))/stepLat)
        zm[latIdx][lonIdx]+=1

    zm2=np.log10(zm)    
    '''
    #flip up/down
    row=zm2.shape[0]    
    for i in range(row // 2):
        zm2[i], zm2[row-1-i] = zm2[row-1-i], zm2[i]  
    '''    
    plt.imshow(zm2)
        
    fig = plt.gcf()
    fig.set_size_inches(20, 12)  
    plt.savefig(outFile)
    

       
    