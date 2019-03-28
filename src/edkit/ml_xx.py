

'''
def mlRead_eqt(eqtFile):
    data2=[]
    with open(eqtFile,'rt') as f1:
        lines=f1.readlines()
        #data1=[d1.split('\n')[0] for d1 in lines]
        data1=[d1.rstrip('\n') for d1 in lines]        
        #data2=ml_utils.ml_EqtToMl2(data1)
        data2=data1
        
    return data2
'''



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


'''
def mlLoad(sPath):
    #sfPath_root="d:\prjs_github"
    #sfPath_load=os.path.join(sfPath_root,"data")
    #sFile=os.path.join(sfPath_load,"ml","ms6.pkl")    
    sFile=os.path.join(sPath,"ml","ml_1965_2018.pkl")        
    data1=ml_Load(sFile)
    return data1
'''


'''
dataMs6=ml.mlLoad_Stock_ms6(sDataPath)
print(dataMs6)
'''


'''
def ml_Draw_file2png(infile):
    #poss=[]
    with open(infile) as f1:
        data1=f1.readlines()
        lons=[float(d.split(",")[7]) for d in data1]
        lats=[float(d.split(",")[6]) for d in data1]
        shsi=[float(d.split(",")[9])*5 for d in data1]
        #poss=zip(lons,lats)    
        
        
        for i,v in enumerate(data1):
            vs=v.split(',')
            print(i,vs)
            lon=float(vs[7])
            lat=float(vs[6])
            print(lon,lat)
          
    #print(list(poss)[:10])
    #return poss
        
        #ok
        #p1=plt.plot(lons,lats,'ro')
        #plt.setp(p1,markersize=1) #plt default value isnot 1
        #plt.setp(p1,markerfacecolor='C0')             
        #plt.savefig("p1.png")

        plt.scatter(lons,lats,shsi)
        plt.savefig("p2.png")
'''        
    
    
'''
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
'''

'''  
def testing_GIS_Draw_02():   
    plt.figure(figsize=(6, 3))
    ax = plt.axes(projection=ccrs.Mollweide(central_longitude=105.0))
    ax.coastlines(resolution='110m')   
    ax.gridlines()    
    plt.savefig("testing_GIS_Draw_02.png")
'''

'''
def testing_ML_Draw_gis_02():
    data1=ml_Read_sfml2("ml_1965_2018.sfml2")
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
'''


def ml_ML_Draw_gis_04_chuandian(mx=0,xi=90,xx=115,yi=15,yx=35):
    data1=ml_Read_sfml2("ml_1965_2018.sfml2")
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

def testing_ML_Draw_xy_01():
    data1=ml_Read_sfml2("ml_1965_2018.sfml2")
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


def testing_ML_Draw_gis_03(xi=60,xx=150,yi=0,yx=70):
    data1=ml_Read_sfml2("ml_1965_2018.sfml2")
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
    data1=ml_Read_sfml2("ml_1965_2018.sfml2")
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
    data1=ml_Read_sfml2("ml_1965_2018.sfml2")
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


def mlDraw_mt__easy(mx=0,xi=90,xx=115,yi=15,yx=35):
    data1=ml_Read_sfml2("ml_1965_2018.sfml2")
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
        
  
    
    
