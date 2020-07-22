#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:34:32 2020

@author: miriamcorona
"""



import pandas as pd
import glob
from glob import iglob
import os 
import numpy as np  

os.chdir('/Users/miriamcorona/Desktop/NPI_Project')

# #this is the good code
path = '/Users/miriamcorona/Desktop/NPI_Project'
allFiles = glob.glob(os.path.join(path,"*.csv"))

np_array_list = []
for file_ in allFiles:
    df1 = pd.read_csv(file_)
    filename = file_
    #removing the end of the file name
    countyname = filename.replace('pcp.csv',"").replace('clinic.csv',"").replace('/Users/miriamcorona/Desktop/NPI_Project/',"")
    #converting county to string
    centy = str(countyname)
    doc = 'pcp'
#identifying wether the file says pcp or clinic to add a column later
    if doc in file_:
        segu = "pcp"
    else:
        segu = "clinic"
    #disregard code below
    #pcplocator = excel1.find('pcp')#9
    #if pcplocator:
    #    pcplocator = 'clinic'
    #csvlocator = excel1.find('.csv')#12
    #segment = excel1[pcplocator:csvlocator]
    #segu = str(segment)
    #disregard code above
    
    #identifying the amount of rows needed to add to the specific file
    index = df1.index
    number_of_rows = len(index)
    
    #creating empty lists to append to
    county = []
    seg = []
    #code below added rows to the bottom of the file instead of to the right
    #county.append(centy)
    #seg.append(seg)
    
    #this would append the exact amount of rows to the files
    for i in range(number_of_rows):
        county.append(centy)
        seg.append(segu)
    
    #this added the columsn with the data to the dataframe
    df1['county'] = pd.Series(county)
    df1['segment'] = pd.Series(seg)
    
    #disregard code below
    #print(df1)
    #df1['countyname'] = str(countyname)
    #df1['segment'] = str(segment)
    
    #will print out the first 5 rows
    print(df1.head())
    
    df1.to_csv(file_, index=False)
    
