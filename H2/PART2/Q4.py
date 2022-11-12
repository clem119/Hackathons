from imports import *
from Q1 import df
import datetime

def cmpDates(d1, d2):
    C1 = convert(d1)
    C2 = convert(d2)
    for i in range(3):
        if (C1[i] != C2[i]): return C1[i]-C2[i]
    return 0
    
def convert(date):
    return (
        int(date[:2]),
        int(date[3:5]),
        int(date[6:])
        )

def convertSec(date):
    return int(
        f"20{int(date[:2])}{date[3:5]}{date[6:]}"
    )

start_date = '15-01-02'
intermidate_date = '18-12-01'
end_date = '18-12-31'

mark1 = (cmpDates(df['Date'], start_date) > 0) & (cmpDates(df['Date'], intermidate_date) <= 0)
mark2 = (cmpDates(df['Date'], intermidate_date) < 0) & (cmpDates(df['Date'], end_date) <= 0)

traningSet = df.loc[mark1]
validationSet = df.loc[mark2]
print(traningSet)
print(validationSet)