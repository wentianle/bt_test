# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime
from backtrader import cerebro  # For datetime objects
import pandas as pd
import backtrader as bt
from pandas.core.frame import DataFrame
import tushare as ts


class TestStrategy(bt.Strategy):
    def log(self, txt, dt=None, doprint=False):
        if doprint:
            dt = dt or self.datas[0].datetime.date(0)

    def __init__(self) -> None:
        super().__init__()
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.sma5 = bt.ind.SMA(period=5)
        self.sma30 = bt.ind.SMA(period=30)


def get_data(code, start_time='20100101', end_time='20210101'):

    ts.set_token('a339e517ed9b1cb97cda578c2ee8fa829ef50d13ae3623a113227777')
    pro = ts.pro_api()
    
    df  = ts.pro_bar(ts_code=code, adj='qfq', start_date=start_time, end_date=end_time)
    df.index = pd.to_datetime(df.trade_date)
    df.sort_index(ascending=True, inplace=True)
    # df = df.rename(columns={'vol', 'volume'})
    df['volume'] = df['vol']
    df['openinterest'] = 0
    df = df[['open', 'high', 'low', 'close', 'volume', 'openinterest']]
    return df 


if __name__ == '__main__':

    st_number = '300454.SZ'
    df = get_data(st_number)

    data = bt.feeds.PandasData(dataname=df)

    # print(data)

    # cerebro = bt.Cerebro()
    # # Add the Data Feed to Cerebro
    # cerebro.adddata(data)

    # cerebro.add_signal(bt.SIGNAL_LONGSHORT, MySignal, subplot=False)
    # # 这句话很有用，画图看效果
    # # cerebro.signal_accumulate(True)
    # cerebro.broker.setcash(10000.0)


