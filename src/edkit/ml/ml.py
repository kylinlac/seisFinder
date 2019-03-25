'''
read/load/fetch data

read: file
load: dump
fetch: mysql
get: restful
request: web service
rpc: RPC (?call)

'''

import os
import sys
import ml_utils


def mlRead_eqt(eqtFile):
    data2=[]
    with open(eqtFile,'rt') as f1:
        lines=f1.readlines()
        #data1=[d1.split('\n')[0] for d1 in lines]
        data1=[d1.rstrip('\n') for d1 in lines]        
        #data2=ml_utils.ml_EqtToMl2(data1)
        data2=data1
        
    return data2


def mlLoad(pklFile):
    data1=ml_utils.ml_Load(inFile)
    #sys.path.append("")
    return data1


def mlFetch(sUrl):
    data1=[]

    return data1


def mlLoad_Stock_ms6():
    sfPath_root="d:\prjs_github"
    sfPath_load=os.path.join(sfPath_root,"data")
    sFile=os.path.join(sfPath_load,"ml","ms6.pkl")
    data1=ml_utils.ml_Load(sFile)
    return data1






