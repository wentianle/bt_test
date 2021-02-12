import datetime
from backtrader import cerebro  # For datetime objects
import pandas as pd
import backtrader as bt
from pandas.core.frame import DataFrame
import tushare as ts
import logging

log = logging.getLogger(__name__)

class SMACross(bt.Strategy):
    params = dict(
        sma_lower=10,  # period for lower SMA
        sma_higher=50,  # period for higher SMA
    )

    def __init__(self):
        # 10日SMA计算
        sma1 = bt.ind.SMA(period=self.p.sma_lower)
        # 50日SMA计算
        sma2 = bt.ind.SMA(period=self.p.sma_higher)

        # 均线交叉, 1是上穿，-1是下穿
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        close = self.data.close[0]
        date = self.data.datetime.date(0)
        if not self.position:
            if self.crossover > 0:
                log.info("buy created at {} - {}".format(date, close))
                self.buy()

        elif self.crossover < 0:
            log.info("sell created at {} - {}".format(date, close))
            self.close()

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



if __name__ == "__main__":
    cerebro = bt.Cerebro()

    st_number = '300454.SZ'
    df = get_data(st_number)

    data = bt.feeds.PandasData(dataname=df)

    cerebro.adddata(data)

    cerebro.addstrategy(SMACross)
    cerebro.addsizer(bt.sizers.AllInSizerInt)
    cerebro.broker.set_cash(100000)

    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name="annual_returns")
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name="draw_down")
    cerebro.addanalyzer(bt.analyzers.Transactions, _name="transactions")

    results = cerebro.run()

    # 打印Analyzer结果到日志
    for result in results:

        annual_returns = result.analyzers.annual_returns.get_analysis()
        log.info("annual returns:")
        for year, ret in annual_returns.items():
            log.info("\t {} {}%, ".format(year, round(ret * 100, 2)))

        draw_down = result.analyzers.draw_down.get_analysis()
        log.info(
            "drawdown={drawdown}%, moneydown={moneydown}, drawdown len={len}, "
            "max.drawdown={max.drawdown}, max.moneydown={max.moneydown}, "
            "max.len={max.len}".format(**draw_down)
        )

        transactions = result.analyzers.transactions.get_analysis()
        log.info("transactions")

    # 运行结果绘图
    cerebro.plot()