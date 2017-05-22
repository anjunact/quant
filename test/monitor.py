import tushare as ts
import pandas as pd

stocks = ['002158','002342','600717','600803','601000']
buy_prices = [21.05,10.03,13.75,13.85,5.85]
df = ts.get_realtime_quotes(stocks) #Single stock symbol
rs = df[['code','name','price','bid','ask','volume','amount','time']]
print(rs)
df2 = pd.DataFrame({'code':stocks,'buy_price':buy_prices})
df1 =df[['code','name','price']]
alldf = pd.merge(df1,df2,on='code')
print(alldf)

s1 = pd.Series(df['price'].astype(float).values,index=df['code'])
s2 = pd.Series(buy_prices,index=df['code'])
s3 = (s1-s2)/s2
print(s3*100)
print (s1-s2)
