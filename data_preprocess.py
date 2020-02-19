# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:22:33 2020

@author: 2010
"""

import pandas as pd
import json
import pickle

with open('multilabeldatas/data.txt','rb') as f:
    string = f.readlines()
    f.close()

df = pd.DataFrame(columns=['index', 'labels', 'sentence'])
for line in string:
    
    string = line.decode()
    string = string.strip('\r\n')
    string = string.strip(',')
    j = json.loads(string)
    for i in j['labels']:
      j[i] = 1
    a = pd.DataFrame([j])
    df =df.append(a,ignore_index=True)
    

f = open('df12','wb+')
pickle.dump(df,f)
f.close()