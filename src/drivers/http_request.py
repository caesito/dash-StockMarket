from typing import List, Dict 
from .header_request import HeaderRequests
import requests

class HttpRequestChart(HeaderRequests):

    def __init__(self,tickers: List[str]) -> None:
        self.__url_chart='https://query1.finance.yahoo.com/v8/finance/chart/'
        self.tickers=tickers

    def request_from_url_chart(self) -> List[Dict]:

        response_chart=[]
        for ticker in self.tickers:
            url_chart ='{}{}'.format(self.url_chart, ticker)
            response= requests.get(url_chart, headers=super().header, data=super().payload_chart).json()
            response_chart.append(response)
            
        return response_chart

class HttpRequestQuotes(HeaderRequests):

    def __init__(self, tickers: List[str]) -> None:
        self.__url_name='https://query1.finance.yahoo.com/v1/finance/quoteType/?symbol='
        self.__url_info='https://query1.finance.yahoo.com/v10/finance/quoteSummary/'
        self.__parameter='?modules=assetProfile%2CsecFilings'
        self.tickers=tickers

    def request_from_url_quote(self) -> List[Dict[str, str]]:

        response_tickers= []
        for ticker in self.tickers:
            url_name='{}{}'.format(self.__url_name, ticker) 
            url_info='{}{}{}'.format(self.__url_info, ticker, self.__parameter)

            response_name=requests.get(url_name,headers=super().header, data=super().payload_name).json()
            response_info=requests.get(url_info,headers=super().header, data=super().payload).json()

            result={
                'name': response_name,
                'info': response_info
            }
            response_tickers.append(result)

        return response_tickers
