# -*- coding: utf-8 -*-
"""

Adapted from
https://medium.com/analytics-vidhya/top-4-pre-trained-models-for-image-classification-with-python-code-a3cb5846248b
by Alfonso Blanco García , Jul 2023
"""

######################################################################
# PARAMETERS
######################################################################

#batch_size = 128
#epochs = 30
######################################################################
import tensorflow as tf
import keras

from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model
from keras import optimizers
import numpy as np
import time

import functools

"""
Descarga del fichero de standford
https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download
https://www.analyticslane.com/2020/02/14/leer-y-guardar-archivos-de-matlab-en-python/#:~:text=La%20lectura%20de%20los%20archivos,archivo%20a%20la%20funci%C3%B3n%20loadmat%20.
DESCARGA ANNOTATIONS Y CLAS NAMES en CSV 
https://github.com/BotechEngineering/StanfordCarsDatasetCSV/blob/main/cardatasettest.csv


"""
## image path
train_data_dir = 'KaggleCarsByBrands_1_20\\train'
validation_data_dir = 'KaggleCarsByBrands_1_20\\valid'
## other
img_width, img_height = 224, 224

batch_size = 20

nb_classes = 20

nb_epoch =100
# Callback Settings:
early_stopping_patience = 10
reduce_lr_on_plateau_factor = 0.2
reduce_lr_on_plateau_patience = 3

# https://github.com/afaq-ahmad/Car-Models-and-Make-Classification-Standford_Car_dataset-mobilenetv2-imagenet-93-percent-accuracy/blob/master/Car_classification.ipynb
def get_callbacks_list(_early_stopping_patience, _reduce_lr_on_plateau_factor, _reduce_lr_on_plateau_patience):
    """Get callbacks for a model"""
    return [
       
        keras.callbacks.ModelCheckpoint(
            verbose=1,
            filepath='best_brand_1_20.h5',
            mode='max',
            monitor='val_acc',
            #monitor='top6_acc',
            save_best_only=True
        ),
      
    ]
#　start measurement
start = time.time()

# IGNORE data-augmentation parameters to ImageDataGenerator
#train_datagen = ImageDataGenerator(rescale = 1./255., rotation_range = 40, width_shift_range = 0.2, height_shift_range = 0.2,shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
train_datagen = ImageDataGenerator(rescale = 1./255.)

validation_datagen = ImageDataGenerator( rescale = 1.0/255. )

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        color_mode='rgb',
        class_mode='categorical',
        batch_size=batch_size,
        shuffle=True
)

validation_generator = validation_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        color_mode='rgb',
        class_mode='categorical',
        batch_size=batch_size,
        shuffle=True
)
from tensorflow.keras.applications.inception_v3 import InceptionV3

base_model = InceptionV3(input_shape = (224, 224, 3), include_top = False, weights = 'imagenet')

#base_model = InceptionV3(input_shape = (224, 224, 3), include_top = False)

#IGNORE  only change the last layer.

#for layer in base_model.layers:
#    layer.trainable = False
    
from tensorflow.keras.optimizers import RMSprop


x = Flatten()(base_model.output)

x = Dense(4096, activation='relu')(x)
x = Dropout(0.2)(x)
x = Dense(3072, activation='relu')(x)
x = Dropout(0.2)(x)
x = Dense(2048, activation='relu')(x)
x = Dropout(0.2)(x)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.2)(x)

x = Dense(nb_classes, activation='softmax')(x)

model = tf.keras.models.Model(base_model.input, x)



model.compile(optimizer = RMSprop(learning_rate=0.0001), loss = 'categorical_crossentropy', metrics = ['acc'])

inc_history = model.fit(train_generator, validation_data = validation_generator,
                        
                        steps_per_epoch = 10, epochs = nb_epoch,
                        callbacks=get_callbacks_list(early_stopping_patience, reduce_lr_on_plateau_factor, reduce_lr_on_plateau_patience))

model.save("ModelCarsBrands_Inception_v3_1_20.h5")