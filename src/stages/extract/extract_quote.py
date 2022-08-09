from src.drivers.interfaces.http_request import HttpRequestQuoteInterface
from src.stages.contract.extract_quote_contract import ExtractQuoteContract

class ExtractQuote():

    def __init__(self, http_request: HttpRequestQuoteInterface) -> None:
        self.__http_request=http_request

    def extract(self) -> ExtractQuoteContract:

        try:
            content_quote=self.__http_request.request_from_url_quote()
            return ExtractQuoteContract(
                quote_summary=content_quote
            )
        except Exeption as error:
            print(error)
            