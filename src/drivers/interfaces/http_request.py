from typing import List, Dict
from abc import ABC, abstractmethod

class HttpRequestChartInterface(ABC):

    @abstractmethod
    def request_from_url_chart(self) -> List[Dict]:
        pass

class HttpRequestQuoteInterface(ABC):

    @abstractmethod
    def request_from_url_quote(self) -> List[Dict[str, str]]:
        pass
