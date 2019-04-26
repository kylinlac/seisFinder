import numpy as np
import pandas as pd


'''
----np
mean 平均值
sum 求和
cumsum 累加
cumprod 累乘
std 方差
var 标准差
max 最大值
min 最小值
argmax 最大值索引
argmin 最小值索引
'''


def sfTool_list_to_npArray(data11):
    npa=np.array(data11)
    return npa

def sfTool_list_to_pdSeries(data11):
    ser=pd.Series(data11)
    return ser


def sfStats_mean(data11):    
    bRes=False
    fValue=0.0
    if data11:
        npData=sfTool_list_to_npArray(data11)
        fValue=npData.mean()
        bRes=True
   
    return (bRes,fValue)    
    
def sfStats_std(data11):    
    bRes=False
    fValue=0.0
    if data11:
        npData=sfTool_list_to_npArray(data11)
        fValue=npData.std()
        bRes=True
   
    return (bRes,fValue)    
    
def sfStats_var(data11):    
    bRes=False
    fValue=0.0
    if data11:
        npData=sfTool_list_to_npArray(data11)
        fValue=npData.var()
        bRes=True
   
    return (bRes,fValue)    

def sfStats_min(data11):    
    bRes=False
    fValue=0.0
    if data11:
        npData=sfTool_list_to_npArray(data11)
        fValue=npData.min()
        bRes=True
   
    return (bRes,fValue)    

def sfStats_max(data11):    
    bRes=False
    fValue=0.0
    if data11:
        npData=sfTool_list_to_npArray(data11)
        fValue=npData.max()
        bRes=True
   
    return (bRes,fValue)    

def sfStats_count(data11):    
    bRes=False
    fValue=0.0
    if data11:
        fValue=len(data11)
        bRes=True
   
    return (bRes,fValue)    

def sfStats_median(data11):    
    bRes=False
    fValue=0.0
    if data11:
        pds=sfTool_list_to_pdSeries(data11)
        fValue=pds.median()
        bRes=True
   
    return (bRes,fValue)    

def sfStats_skew(data11):    
    bRes=False
    fValue=0.0
    if data11:
        pds=sfTool_list_to_pdSeries(data11)
        fValue=pds.skew()
        bRes=True
   
    return (bRes,fValue)    

def sfStats_kurt(data11):    
    bRes=False
    fValue=0.0
    if data11:
        pds=sfTool_list_to_pdSeries(data11)
        fValue=pds.kurt()
        bRes=True
   
    return (bRes,fValue) 

