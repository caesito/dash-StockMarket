from src.drivers.interfaces.http_request import HttpRequestChartInterface
from src.stages.contracts.extract_chart_contract import ExtractChartContract

class ExtractChart():

    def __init__(self, http_request: HttpRequestChartInterface) -> None:
        self.__http_request=http_request
    
    def extract(self) -> ExtractChartContract:

        try:
            content_chart=self.__http_request.request_from_url_chart()
            return ExtractChartContract(
                chart_summary=content_chart
            )
        except Exeption as error:
            print(error)
            