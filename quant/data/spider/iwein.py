from bs4 import BeautifulSoup
from selenium import webdriver
# from lxml import etree
from quant.db import db,Stock


def start():
    driver = webdriver.Chrome();
    url = 'http://www.iwencai.com/stockpick/search?tid=stockpick&qs=stockpick_diag&ts=1&w='
    code='600256';
    driver.get(url + code)
    html= driver.page_source
    soup= BeautifulSoup(html,'lxml')
    tds =  soup.select(".zcwylw_table tbody tr td")
    for e in tds:
        print(e.text)
    stock = Stock('600256', 'FF')
    stock.buttom = tds[0]
    stock.top = tds[1]
    stock.up = tds[2]
    stock.down = tds[3]
    db.session.add(stock)
    db.session.commit()
    #xpath
    # selector = etree.HTML(html)
    # elems = selector.xpath('//*[@id="dp_block_5"]/div/table/tbody/tr[2]/td')
    # for e in elems:
    #     print(e.text)


    driver.close()

if __name__=='__main__':
    start()