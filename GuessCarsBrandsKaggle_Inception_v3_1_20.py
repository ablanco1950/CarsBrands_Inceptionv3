# -*- coding: utf-8 -*-
"""

 Alfonso Blanco García , Jun 2023
"""

######################################################################
# PARAMETERS
######################################################################

######################################################################

import os
import re

import cv2

import numpy as np
import keras
import functools  
import time
inicio=time.time()

TabCarBrand=[]

f=open("CarBrand.csv","r")

for linea in f:
    lineadelTrain =linea.split(",")
    TabCarBrand.append(lineadelTrain[3])

def GetBrandFromModel(Modelo):
    f=open("CarBrand.csv","r")
    
    for linea in f:
        lineadelTrain =linea.split(",")
        ModelFrom=int(lineadelTrain[1])
        ModelTo=int(lineadelTrain[2])
        if Modelo >= ModelFrom and Modelo <= ModelTo:
            return int(lineadelTrain[0]), lineadelTrain[3]
    print("RARO NO ENCUENTRA EL MODELO")
    return -1, ""

def loadimagesTest():
    
    images=[]
    Y=[]
    imagesName=[]
    f=open("cardatasettrain.csv","r")
    ContTraining=0
    ContValid=0
    Conta=0;
    for linea in f:
        Conta=Conta+1
        if Conta==1: continue
        
        
        if Conta < 8000: continue
       
        lineadelTrain =linea.split(",")
       
        NameImg=lineadelTrain[6]
        # OJO LLEVA UN CR AL FINAL
        NameImg=NameImg[0:9]
        
        img=cv2.imread('C:\\archiveKaggle\\cars_train\\cars_train' + '\\'+str(NameImg)) 
       
        img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
               
        
        Modelo=int(lineadelTrain[5])
        Brand, BrandName=GetBrandFromModel(Modelo)
        if Brand==-1 :
            print ("NO SE ENCUENTRA MODELO " + str(Modelo) + " en " + NameImg)
        if Brand >20: continue
        Y.append(Brand)
        images.append(img)
        imagesName.append(NameImg)
       
    return images, Y, imagesName


def PredictModel(model,x_test_test):
    predictions1=model.predict(x_test_test)
    #print(predictions1)
    
    predictions=np.argmax(predictions1, axis=1)
    #print(predictions)
    p=[]
    
    p.append(predictions1[0][predictions])
    
    return predictions, p, predictions1
    
###########################################################
# MAIN
##########################################################

from tensorflow.keras.models import load_model

model_1_10 = load_model('best_brand_1_20.h5')

#model_1_10 = load_model('ModelCarsBrands_Inception_v3_1_20.h5')

X_test, Y_test, imageName_test = loadimagesTest()

x_test=np.array(X_test)

# Scale images to the [0, 1] range
x_test = x_test.astype("float32") / 255.0


TotalHits=0
TotalFailures=0
with open( "BrandsResults.txt" ,"w") as  w:
    
    
    
    for i in range(len(x_test)):
        
                
        TabP=[]
        TabModel=[]
        TabPredictions1=[]
        
        
        x_test_test=[]
        x_test_test.append(x_test[i])
       
        x_test_test=np.array(x_test_test)
        
        
        predictions, p, predictions1 = PredictModel(model_1_10,x_test_test)
            
        
        predictions=int(predictions[0])
        predictions=predictions+1
        
        
        IndexCarBrandPredict=predictions-1
        IndexCarBrandTrue=Y_test[i]-1
        NameCarBrandPredict=TabCarBrand[IndexCarBrandPredict]
        NameCarBrandTrue=TabCarBrand[IndexCarBrandTrue]
        if Y_test[i]!=predictions:
            TotalFailures=TotalFailures + 1
            print("ERROR " + imageName_test[i]+ " is assigned brand " + str(predictions)
                  +  NameCarBrandPredict + "  True brand is " + str(Y_test[i])+ NameCarBrandTrue)
                  
        else:
            print("HIT " + imageName_test[i]+ " is assigned brand " + str(predictions)
                  +  NameCarBrandPredict )
           #      + "probabilidad = " + str(Pmax))
                 
          #print("probabilidad = " + str(p[0]))
            TotalHits=TotalHits+1
        lineaw=[]
        lineaw.append(imageName_test[i]) 
        lineaw.append(str(Y_test[i]))
        lineaw.append(NameCarBrandTrue)
        
        lineaw.append(NameCarBrandPredict)
        lineaw.append( str(p))
        lineaWrite =','.join(lineaw)
        lineaWrite=lineaWrite + "\n"
        w.write(lineaWrite)
          
print("")
print("Total hits = " + str(TotalHits))  
print("Total failures = " + str(TotalFailures) )     
print("Accuracy = " + str(TotalHits*100/(TotalHits + TotalFailures)) + "%") 
