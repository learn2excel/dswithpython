# Exploratory Data Analysis
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv, find_dotenv

dotenvpath = find_dotenv()
load_dotenv(dotenvpath)

rawdatapath = os.environ.get("RAW_DATA_PATH")
print(rawdatapath)
train_file_path = os.path.join(rawdatapath, 'train.csv')
test_file_path = os.path.join(rawdatapath, 'test.csv')

train_df = pd.read_csv(train_file_path, index_col='PassengerId')

print(train_df.info())

print(train_df.head(10))

print(train_df.tail())

test_df = pd.read_csv(test_file_path, index_col='PassengerId')

test_df['Survived'] = -999

print(test_df.info())

df=pd.concat((test_df, train_df), axis=0)

print(df.info())
print(df[['Name','Age']])