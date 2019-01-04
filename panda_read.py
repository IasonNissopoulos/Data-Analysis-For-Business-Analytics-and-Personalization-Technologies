import pandas as pd
import numpy as np
import xlsxwriter

#install to xlsxwriter gia to save se ksexorista sheets.den brika kalitero tropo na to kanw alla doulepse.
#Sta dates mou ta bgazei gia kapoio logo me ### to tsekaroume pio meta.

xls = pd.ExcelFile('POS DATA_BAPT.xlsx')
df1 = pd.read_excel(xls, 'POS DATA')
df2 = pd.read_excel(xls, 'LOYALTY')
df3 = pd.read_excel(xls, 'BARCODES')
df4 = pd.read_excel(xls, 'Categories Hierarchy')

#negatives
df1 = df1[df1["Sum_Units"] >= 0]

#changes above here
writer = pd.ExcelWriter('POS DATA_BAPT.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='POS DATA')
df2.to_excel(writer, sheet_name='LOYALTY')
df3.to_excel(writer, sheet_name='BARCODES')
df4.to_excel(writer, sheet_name='Categories Hierarchy')

writer.save()