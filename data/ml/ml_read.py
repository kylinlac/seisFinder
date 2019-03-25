# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:39:30 2019

@author: wjb
"""

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


ml_Read()