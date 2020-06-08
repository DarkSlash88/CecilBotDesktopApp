import xlrd
import re

# Open specified excel file and read data from file.
# Warning: when files are updated and their names get changed, you
#   must update the hard coded file name in DataBuilder.py
def dict_builder(path=""):
    location = path
    book = xlrd.open_workbook(location)
    sheet = book.sheet_by_index(0)
    sheet.cell_value(0, 0)
    data_dictionary = dict()

    for rownum in range(1, sheet.nrows):
        tempdict = dict()
        for cn, values in zip(sheet.row_values(0, 1), sheet.row_values(rownum, 1)):
            if (values != ""):
                tempdict[cn] = values
        if (re.match(r".*Root Table.*", location, re.IGNORECASE)):
            data_dictionary[str(sheet.cell_value(rownum, 0))] = tempdict
        else:
            data_dictionary[str(sheet.cell_value(rownum, 0)).lower()] = tempdict

    return data_dictionary
