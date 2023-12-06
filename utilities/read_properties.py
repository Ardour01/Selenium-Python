from jproperties import Properties
import os
import yaml
from yaml.loader import SafeLoader


def read_properties(keys):
    config_filepath = os.path.normpath(os.getcwd() + os.sep).rstrip(
        "/tests/") + "/data/config.properties"
    prop = Properties()
    with open(config_filepath, 'rb') as config_file:
        prop.load(config_file)
    return prop.properties[keys]


def read_yaml(key):
    config_filepath = os.path.normpath(os.getcwd() + os.sep).rstrip(
        "/utilities/") + "/data/constants.yaml"
    # Open the file and load the file
    with open(config_filepath) as f:
        data = yaml.load(f, Loader=SafeLoader)

    return data[key]
#
#
# def compare_excel():
#     from openpyxl import load_workbook
#     wb1 = load_workbook('../data/New.xlsx')
#     wb2 = load_workbook('../data/Old.xlsx')
#     for worksheet in wb1.sheetnames:
#         sheet1 = wb1[worksheet]
#         sheet2 = wb2[worksheet]
#
#         # iterate through the rows and columns of both worksheets
#         for row in range(1, sheet1.max_row + 1):
#             for col in range(1, sheet1.max_column + 1):
#                 cell1 = sheet1.cell(row, col)
#                 cell2 = sheet2.cell(row, col)
#                 if cell1.value != cell2.value:
#                     print("Sheet {0} -> Row {1} Column {2} - {3} != {4}".format(worksheet, row, col, cell1.value,
#                                                                                 cell2.value))
#
#
# compare_excel()
#
#
# # import pandas as pd
# # from pathlib import Path
# #
# #
# # def excel_diff(path_old, path_new, index_col):
# #     path_old = Path('../data/Old.xlsx')
# #     path_new = Path('../data/New.xlsx')
# #     df_old = pd.read_excel(path_old, index_col=None).fillna(0)
# #     df_new = pd.read_excel(path_new, index_col=None).fillna(0)
# #
# #     # Perform Diff
# #     df_diff = df_new.copy()
# #     dropped_rows = []
# #     new_rows = []
# #     new_cols = []
# #     dropped_cols = []
# #
# #     cols_old = df_old.columns
# #     cols_new = df_new.columns
# #     common_columns = list(set(cols_old).intersection(cols_new))
# #     uncommon_cols = list(set(cols_old).union(cols_new)-set(common_columns))
# #
# #     new_cols.append(uncommon_cols)
# #     for row in df_diff.index:
# #         if (row in df_old.index) and (row in df_new.index):
# #             for col in common_columns:
# #                 value_old = df_old.loc[row, col]
# #                 value_new = df_new.loc[row, col]
# #                 if value_old == value_new:
# #                     df_diff.loc[row, col] = df_new.loc[row, col]
# #                 else:
# #                     df_diff.loc[row, col] = '{} → {}'.format(value_old, value_new)
# #
# #         else:
# #             new_rows.append(row)
# #
# #     for row in df_old.index:
# #         if row not in df_new.index:
# #             dropped_rows.append(row)
# #             df_diff = df_diff.append(df_old.loc[row, :])
# #
# #     df_diff = df_diff.sort_index().fillna('')
# #     print(df_diff)
# #     print('\nNew Rows:     {}'.format(new_rows))
# #     print('Dropped Rows: {}'.format(dropped_rows))
# #
# #     # Save output and format
# #     fname = '{} vs {}.xlsx'.format(path_old.stem, path_new.stem)
# #     writer = pd.ExcelWriter(fname, engine='xlsxwriter')
# #
# #     df_diff.to_excel(writer, sheet_name='DIFF', index=True)
# #     df_new.to_excel(writer, sheet_name=path_new.stem, index=True)
# #     df_old.to_excel(writer, sheet_name=path_old.stem, index=True)
# #
# #     # get xlsxwriter objects
# #     workbook = writer.book
# #     worksheet = writer.sheets['DIFF']
# #     # worksheet.hide_gridlines(2)
# #     # worksheet.set_default_row(15)
# #
# #     # define formats
# #     # date_fmt = workbook.add_format({'align': 'center', 'num_format': 'yyyy-mm-dd'})
# #     # center_fmt = workbook.add_format({'align': 'center'})
# #     # number_fmt = workbook.add_format({'align': 'center', 'num_format': '#,##0.00'})
# #     # cur_fmt = workbook.add_format({'align': 'center', 'num_format': '$#,##0.00'})
# #     # perc_fmt = workbook.add_format({'align': 'center', 'num_format': '0%'})
# #     grey_fmt = workbook.add_format({'font_color': '#1560BD', 'bold': 'True'})
# #     highlight_fmt = workbook.add_format({'font_color': '#8B0000', 'bg_color': '#FFCCCB'})
# #     new_fmt = workbook.add_format({'font_color': '#32CD32', 'bold': True})
# #
# #     # set format over range
# #     ## highlight changed cells
# #     worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
# #                                                'criteria': 'containing',
# #                                                'value': '→',
# #                                                'format': highlight_fmt})
# #
# #     # highlight new/changed rows
# #     for row in range(df_diff.shape[0]):
# #         if row in new_rows:
# #             worksheet.set_row(row + 1, 15, new_fmt)
# #         if row in dropped_rows:
# #             worksheet.set_row(row + 1, 15, grey_fmt)
# #
# #
# #     # save
# #     writer.save()
# # def main():
# #     path_old = Path('../data/Old.xlsx')
# #     path_new = Path('../data/New.xlsx')
# #     # get index col from data
# #     df = pd.read_excel(path_new)
# #     index_col = df.columns[0]
# #     print('\nIndex column: {}\n'.format(index_col))
# #
# #     excel_diff(path_old, path_new, index_col)
# #
# #
# # if __name__ == '__main__':
# #     main()
# #
#
# # import csv
# #
# # def compare_csv(file1, file2):
# #     with open(file1, 'r') as f1, open(file2, 'r') as f2:
# #         csv_reader1 = csv.reader(f1)
# #         csv_reader2 = csv.reader(f2)
# #         header1 = next(csv_reader1)
# #         header2 = next(csv_reader2)
# #         if header1 != header2:
# #             print("Headers are not equal")
# #             return
# #         for row1, row2 in zip(csv_reader1, csv_reader2):
# #             if row1 != row2:
# #                 print(f"Difference at row {csv_reader1.line_num}: {row1} <> {row2}")
# #
# #             filename = "Difference.csv"
# #
# #             # writing to csv file
# #             with open(filename, 'w') as csvfile:
# #                 csvwriter = csv.writer(csvfile)
# #                 csvwriter.writerow(row1)
# #
# # compare_csv('../data/Old.csv', '../data/New.csv')
#
