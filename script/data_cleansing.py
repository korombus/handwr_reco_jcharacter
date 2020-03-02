# -*- coding: utf-8 -*-
import os
import os.path
import cv2
import numpy as np
import argparse
from tqdm import tqdm

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", default=os.getcwd()+r'\character_image\hiragana73')
    parser.add_argument("-o", "--output", default=os.getcwd()+r'\character_image\conv_hiragana73')
    args = parser.parse_args()

    # イメージクレンジングを行う画像のフォルダ一覧を取得
    img_dir_list = os.listdir(args.directory)
    for image_dir in img_dir_list:

        # クレンジングした画像の出力先フォルダが存在しない場合は作成
        if not os.path.isdir(args.output+'\\'+image_dir):
            os.mkdir(args.output+'\\'+image_dir)

        # イメージの一覧を取得
        img_list = os.listdir(args.directory+'\\'+image_dir)
        for image in tqdm(img_list):
            # 画像をグレイスケール化
            img = cv2.imread(args.directory+'\\'+image_dir+'\\'+image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # ガウシアンフィルタでぼかしを掛けて、二値化を行う
            blur = cv2.GaussianBlur(img,(5,5),0)
            ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

            # どうしてもゴミが残るのでクローズ処理を掛ける（白黒が反対なため）
            kernel = np.ones((3,3),np.uint8)
            img = cv2.dilate(img, kernel, iterations = 1)
            img = cv2.erode(img, kernel, iterations = 1)

            # クレンジングした画像を保存
            cv2.imwrite(args.output+'\\'+image_dir+'\\'+image, img)