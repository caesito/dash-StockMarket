from typing import List, Dict
from abc import ABC, abstractmethod

class HttpRequestInterface(ABC):

    @abstractmethod
    def request_from_url_chart(self) -> List[Dict]:
        pass

    @abstractmethod
    def request_from_url_quote(self) -> List[Dict]:
        pass
