# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:26:13 2020

@author: Muhammed Hassan M
"""

import os
#dir(os)
#import glob
import shutil
TRAIN_DIR = 'C:/Users/Muhammed Hassan M/Desktop/DANCE_FORM_DETECTION/Dataset/Prepared_data_for_Transfer_learnig/train'
VALID_DIR = 'C:/Users/Muhammed Hassan M/Desktop/DANCE_FORM_DETECTION/Dataset/Prepared_data_for_Transfer_learnig/valid'

for folder in os.listdir(TRAIN_DIR):
    print(folder)
    if not os.path.isdir('C:/Users/Muhammed Hassan M/Desktop/DANCE_FORM_DETECTION/Dataset/Prepared_data_for_Transfer_learnig/valid/'+folder):
        os.mkdir('C:/Users/Muhammed Hassan M/Desktop/DANCE_FORM_DETECTION/Dataset/Prepared_data_for_Transfer_learnig/valid/'+folder)
    percent = int(len(os.listdir(os.path.join(TRAIN_DIR,folder)))*20/100)
    print( len(os.listdir(os.path.join(TRAIN_DIR,folder))))
    
    for image in os.listdir(os.path.join(TRAIN_DIR,folder)):
        
        if len(os.listdir(os.path.join(VALID_DIR,folder))) != percent:
            print(percent)
            shutil.move(os.path.join(TRAIN_DIR,folder,image),os.path.join(VALID_DIR,folder))
        else:
            pass
                


