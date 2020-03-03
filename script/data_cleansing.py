# -*- coding: utf-8 -*-
import os
import os.path
import cv2
import csv
import numpy as np
import argparse
import platform
from tqdm import tqdm

def data_cleansing(args, label_list, dir_ref_char):
    
    # イメージクレンジングを行う画像のフォルダ一覧を取得
    img_dir_list = os.listdir(args.directory)
    # ラベル用の文字列
    labels = "file_name,target\n"

    for image_dir in img_dir_list:

        # クレンジングした画像の出力先フォルダが存在しない場合は作成
        if not os.path.isdir(args.output+dir_ref_char+image_dir):
            os.makedirs(args.output+dir_ref_char+image_dir)

        # イメージの一覧を取得
        img_list = os.listdir(args.directory+dir_ref_char+image_dir)
        for image in tqdm(img_list):
            # 画像をグレイスケール化
            img = cv2.imread(args.directory+dir_ref_char+image_dir+dir_ref_char+image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # ガウシアンフィルタでぼかしを掛けて、二値化を行う
            blur = cv2.GaussianBlur(img,(5,5),0)
            ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

            # どうしてもゴミが残るのでクローズ処理を掛ける（白黒が反対なため）
            kernel = np.ones((3,3),np.uint8)
            img = cv2.dilate(img, kernel, iterations = 1)
            img = cv2.erode(img, kernel, iterations = 1)

            # クレンジングした画像を保存
            cv2.imwrite(args.output+dir_ref_char+image_dir+dir_ref_char+image, img)

            # ラベルを作成
            labels += image+","+label_list[image_dir]+"\n"
    
    # ラベルを保存
    with open('label.csv', mode='w') as f:
        f.write(labels)


if __name__ == "__main__":

    pf = platform.system()
    dir_ref_char = '/'

    if pf == 'Windows':
        dir_ref_char = '\\'

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", default=os.getcwd()+dir_ref_char+'character_image'+dir_ref_char+'hiragana73')
    parser.add_argument("-o", "--output", default=os.getcwd()+dir_ref_char+'character_image'+dir_ref_char+'conv_hiragana73')
    parser.add_argument("-l", "--label", default=os.getcwd()+dir_ref_char+'hiragana_label.csv')
    args = parser.parse_args()

    # ラベル作成用のデータをcsvから読み出し
    label_list = {}
    with open(args.label) as f:
        label_data = f.read().split('\n')
        for data in label_data:
            label = data.split(',')
            label_list[label[0]] = label[1].strip()

    data_cleansing(args, label_list, dir_ref_char)
