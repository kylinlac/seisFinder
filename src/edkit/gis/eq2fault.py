# -*- coding: utf-8 -*-
 
#import os
#import ogr
from osgeo import ogr
from osgeo import gdal
import shapely.wkt
import shapely.geometry

def getDistance():
    pass


#字段：断层编码，断层标识，断层序号，断层名称
    
MAX_DISTANCE=2.0 #200KM

lon0=116.2
lat0=39.6
pt=shapely.geometry.Point(lon0,lat0)

gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8","YES")
gdal.SetConfigOption("SHAPE_ENCODING","GBK")

shapefile=ogr.Open("fault_dqd.shp")
#shapefile=ogr.Open("activeFault.shp")
layer0=shapefile.GetLayer(0)

dis={}
for i in range(layer0.GetFeatureCount()):
    featurei=layer0.GetFeature(i)
    keys=featurei.GetField(1)  #ok,index or field name
    #properties = featurei. get("properties")
    #
    #print("key: ",keys)
    
    #name=featurei.GetField("断层编码")
    #name=featurei.GetField(r"名称")
    name=keys
    geometry=featurei.GetGeometryRef()
    
    wkt=geometry.ExportToWkt()
    shape=shapely.wkt.loads(wkt)
    dis1=shape.distance(pt)
    print(i,": ",name,", ",dis1)
    dis[name]=dis1
    
#print(dis)
#print(dis["F87"])

listV= sorted(dis.values())
goalDis=listV[0]
print(goalDis)

goalFault="-1"
for key1, val1 in dis.items():
    if val1 == goalDis:
        goalFault=key1
print(goalFault)
    