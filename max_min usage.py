# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:34:05 2022

@author: ishar
"""

import matplotlib.pyplot as plt
import psutil as p
app_name_list={}

count=0

for process in p.process_iter():
    count=count+1
    if count <= 6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("name :  ",name,"-- cpu usage : ",cpu_usage)
        app_name_list.update({name:cpu_usage})
        
        
keymax=max(app_name_list, key= app_name_list.get)
print(keymax)
keymin=min(app_name_list, key=app_name_list.get)
print(keymin)
name_list=[keymax,keymin]
print(name_list)

app=app_name_list.values()
maxapp=max(app)
print("maximum: ",maxapp)
minapp=min(app)
print("minimum: ",minapp)
max_min_list=[maxapp,minapp]
print(max_min_list)
        
        

plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("CPU Usage")
plt.bar(name_list, max_min_list,width=0.6, color=("purple","red"))
plt.show()
    
    