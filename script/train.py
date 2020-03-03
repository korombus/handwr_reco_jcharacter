# -*- coding: utf-8 -*-
# general
import os
import numpy as np
import argparse
import random
from tqdm import tqdm
from matplotlib import pyplot as plt

# original
import common
import data_loader

# training
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop

def create_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(4, 4), activation='relu', input_shape=(48, 48, 3)))
    model.add(Conv2D(64, (4, 4), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(73, activation='softmax'))
    
    return model


if __name__ == "__main__":
    dir_ref_char = common.get_directory_reference_char()

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--label", default=os.getcwd()+dir_ref_char+'label.csv')
    args = parser.parse_args()

    # データ読み込み
    train_x, train_y, test_x, test_y = data_loader.load_data(args.label)

    # モデル生成
    model = create_model()
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

    # 学習開始
    history = model.fit(train_x, train_y, batch_size=128, epochs=10, verbose=1, validation_data=(test_x, test_y))

    score = model.evaluate(test_x, test_y, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    # 精度のplot
    plt.plot(history.history['accuracy'], marker='.', label='acc')
    plt.plot(history.history['val_accuracy'], marker='.', label='val_acc')
    plt.title('model accuracy')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(loc='best')
    plt.savefig('accuracy.png')

    plt.figure()

    # 損失のplot
    plt.plot(history.history['loss'], marker='.', label='loss')
    plt.plot(history.history['val_loss'], marker='.', label='val_loss')
    plt.title('model loss')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(loc='best')
    plt.savefig('loss.png')