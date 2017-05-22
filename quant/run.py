from db import db,Stock
from data import  xls2db
from data.spider import iwein
def input():
    list = xls2db.excel_table_byindex('data/a.xls')
    for e in list:
        print(e)
        code = e.get('股票代码')[:-3]
        name = e.get('股票简称')
        print(name, code)
        stock = Stock(code=code, name=name)
        db.session.add(stock)
        db.session.commit()
def get_data():
    return Stock.query.all()

if __name__ == '__main__':
    iwein.start(get_data())