import xlrd

def dict_builder(path=""):
    location = path
    book = xlrd.open_workbook(location)
    sheet = book.sheet_by_index(0)
    sheet.cell_value(0, 0)
    data_dictionary = dict()

    for rownum in range(1, sheet.nrows):
        tempdict = dict()
        for cn, values in zip(sheet.row_values(0, 1), sheet.row_values(rownum, 1)):
            tempdict[cn] = values
        data_dictionary[sheet.cell_value(rownum, 0)] = tempdict

    return data_dictionary
