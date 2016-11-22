# -*- coding: utf-8 -*-
from xmlrpclib import ServerProxy
from pandas import DataFrame


class VanasCli(object):

    """vanas处理"""

    def __init__(self):
        self._serv = ServerProxy("http://139.196.6.151:5555",allow_none=True)

    def get_bar(self,symbol,start_utc_time,end_utc_time):
        col_name = "ctp_{symbol}_M1".format(symbol=symbol)
        bar_list = self._serv.get_data(col_name,start_utc_time,end_utc_time)
        df = self._create_df(bar_list)
        return df







    def get_m5_bar(self,symbol,start_utc_time,end_utc_time):
        col_name = "ctp_{symbol}_M1_M5".format(symbol=symbol)
        bar_list = self._serv.get_data(col_name,start_utc_time,end_utc_time)
        df = self._create_df(bar_list)
        return df


    def _create_df(self,bar_list):
        columns=['count','last_time','voloum','close','open','high','low']
        index = []
        count = []
        last_time = []
        voloum = []
        close = []
        open = []
        high = []
        low = []
        for bar in bar_list:
            for k,v in bar.items():
                if k == 'high_price':
                    high.append(v)
                elif k == 'end_utc_time':
                    last_time.append(v)
                elif k == 'count':
                    count.append(v)
                elif k == 'volume':
                    voloum.append(v)
                elif k == 'low_price':
                    low.append(v)
                elif k == 'close':
                    close.append(v)
                elif k == 'open':
                    open.append(v)
                elif k == 'start_utc_time':
                    index.append(str(v))
        data = {
            'count':count,
            'last_time':last_time,
            'voloum':voloum,
            'close':close,
            'open':open,
            'high':high,
            'low':low
        }
        df = DataFrame(data,index=index,columns=columns)
        return df





if __name__ == '__main__':
    cli = VanasCli()
    cli.get_bar("CF701","2016-11-21 14:20","2016-11-21 14:50")



