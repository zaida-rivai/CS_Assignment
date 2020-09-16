#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:38:24 2020

@author: zaidarivai
"""

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("istherecorrelation.csv",delimiter=';')

fig, ax = plt.subplots()

# fig.set_size_inches(3, 1.5)


fig, ax = plt.subplots()
plt.scatter(df.iloc[:,0],df.iloc[:,-1],label="Netherlands")
# plt.scatter(df.iloc[:,0],df.iloc[:,1])
plt.xlabel("Year")
plt.ylabel("Annually beer consumption (x1000 hectoliter)")
plt.legend()
plt.show()
fig.savefig('myfig.png',dpi=300)