import pandas as pd
#import datetime as dt
#import pandasql as ps
import os
import zipfile as zp
#import matplotlib.pyplot as plt

DIR=r'/home/anuj/Downloads'
ZIp='archive(2).zip'

os.chdir(DIR)
zf = zp.ZipFile(f'{ZIp}')

dfs={}
for name in zf.namelist():
    df_name= name.replace('.csv','')
    dfs[df_name]=pd.read_csv(zf.open(name,mode='r'),encoding='latin')

sales_store=dfs['Salesstore']
#sales_store.columns=sales_store.columns.str.replace(' ','_')

#sales_store[sales_store.duplicated()]## Check duplicates
#sales_store.info()
#sales_store.isnull().values.any() ########Check NUlls
#sales_store.isnull().isnull().sum() ########Check NUlls by each column

sales_store.info()
