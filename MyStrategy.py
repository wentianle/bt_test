from backtrader import indicators as btind
import backtrader as bt
class MyStrategy(bt.Strategy):
    params = dict(period1=20, period2=25, period3=10, period4=100)

    def __init__(self):

        sma1 = btind.SimpleMovingAverage(self.datas[0], period=self.p.period1)

        # This 2nd Moving Average operates using sma1 as "data"
        sma2 = btind.SimpleMovingAverage(sma1, period=self.p.period2)

        # New data created via arithmetic operation
        something = sma2 - sma1 + self.data.close

        # This 3rd Moving Average operates using something  as "data"
        sma3 = btind.SimpleMovingAverage(something, period=self.p.period3)

        # Comparison operators work too ...
        greater = sma3 > sma1

        # Pointless Moving Average of True/False values but valid
        # This 4th Moving Average operates using greater  as "data"
        sma3 = btind.SimpleMovingAverage(greater, period=self.p.period4)
