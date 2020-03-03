# -*- coding: utf-8 -*-
import urllib.request
import os
import zipfile
from tqdm import tqdm

# ダウンロードの進捗表示
def show_progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    percent = downloaded / total_size
    now_progress = round(percent * 100)

    max_symbol_num = 20
    progress_symbol_num = round(percent * max_symbol_num)

    progress_bar = '\u2588' * progress_symbol_num + '.' * (max_symbol_num - progress_symbol_num)
    print('\rDOWNLOADING:'+progress_bar+'('+str(now_progress)+'%)', end='')

if __name__ == "__main__":

    # 画像のzipファイルを取得
    file_name = "hiragana73.zip"
    url = "http://lab.ndl.go.jp/dataset/"+file_name

    # ファイルが存在しない場合のみzipファイルをダウンロード
    zip_file_abspath = os.getcwd()+'//'+file_name
    if not os.path.isfile(zip_file_abspath):
        urllib.request.urlretrieve(url, zip_file_abspath, reporthook=show_progress)
    else:
        print('It was exist zip file.')
    
    # zipファイルの解凍ディレクトリ
    zip_file_open_root_directory = os.getcwd()+'//character_image'
    zip_file_open_directory = zip_file_open_root_directory+'//hiragana73'

    # zipファイルが解凍されてない場合のみzipファイルを解凍
    if not os.path.exists(zip_file_open_directory):
        with zipfile.ZipFile(zip_file_abspath) as zip:
            for member in tqdm(zip.infolist(), desc='Extracting '):
                try:
                    zip.extract(member, zip_file_open_root_directory)
                except zipfile.error as e:
                    pass
    else:
        print('It was already open zip file.')
