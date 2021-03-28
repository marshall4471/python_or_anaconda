# -*- coding: utf-8 -*-
"""python_or_anaconda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iTK2zg7UYjFT1Otmg-c0FVclz4nCkQMt
"""

import zipfile
from google.colab import drive

drive.mount('/content/gdrive/')



file1 = ("/content/gdrive/MyDrive/archive/train")

file2 = ("/content/gdrive/MyDrive/archive/valid")

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.05,
                                   zoom_range = 0.05,
                                   horizontal_flip = True)

train_set = train_datagen.flow_from_directory(file1,
                                                 target_size = (384, 384),
                                                 batch_size = 16,
                                                 class_mode = 'binary')

import tensorflow as tf

test_datagen = ImageDataGenerator(rescale = 1./255)

test_set = test_datagen.flow_from_directory(file2,
                                            target_size = (384, 384),
                                            batch_size = 16,
                                            class_mode = 'binary')
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(128, kernel_size=[5,5], padding='valid', activation='relu', input_shape=[384, 384, 3]))
model.add(tf.keras.layers.MaxPooling2D(pool_size=[3,3], strides=2, padding='valid'))
model.add(tf.keras.layers.Conv2D(32, kernel_size=[3,3], padding='valid', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=[3,3], strides=2, padding='valid'))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer = 'adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(train_set, validation_data =test_set, epochs=15, verbose=1)
history.history['accuracy']
model.save("snake_pred6.h5")



