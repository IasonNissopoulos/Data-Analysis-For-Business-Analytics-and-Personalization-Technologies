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
#df1 = df1[df1["Sum_Units"] >= 0]

#NULL->df2['Children'] = df2['Children'].fillna(0)
#auta girnane pisw 6000 kati stoixeia pou exoun unknown
#ama den ginete mporoume na tous dwsume random timi
a = df2[df2['Sex'] == 'Unknown']
b = list(a['CardholderID'].values.flatten()) 
c = list(df1['Card_ID'].values.flatten())

#count = 0

dic = dict.fromkeys(b,0)
print(len(dic))
for i in c:
   if i in dic.keys():
      dic[i] += 1 
print(dic)


#changes above here
writer = pd.ExcelWriter('POS DATA_BAPT.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='POS DATA')
df2.to_excel(writer, sheet_name='LOYALTY')
df3.to_excel(writer, sheet_name='BARCODES')
df4.to_excel(writer, sheet_name='Categories Hierarchy')

writer.save()