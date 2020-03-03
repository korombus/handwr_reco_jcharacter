# Japanese Hiragana handwriting recognition.
本リポジトリは、手書き文字認識を実験的に行っています。

## Environment
`Python 3.7.2` `pip 20.0.2` 

## Usage
```
$ pip install -r requirements.txt
$ python download.py
$ python script/data_cleansing.py
$ python script/train.py
```

## Experiment training
![accuracy](https://user-images.githubusercontent.com/8738033/75785583-55492500-5da7-11ea-88f7-b5e8b92068a9.png)
![loss](https://user-images.githubusercontent.com/8738033/75785687-7c9ff200-5da7-11ea-96f7-be2f40a92c51.png)

```
Test loss: 0.062190211799325185
Test accuracy: 0.9849777221679688
```

## Tips
本実験で利用している手書き文字のデータセットは以下で公開されているデータを利用しています。
> NDLラボ 文字画像データセット(平仮名73文字版)<br />
> https://lab.ndl.go.jp/cms/hiragana73
