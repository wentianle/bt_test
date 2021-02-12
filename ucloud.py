import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st_number = '300454.SZ'
first_money = 1000000

import tushare as ts
ts.set_token('a339e517ed9b1cb97cda578c2ee8fa829ef50d13ae3623a113227777')
pro = ts.pro_api()

df = pro.daily(ts_code=st_number, start_date='20100701', end_date='20210208')

df.to_csv(st_number+'.csv')

df = pd.read_csv(st_number+'.csv', index_col='trade_date', parse_dates=['trade_date'])[['open', 'close', 'low', 'high']].sort_index()

df['ma5'] = df['open'].rolling(5).mean()
df['ma30'] = df['open'].rolling(30).mean()

df = df.dropna()

# df[['open', 'ma5', 'ma30']].plot()
# plt.show()
sre1 = df['ma5'] < df['ma30']
sre2 = df['ma5'] >= df['ma30']

golden_cross = df[sre1 & sre2.shift(1)].index
death_cross = df[~(sre1 | sre2.shift(1))].index

sr1 = pd.Series(1, index = golden_cross)
sr2 = pd.Series(0, index = death_cross)
sr = sr1.append(sr2).sort_index()

money = first_money
hold = 0

for i in range(0, len(sr)) :
    price = df['open'][sr.index[i]]
    if sr.iloc[i] == 1:
        buy = (money // (price *100))   
        money -= buy * price * 100 
        hold += buy * 100
        # print(i,"   buy:", buy)
    else:
        money += hold * price
        hold = 0
    
    print(sr.index[i], hold, money, price)

current_price =df['open'][-1] 
now_money = hold * current_price + money

# if __name__ == '__main__':

# print(sr)
print('本金:',first_money,' 账户余额:',now_money , ' 盈利:',now_money-first_money, ' 当前价格:',current_price)