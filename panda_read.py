import pandas as pd
import numpy as np

xls = pd.ExcelFile('POS DATA_BAPT.xlsx')
df1 = pd.read_excel(xls, 'POS DATA')
df2 = pd.read_excel(xls, 'LOYALTY')
df3 = pd.read_excel(xls, 'BARCODES')
df4 = pd.read_excel(xls, 'Categories Hierarchy')

print(df1.loc[: , "Date"])
