from src.drivers.http_request import HttpRequest
from src.drivers.mocks.http_request_mock import MockHttpRequest


def test_request_from_url_chart():

    #request_chart=HttpRequest(['JNJ'])
    #response_content=request_chart.request_from_url_chart()
    
    request_chart=MockHttpRequest(['JNJ'])
    response_content=request_chart.mock_request_from_url_chart()
    
    assert isinstance(response_content, list)
    assert isinstance(response_content[0], dict)

 
def test_request_from_url_quote():

    #request_quote=HttpRequest(['JNJ'])
    #response_content=request_quote.request_from_url_quote()

    request_quote=MockHttpRequest(['JNJ'])
    response_content=request_quote.mock_request_from_url_quote()

    assert isinstance(response_content, list)
    assert isinstance(response_content[0], dict)
    