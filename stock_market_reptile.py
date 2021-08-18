# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:22:36 2021

@author: su
"""
import requests
from io import StringIO
import pandas as pd

datestr = input("請輸入查詢日期: ")
stock_symbol = input("請輸入股票代碼: ")

# 下載股價
data = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

data_text = data.text.split('\n')

data_text = [i for i in data_text if len(
    i.split('",')) == 17 and i[0] != '=']

alldata = "\n".join(data_text)
df = pd.read_csv(StringIO(alldata), header=0)

df = df.drop(columns=['Unnamed: 16'])
filter_df = df[df["證券代號"] == stock_symbol]
print(filter_df)
