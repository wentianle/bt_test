from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime
from backtrader import cerebro  # For datetime objects
import pandas as pd
import backtrader as bt
from pandas.core.frame import DataFrame
import tushare as ts
import logging


# Create a Stratey
class TestStrategy(bt.Strategy):
    
    params = (
        ('exitbars', 5),
        ('maperiod5', 5),
        ('maperiod30', 30),
        ('printlog', False),
    )

    def log(self, txt, dt=None, doprint=False):
        ''' Logging function for this strategy'''
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Add a MovingAverageSimple indicator
        self.sma5 = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.maperiod5)
        self.sma30 = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.maperiod30)
        
        # Indicators for the plotting show
        bt.indicators.ExponentialMovingAverage(self.datas[0], period=25)
        bt.indicators.WeightedMovingAverage(self.datas[0], period=25,
                                            subplot=True)
        bt.indicators.StochasticSlow(self.datas[0])
        bt.indicators.MACDHisto(self.datas[0])
        rsi = bt.indicators.RSI(self.datas[0])
        bt.indicators.SmoothedMovingAverage(rsi, period=10)
        bt.indicators.ATR(self.datas[0], plot=False)

        print("init______")


        
    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))
    
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm

            elif order.issell():
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None
    
    # def onece(self, start, end):
    #     print("onece")

    # def preonce(self, start, end):
    #     print("preonce")

    # def oncestart(self, start, end):
    #     self.onece(start, end)
    #     print("oncestart")

    # def prenext(self):
    #     print('prenext:: current period:', len(self))

    # def nextstart(self):
    #     print('nextstart:: current period:', len(self))
    #     # emulate default behavior ... call next
    #     self.next()

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])
        
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return
        
        # Check if we are in the market
        if not self.position:
            print("Buy ", self.sma5[0] < self.sma30[0], self.sma5[0] , self.sma30[0], self.broker.get_cash())
            if self.sma5[0] < self.sma30[0]:
                    # BUY, BUY, BUY!!! (with all possible default parameters)
                    self.log('BUY CREATE, %.2f' % self.dataclose[0])
                    self.buy()
        else:
            # Already in the market ... we might sell

            print("SELL", self.sma5[0] < self.sma30[0], self.sma5[0] , self.sma30[0])
            if self.sma5[0] >= self.sma30[0]:
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.close()

    def start(self):
        print('Backtesting is about to start')

    def stop(self):
        print('Backtesting is finished')
        
        
def get_data(code, start_time='20100101', end_time='20210210'):

    ts.set_token('a339e517ed9b1cb97cda578c2ee8fa829ef50d13ae3623a113227777')
    ts.pro_api()
    
    df  = ts.pro_bar(ts_code=code, adj='qfq', start_date=start_time, end_date=end_time)
    df.index = pd.to_datetime(df.trade_date)
    df.sort_index(ascending=True, inplace=True)
    df['volume'] = df['vol']
    df['openinterest'] = 0
    df = df[['open', 'high', 'low', 'close', 'volume', 'openinterest']]
    return df 


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    cerebro.addstrategy(TestStrategy, maperiod5=5, maperiod30=30)

    cerebro.broker.setcash(100000.0)
    cerebro.broker.setcommission(commission=0.0005)
    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize)
    
    data = bt.feeds.PandasData(dataname=get_data('688158.SH'))
    
    cerebro.adddata(data)

      # 添加分析对象
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = "sharpe")
    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name = "AR")
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name = "DD")
    cerebro.addanalyzer(bt.analyzers.Returns, _name = "RE")
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name = "TA")
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    results = cerebro.run(maxcpus=1)

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    print('Final Portfolio Cash: %.2f' % cerebro.broker.get_cash())

    # print("夏普比例:", results[0].analyzers.sharpe.get_analysis())
    # print("年化收益率:", results[0].analyzers.AR.get_analysis())
    # print("回撤:", results[0].analyzers.DD.get_analysis())
    # print("收益:", results[0].analyzers.RE.get_analysis())
    # print("交易统计结果:", results[0].analyzers.TA.get_analysis())

    print("夏普比例:", results[0].analyzers.sharpe.get_analysis()["sharperatio"])
    print("年化收益率:", results[0].analyzers.AR.get_analysis())
    print("最大回撤:%.2f，最大回撤周期%d" % (results[0].analyzers.DD.get_analysis().max.drawdown, results[0].analyzers.DD.get_analysis().max.len))
    print("总收益率:%.2f" % (results[0].analyzers.RE.get_analysis()["rtot"]))
    results[0].analyzers.TA.print()



    cerebro.plot()
