from src.drivers.interfaces.http_request import HttpRequestInterface
from src.stages.contract.extract_contract import ExtractContract

class ExtractQuote():

    def __init__(self, http_request_chart: HttpRequestInterface, http_request_quote: HttpRequestInterface) -> None:
        self.__http_request_chart=http_request_chart
        self.__http_request_quote=http_request_quote

    def extract(self) -> ExtractQuoteContract:

        try:
            content_chart=self.__http_request_chart.request_from_url_chart()
            content_quote=self.__http_request_quote.request_from_url_quote()
            return ExtractQuoteContract(
                chart_summary=content_chart,
                quote_summary=content_quote
            )
        except Exeption as error:
            print(error)
            