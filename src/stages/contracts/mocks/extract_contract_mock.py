from src.stages.contracts.extract_contract import ExtractContract
from src.drivers.mocks.http_request_mock import MockHttpRequest

summary=MockHttpRequest(['JNJ'])

extract_contract_mock=ExtractContract(
    chart_summary=summary.request_from_url_chart(),
    quote_summary=summary.request_from_url_quote()
)
