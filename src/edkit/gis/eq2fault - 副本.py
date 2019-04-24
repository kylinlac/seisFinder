#import os
#import ogr
from osgeo import ogr
import shapely.wkt
import shapely.geometry

def getDistance():
    pass


MAX_DISTANCE=2.0 #200KM

lon0=116.2
lat0=39.6
pt=shapely.geometry.Point(lon0,lat0)

shapefile=ogr.Open("fault_dqd.shp")
#shapefile=ogr.Open("activeFault.shp")
layer0=shapefile.GetLayer(0)

for i in range(layer0.GetFeatureCount()):
    featurei=layer0.GetFeature(i)
    name=featurei.GetField(r"断层编码")
    #name=featurei.GetField(r"名称")
    geometry=featurei.GetGeometryRef()
    
    wkt=geometry.ExportToWkt()
    shape=shapely.wkt.loads(wkt)
    dis1=shape.distance(pt)
    print(i,": ",name,", ",dis1)
    
    