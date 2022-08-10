from src.stages.extract.extract_content import ExtractContent
from src.drivers.mocks.http_request_mock import MockHttpRequest
from src.stages.contracts.extract_contract import ExtractContract

def test_extract():

    extract_content=ExtractContent(MockHttpRequest('JNJ'))
    response=extract_content.extract()
    assert isinstance(response, ExtractContract)