# -*- coding: utf-8 -*-
import cv2
import numpy as np
import random
from tqdm import tqdm
from keras.utils.np_utils import to_categorical

def load_data(label):
    x_train, y_train = [], []
    x_test, y_test = [], []

    # 画像ファイルのパスをtarget毎に分類
    img_path_list = {}
    target_img = ""
    target_index = -1
    with open(label, mode='r', encoding="utf-8") as f:
        label_data = f.read().split('\n')
        for data in label_data:
            # 改行コードで終わっている可能性があるので文字列の存在確認
            if data:
                path, target = data.split(',')
                if target_img != target:
                    target_img = target
                    target_index += 1
                    img_path_list[target_index] = []
                
                img_path_list[target_index].append(path)
    
    # 各画像毎に7割をtrain、3割をtestに振り分ける
    for target in tqdm(img_path_list):
        path_list = img_path_list[target]
        random.shuffle(path_list)
        train_path, test_path = path_list[0:int(len(path_list) * 0.7)], path_list[int(len(path_list) * 0.7):len(path_list)]
        # 画像を読み込み、0-1に圧縮した行列をx_train, x_testに放り込んでいく
        for train in train_path:
            img = cv2.imread(train)
            img = img/255
            x_train.append(img)
            # ラベルをone-hot vectorに変換
            y_train.append(to_categorical(target,73))
        
        for test in test_path:
            img = cv2.imread(test)
            img = img/255
            x_test.append(img)
            # ラベルをone-hot vectorに変換
            y_test.append(to_categorical(target,73))

    # numpyの配列に直して返す
    return np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)