# -*- coding: utf-8 -*-
from db import db,Stock
from data import  xls2db
from data.spider import iwein
def input():
    list = xls2db.excel_table_byindex('data/a.xls')
    for e in list:
        print(e)
        code = e.get('code')[:-3]
        name = e.get('name')
        print(name, code)
        stock = Stock(code=code, name=name)
        db.session.add(stock)
        db.session.commit()
def get_data():
    return Stock.query.all()

if __name__ == '__main__':
    # input()
    iwein.start(get_data())