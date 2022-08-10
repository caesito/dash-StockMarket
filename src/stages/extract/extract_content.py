from src.drivers.interfaces.http_request import HttpRequestInterface
from src.stages.contracts.extract_contract import ExtractContract

class ExtractContent:

    def __init__(self, http_request: HttpRequestInterface) -> None:
        self.__http_request=http_request

    def extract(self) -> ExtractContract:

        try:
            content_chart=self.__http_request.request_from_url_chart()
            content_quote=self.__http_request.request_from_url_quote()
            return ExtractContract(
                chart_summary=content_chart,
                quote_summary=content_quote
            )
        except Exception as error:
            print(error)
            