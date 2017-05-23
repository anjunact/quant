# -*- coding: utf-8 -*-
import urllib
import datetime

def download_stock_data(stock_list):
    for sid in stock_list:
          url='http://finance.yahoo.com/d/quotes.csv?s='
        url = 'http://table.finance.yahoo.com/table.csv?s=' + sid
        fname = sid + '.csv'
        print('downloading %s form %s' % (fname, url))
        urllib.urlretrieve(url, fname)

if __name__ == '__main__':
    stock_list = ['300001.sz', '300002.sz']
    download_stock_data(stock_list)