# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:09:16 2020

@author: Muhammed Hassan M
"""
import os
import shutil
import pandas as pd

TRAIN_CSV_PATH = 'C:/Users/Muhammed Hassan M/Desktop/DANCE_FORM_DETECTION/dataset/train.csv'
TRAIN_IMG_DIR = 'C:/Users/Muhammed Hassan M/Desktop/DANCE_FORM_DETECTION/dataset/train'
df = pd.read_csv(TRAIN_CSV_PATH)
classes = df.target.unique()
class_count =df.groupby('target').size()
#df.iloc[0]
manipuri = 0
bharatanatyam = 0
odissi = 0
kathakali = 0
kathak = 0
sattriya = 0
kuchipudi = 0
mohiniyattam = 0

for class_ in classes:
    if not os.path.exists(class_):
        os.mkdir(os.path.join(os.getcwd(),class_))
    else:
        pass
for index, row in df.iterrows():
   
    if row['target'] == classes[0]:
        print(row['Image'])
        try:
            
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[0],row['Image']))
            manipuri+=1
        
        except:
            print("Files Allready Moved")
    else:
        pass
        
    if row['target'] ==classes[1] :
        print(row['Image'])
        try:
            
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[1],row['Image']))
            bharatanatyam+=1
        
        except:
            print("Files Allready Moved")
    else:
        pass
        
    if row['target'] == classes[2]:
        print(row['Image'])
        try: 
            
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[2],row['Image']))
            odissi+=1
        
        except:
            print("Files Allready Moved")
    else:
        pass
     
    if row['target'] == classes[3]:
        print(row['Image'])
        try:
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[3],row['Image']))
            kathakali+=1
        except:
            print("Files Allready Moved")
    else:
        pass
    if row['target'] == classes[4]:
        print(row['Image'])
        try:
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[4],row['Image']))
            kathak+=1
        except:
            print("Files Allready Moved")
    else:
        pass
    if row['target'] == classes[5]:
        print(row['Image'])
        try:
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[5],row['Image']))
            sattriya+=1
        except:
            print("Files Allready Moved")
    else:
        pass
    if row['target'] == classes[6]:
        print(row['Image'])
        try:
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[6],row['Image']))
            kuchipudi+=1
        except:
            print("Files Allready Moved")
    else:
        pass
    if row['target'] == classes[7]:
        print(row['Image'])
        try:
            shutil.move(os.path.join(TRAIN_IMG_DIR,row['Image']),os.path.join(os.getcwd()+'\\'+classes[7],row['Image']))
            mohiniyattam+=1
        except:
            print("Files Allready Moved")
    else:
        pass
    

