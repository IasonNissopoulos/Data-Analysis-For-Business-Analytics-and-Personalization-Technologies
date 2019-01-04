import pandas as pd
import numpy as np
import xlsxwriter

xls = pd.ExcelFile('POS DATA_BAPT.xlsx')
df1 = pd.read_excel(xls, 'POS DATA')
df2 = pd.read_excel(xls, 'LOYALTY')
df3 = pd.read_excel(xls, 'BARCODES')
df4 = pd.read_excel(xls, 'Categories Hierarchy')

df1 = df1[df1["Sum_Units"] >= 0]

writer = pd.ExcelWriter('POS DATA_BAPT.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='POS DATA')
df2.to_excel(writer, sheet_name='LOYALTY')
df3.to_excel(writer, sheet_name='BARCODES')
df4.to_excel(writer, sheet_name='Categories Hierarchy')

writer.save()