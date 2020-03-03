# -*- coding: utf-8 -*-
# general
import os
import numpy as np
import argparse
import random
from tqdm import tqdm

# original
import common
import data_loader

# training
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop

def create_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(4, 4), activation='relu', input_shape=(48, 48, 1)))
    model.add(Conv2D(64, (4, 4), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(47, activation='softmax'))
    
    return model


if __name__ == "__main__":
    dir_ref_char = common.get_directory_reference_char()

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--label", default=os.getcwd()+dir_ref_char+'label.csv')
    args = parser.parse_args()

    # データ読み込み
    train_x, train_y, test_x, test_y = data_loader.load_data(args.label)

    print(train_x.shape)
    print(train_y.shape)
    print(test_x.shape)
    print(test_y.shape)