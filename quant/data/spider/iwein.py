from bs4 import BeautifulSoup
from selenium import webdriver
# from lxml import etree
import  os,sys
from  os.path import  dirname
fpath = os.path.abspath(__file__)

sys.path.append(dirname(dirname(dirname(fpath))))
print(sys.path)
from db import db,Stock



def start(stocks):
    driver = webdriver.Chrome();
    for stock in stocks:
        url = 'http://www.iwencai.com/stockpick/search?tid=stockpick&qs=stockpick_diag&ts=1&w='
        code = stock.code;
        driver.get(url + code)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        tds = soup.select(".zcwylw_table tbody tr td")
        if len(tds)>3:
            for e in tds:
                print(e.text)
            stock.buttom = float(tds[0].text)
            stock.top = float(tds[1].text)
            stock.up = float(tds[2].text)
            stock.down = float(tds[3].text)
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