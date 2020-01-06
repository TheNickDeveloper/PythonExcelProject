import xlwings as xw
import pandas as pd
from enum import Enum

def get_last_row(worksheet, start_count_row):
    return worksheet.cells(worksheet.api.rows.count, start_count_row).end(-4162).row

def get_last_col(worksheet, start_count_col):
    return worksheet.cells(start_count_col, worksheet.api.columns.count).end(-4159).column

def get_range_dataframe(worksheet, start_count_row, start_count_col, header_count=1):
    return worksheet.range(worksheet.cells(start_count_row, start_count_col)).options(pd.DataFrame, expand='table',header=header_count).value