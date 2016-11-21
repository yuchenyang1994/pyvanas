# -*- coding: utf-8 -*-
from xmlrpclib import ServerProxy

class VanasCli(object):

    """vanas处理"""

    def __init__(self):
        self._serv = ServerProxy("http://139.196.6.151:5555",allow_none=True)

    def get_bar(self,symbol,start_utc_time,end_utc_time):
        col_name = "ctp_{symbol}_M1".format(symbol=symbol)
        data = self._serv.get_data(col_name,start_utc_time,end_utc_time)

    def get_m5_bar(self,symbol,start_utc_time,end_utc_time):
        col_name = "ctp_{symbol}_M1_M5".format(symbol=symbol)
        data = self._serv.get_data(col_name,start_utc_time,end_utc_time)



if __name__ == '__main__':
    cli = VanasCli()
    cli.get_bar("CF701","2016-11-21 14:20","2016-11-21 14:50")



