from enum import Enum
import pandas as pd

class FileType(Enum):
    Csv = 1
    Text = 2
    Excel = 3
    Json = 4

def read_file_as_datafram(file_path, file_type):
    if file_type == FileType.Csv:
        return pd.read_csv(file_path)

    if file_type == FileType.Excel:
        return pd.read_excel(file_path)

    if file_type == FileType.Text:
        return pd.read_csv(file_path, sep='\t')
        
    if file_type == FileType.Json:
        return pd.read_json(file_path)


def export_file(data_fram, export_file_type, folder_path, file_name, include_index = False):
    export_destination = folder_path + '\\' + file_name

    if export_file_type == FileType.Csv:
        data_fram.to_csv(export_destination + '.csv', index=include_index)

    if export_file_type == FileType.Excel:
        data_fram.to_excel(export_destination + '.xlsx', index=include_index)

    if export_file_type == FileType.Text:
        data_fram.to_csv(export_destination + '.txt', index=include_index, sep='\t')

    if export_file_type == FileType.Json:
        data_fram.to_json(export_destination + '.json', index=include_index)