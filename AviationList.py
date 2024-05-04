import pandas as pd
from pandas import *
import csv

df = pd.read_excel('1.xlsx')

df = df.drop(columns=['MAKE', 'MODEL','FRACPERCENTOWNED', 'FRACPURCHASEDATE',
'COMPALTNAME', 'COMPWEBADDRESS', 'COMPADDRESS1','COMPADDRESS2', 'COMPCITY', 'COMPSTATE',
'COMPSTATEABBR', 'COMPZIPCODE', 'COMPOFFICE', 'COMPFAX','COMPMOBILE','CONTACTPREFIX', 'CONTACTFIRSTNAME',
'CONTACTMI', 'CONTACTLASTNAME', 'CONTACTSUFFIX', 'CONTACTTITLE', 'CONTACTOFFICE', 'CONTACTFAX', 'CONTACTMOBILE', 
'YEARMFR', 'YEARDLV', 'BASEIATA', 'BASEICAO', 'BASENAME', 'BASECITY', 'BASESTATE', 'BASESTATEABBR','AFTT',
'ENG1TT', 'ENG2TT', 'ENG3TT', 'ENG4TT', 'SMOH1', 'SMOH2', 'SMOH3', 'SMOH4', 'STATUS', 'ASKING', 'ASKINGAMT',
'DATELISTED', 'PURCHASEDATE', 'ACID', 'COMPID', 'CONTACTID'])


df = df.loc[(df['RELATION'] == 'Owner') | (df['RELATION'] == 'Chief Pilot') | (df['RELATION'] == 'Co-Owner') | 
(df['RELATION'] == 'Flight Department') | (df['RELATION'] == 'Lessee') |
(df['RELATION'] == 'Operator')]

df= df.loc[(df['COMPCOUNTRY'] != 'Russian Federation') & (df['COMPCOUNTRY'] != 'Iran') & (df['COMPCOUNTRY'] != 'Venezuela') &
(df['BASECOUNTRY'] != 'Russian Federation') & (df['BASECOUNTRY'] != 'Iran') & (df['BASECOUNTRY'] != 'Venezuela') & (df['BASECOUNTRY'] != 'China') &
(df['COMPCOUNTRY'] != 'China')]

df= df.loc[(df['COMPANY'] != 'ACME Inc.') & (df['COMPANY'] != 'Stinky, Inc.')]

df= df.loc[(df['COMPEMAIL'] != 'Sponge@squarepants.com') & (df['COMPEMAIL'] != 'pikachoo@zippy.com')]

df= df.loc[(df['CONTACTEMAIL'] != 'Sponge@squarepants.com') & (df['CONTACTEMAIL'] != 'pikachoo@zippy.com')]

df = df.to_excel('imp.xlsx')

print(df)
