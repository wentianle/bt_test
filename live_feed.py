import backtrader as bt
import xtpwrapper as xtp 


class LiveFeed(xtp.QuoteAPI):

    def __init__(self):
        super().__init__()
        
        self.userid: str = ""
        self.password: str = ""
        self.client_id: int = 0
        self.server_ip: str = ""
        self.server_port: int = 0
        self.protocol: int = 0
        self.session_id: int = 0

        self.connect_status: bool = False
        self.login_status: bool = False

        self.sse_inited: bool = False
        self.szse_inited: bool = False

    
    def OnDisconnected(self, reason):
        """
        当客户端与行情后台通信连接断开时，该方法被调用。
        @remark api不会自动重连，当断线发生时，请用户自行选择后续操作。可以在此函数中调用Login重新登录。注意用户重新登录后，需要重新订阅行情
        :param reason: 错误原因，请与错误代码表对应
        :return:
        """
        pass

    def OnError(self, error_info):
        """
        错误应答
        @param error_info 当服务器响应发生错误时的具体的错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        @remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理
        :param error_info:
        :return:
        """
        pass

    def OnSubMarketData(self, ticker, error_info, is_last):
        """
        订阅行情应答，包括股票、指数和期权

        @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param ticker: 详细的合约订阅情况
        :param error_info: 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnUnSubMarketData(self, ticker, error_info, is_last):
        """
        退订行情应答，包括股票、指数和期权

        @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param ticker: 详细的合约取消订阅情况
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnDepthMarketData(self, market_data, bid1_qty, bid1_count, max_bid1_count, ask1_qty, ask1_count,
                          max_ask1_count):
        """
        深度行情通知，包含买一卖一队列
        @remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param market_data: 行情数据
        :param bid1_qty: 买一队列数据
        :param bid1_count: 买一队列的有效委托笔数
        :param max_bid1_count: 买一队列总委托笔数
        :param ask1_qty: 卖一队列数据
        :param ask1_count: 卖一队列的有效委托笔数
        :param max_ask1_count: 卖一队列总委托笔数
        :return:
        """
        pass

    def OnSubOrderBook(self, ticker, error_info, is_last):
        """
        订阅行情订单簿应答，包括股票、指数和期权

        @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约订阅情况
        :param error_info: 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnUnSubOrderBook(self, ticker, error_info, is_last):
        """
        退订行情订单簿应答，包括股票、指数和期权

        @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约取消订阅情况
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnOrderBook(self, order_book):
        """
        行情订单簿通知，包括股票、指数和期权

        :param order_book: 行情订单簿数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :return:
        """
        pass

    def OnSubTickByTick(self, ticker, error_info, is_last):
        """
        订阅逐笔行情应答，包括股票、指数和期权

        @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约订阅情况
        :param error_info: 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnUnSubTickByTick(self, ticker, error_info, is_last):
        """
        退订逐笔行情应答，包括股票、指数和期权

        @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约取消订阅情况
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnTickByTick(self, tbt_data):
        """
        逐笔行情通知，包括股票、指数和期权

        需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param tbt_data: 逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，
        :return:
        """
        pass

    def OnSubscribeAllMarketData(self, exchange_id, error_info):
        """
        订阅全市场的股票行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，
                            XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllMarketData(self, exchange_id, error_info):
        """
        退订全市场的股票行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllOrderBook(self, exchange_id, error_info):
        """
        订阅全市场的股票行情订单簿应答

        @remark 需要快速返回

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOrderBook(self, exchange_id, error_info):
        """
        退订全市场的股票行情订单簿应答

        @remark 需要快速返回

        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllTickByTick(self, exchange_id, error_info):
        """
        订阅全市场的股票逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllTickByTick(self, exchange_id, error_info):
        """
        退订全市场的股票逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnQueryAllTickers(self, ticker_info, error_info, is_last):
        """
        查询可交易合约的应答

        :param ticker_info: 可交易合约信息
        :param error_info: 查询可交易合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次查询可交易合约的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnQueryTickersPriceInfo(self, ticker_info, error_info, is_last):
        """
        查询合约的最新价格信息应答

        :param ticker_info: 合约的最新价格信息
        :param error_info: 查询合约的最新价格信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnSubscribeAllOptionMarketData(self, exchange_id, error_info):
        """
        订阅全市场的期权行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOptionMarketData(self, exchange_id, error_info):
        """
        退订全市场的期权行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllOptionOrderBook(self, exchange_id, error_info):
        """
        订阅全市场的期权行情订单簿应答

        @remark 需要快速返回
        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOptionOrderBook(self, exchange_id, error_info):
        """
        退订全市场的期权行情订单簿应答

        @remark 需要快速返回
        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllOptionTickByTick(self, exchange_id, error_info):
        """
        订阅全市场的期权逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOptionTickByTick(self, exchange_id, error_info):
        """
        退订全市场的期权逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass





if __name__ == '__main__':

    session_id = 0
    request_id = 1 
    test = xtp.QuoteAPI()
    
    ret = test.Login('120.27.164.138', 6002, '53191002899', '778MhWYa')
    print (ret, test.GetApiLastError())
    if ret == 0: 
        test.Logout()
        test.Release()
        print("test---", ret)
    else:
        print(test.GetApiLastError())

    # if ret == 0:

    #     test.Logout()
    #     test.Release()
    #     # test.SubscribeAllMarketData()

    #     # print(test.OnSubscribeAllMarketData())
