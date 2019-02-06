import pandas as pd

import xlsxwriter

xls = pd.ExcelFile('POS_EVERYONE.xlsx')
df1 = pd.read_excel(xls, 'POS DATA')
df2 = pd.read_excel(xls, 'LOYALTY')
df3 = pd.read_excel(xls, 'BARCODES')
df4 = pd.read_excel(xls, 'Categories Hierarchy')

df3 = pd.merge(df3, df4, how='left', on=['CategoryA', 'CategoryB','CategoryC', 'CategoryD'])
df1 = pd.merge(df1, df3, left_on='Barcode', right_on='Barcode', how='left')
writer = pd.ExcelWriter('POS_EVERYONE.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='POS DATA')
df2.to_excel(writer, sheet_name='LOYALTY')
df3.to_excel(writer, sheet_name='BARCODES')
df4.to_excel(writer, sheet_name='Categories Hierarchy')




writer.save()
