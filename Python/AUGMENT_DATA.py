# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:17:41 2020

@author: Muhammed Hassan M
"""


from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
# keras.preprocessing.image.ImageDataGenerator(featurewise_center=False, samplewise_center=False,\
#                                              featurewise_std_normalization=False, samplewise_std_normalization=False,
#                                              zca_whitening=False, zca_epsilon=1e-06, rotation_range=0, width_shift_range=0.0, height_shift_range=0.0,\
#                                              brightness_range=None, shear_range=0.0, zoom_range=0.0,\
#                                              channel_shift_range=0.0, fill_mode='nearest', cval=0.0, horizontal_flip=False,\
#                                              vertical_flip=False, rescale=None, preprocessing_function=None, data_format='channels_last', \
#                                              validation_split=0.0, interpolation_order=1, dtype='float32')

datagen = ImageDataGenerator(
            rescale=1./255,
            featurewise_center = True,
            featurewise_std_normalization=True,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            vertical_flip=False,
            fill_mode='reflect',
            data_format='channels_last',
            brightness_range=[0.5, 1.5],
            )
directory = 'C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/DEMO_2/Deep_Learning/Dataset/RESIZED/RESIZED_TIF_105'
directory_name = directory.split("/")[-1]+"_"
if not os.path.isdir('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/DEMO_2/Deep_Learning/Dataset/AUGMENTED/'+directory_name+"AUGMENTED"):
         os.mkdir('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/DEMO_2/Deep_Learning/Dataset/AUGMENTED/'+directory_name+"AUGMENTED")
for filename in os.listdir(directory):
    img = load_img(directory+"/"+filename)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    j = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/DEMO_2/Deep_Learning/Dataset/AUGMENTED/', save_prefix=directory_name, save_format='jpg'):
        i += 1
        j += 1
        if i > 20:
            break  # otherwise the generator would loop indefinitely