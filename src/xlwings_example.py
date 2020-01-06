import xlwings as xw
import datetime as dt
import pandas as pd

wb = xw.Book('C:\\Users\\NickTsai\\Desktop\\XlwingsProject\\xlwings_test.xlsm')
wsData = wb.sheets['Data']

# ndim
wsData.range('A1').value = [[100,200], [300, 400]]
    # will read data from excel as list
    # Excel will read the sheet from up to down, left to right => [[100.0], [300.0]]
print(wsData.range('A1:A2').options(ndim=1).value)
    # will divided into two list since there are two rows => [[100.0], [300.0]]
print(wsData.range('A1:A2').options(ndim=2).value)
    # will only have one list since there is only one row => [[100.0, 200.0]]
print(wsData.range('A1:B1').options(ndim=2).value)


# numbers
wsData.range('A1').value = 100
    # will read the data from excel, then change the data type regarding to the given type
print(wsData.range('A1').options(numbers=int).value)
print(wsData.range('A1').options(numbers=float).value)
    # default will be flot
print(wsData.range('A1').options().value)


# dates
wsData.range('A1').value = dt.datetime.now()
print(wsData.range('A1').options(dates=dt.date).value)


# empty
    # fulfill the empty as given value
print(wsData.range('A1:C1').value)
print(wsData.range('A1:C1').options(empty='NA').value)


# transpose
wsData.cells.clear_contents()
wsData.range('A1').value = [100,200,300, 400]
wsData.range('A1').options(transpose=True).value = [100,200,300, 400]


# Read data then convet as dataframe
wsPdF = wb.sheets['pd_dataframe']
df1 = wsPdF.range('A1').options(pd.DataFrame, expand='table',header=1).value
df2 = wsPdF.range('A1').options(pd.DataFrame, expand='table',header=2).value