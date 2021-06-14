# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:37:20 2021

@author: leesy
"""
import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
from collections import defaultdict, Counter
from scipy import signal
import numpy as np
import librosa
import random as rn
from keras.layers import Dense
from keras import Input
#from keras.engine import Model
#from keras.utils import to_categorical
#from keras.layers import *
from keras.models import load_model
import tensorflow as tf
from tensorflow import keras



pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))

def load_file(path): 
       
    input_mfcc = []    
      
    files = os.listdir(path)        
    for wav in files:
        if not wav.endswith(".wav"):continue
        else:               
            w, sr = librosa.load(path+"/"+wav)
            mfcc = librosa.feature.mfcc(w)
            padded_mfcc = pad2d(mfcc, 40)

            input_mfcc.append(padded_mfcc)

    input_data = np.array(input_mfcc)
    
    print(input_data.shape)


    return input_data


def find_celeb(sample_path):
    path = sample_path
    input_data = load_file(path)
    result = []
    model = load_model('./0603-1_20_1000(75%)')
    model.load_weights('./0603-1_20_1000(75%)/103-- 0.7500.hdf5')
    tot = 0
    
    model.summary()
    output_ = model.predict(input_data)
    predict = np.argmax(output_)
    for i in range(len(output_[0])):
        tot += output_[:, i]
        
    acc = output_[:, predict]/tot * 100
    ## print(output_)
    ##print(predict)
    ##print(tot)
    ##print(output_[:, predict])
    if (predict == 0):
        celeb = 'Dr.dre'
    elif (predict == 1):
        celeb = 'Megan Fox'
    elif (predict == 2):
        celeb = '박명수'
    elif (predict == 3):
        celeb = '서현'
    elif (predict == 4):
        celeb = 'Steve Jobs'
    elif (predict == 5):
        celeb = '임시완' 
    elif (predict == 6):
        celeb = 'Taylor Swift'
    else:
        celeb = '한예슬'
    result.append(celeb)
    result.append(acc)
    print(celeb)
    print(acc)
    return result

#find_celeb('./test')