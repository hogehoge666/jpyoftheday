# jpyoftheday

## Description
- USD/JPYの為替レートをYahoo Financeから取得するCLIスクリプト
- 指定した日のデータがない場合は翌日のデータ取得を再帰的に試みる
- yfinanceを利用している
- 勉強のためClean Architectureで作成したので全体的に過剰設計

## Requirements

```
beautifulsoup4==4.13.4
certifi==2025.4.26
charset-normalizer==3.4.1
click==8.1.8
frozendict==2.4.6
idna==3.10
multitasking==0.0.11
numpy==2.2.5
pandas==2.2.3
peewee==3.18.1
platformdirs==4.3.7
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.3
six==1.17.0
soupsieve==2.7
typing_extensions==4.13.2
tzdata==2025.2
urllib3==2.4.0
yfinance==0.2.57
```

## Usage

```
(venv) arm64@src  % python3 demo.py

##############################
    USD to JPY converter
##############################

Type 'q' to exit
Input date(eg: 2025-04-26): 2025-4-26

Requested Date:	2025-04-26 Sat
  Market might have been closed at the requested date.
  Here is the data from the nearest open day.
Retrieved Date:	2025-04-28 Mon
Closing Price:	143.84

Input date(eg: 2025-04-26): q

(venv) arm64@src  %
```