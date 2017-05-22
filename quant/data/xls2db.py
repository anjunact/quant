import xlrd

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print (str(e))
    # finally:
    #     print(2)
def excel_table_byindex(file='file.xls', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheet_by_index(by_index)
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list
