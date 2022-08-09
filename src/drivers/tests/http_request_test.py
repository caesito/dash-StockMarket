from src.drivers.http_request import HttpRequestChart, HttpRequestQuotes
from src.drivers.mocks.http_request_mock import MockHttpRequestChart, MockHttpRequestQuotes


def test_request_from_url_chart():

    #request_chart=HttpRequestChart(['JNJ'])
    #response_content=request_chart.request_from_url_chart()
    
    request_chart=MockHttpRequestChart(['JNJ'])
    response_content=request_chart.mock_request_from_url_chart()
    
    assert isinstance(response_content, list)
    assert isinstance(response_content[0], dict)

 
def test_request_from_url_quote():

    #request_quote=HttpRequestQuote(['JNJ'])
    #response_content=request_quote.request_from_url_quote()

    request_quote=MockHttpRequestQuotes(['JNJ'])
    response_content=request_quote.mock_request_from_url_quote()

    assert isinstance(response_content, list)
    assert isinstance(response_content[0], dict)