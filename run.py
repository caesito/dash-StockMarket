from src.stages.transform.transform_content import TransformContent
from src.stages.contracts.mocks.extract_contract_mock import extract_contract_mock

mock = extract_contract_mock

teste=TransformContent(mock)
print(teste.transform())
