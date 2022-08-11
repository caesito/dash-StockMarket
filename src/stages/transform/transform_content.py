from src.stages.contracts.transform_contract import  TransformContract
from src.stages.contracts.extract_contract import ExtractContract
from datetime import datetime

class TransformContent:

    def __init__(self, extract_contract: ExtractContract) -> None:
        self.__extract_contract=extract_contract
        self.__quote=extract_contract.quote_summary
        self.__chart=extract_contract.chart_summary

    def transform(self) -> TransformContract:
        
        try:
            chart_result=self.__transform_chart()
            quote_result=self.__transform_info_ticker()
            return TransformContract(
                chart_result=chart_result,
                quote_result=quote_result
            )
        except Exception as error:
            print(error)
    
    def __transform_info_ticker(self):
        result_info_ticker=[]
       
        for ticker in range(len(self.__quote)):
            result={
                'Nome completo da empresa': self.__transform_name(),
                'Informacoes': self.__transform_quotes()
            }
            result_info_ticker.append(result)

        return result_info_ticker

    def __transform_name(self):
        for content in self.__quote:
            name=[{'name': name['longName']} for name in content['name']['quoteType']['result']]
        return name[0]['name']

    def __transform_quotes(self):
        info=[]
        
        for content in self.__quote:
            for result in content['info']['quoteSummary']['result']:
                    data = {
                        'Endereco': {
                            'Rua': result['assetProfile']['address1'],
                            'Cidade': result['assetProfile']['city'],
                            'Estado': result['assetProfile']['state'],
                            'Endereco postal': result['assetProfile']['zip'],
                            'Pais': result['assetProfile']['country']
                        },
                        'Telefone': result['assetProfile']['phone'],
                        'Setor': result['assetProfile']['sector'],
                        'Industria': result['assetProfile']['industry'],
                        'Numero_de_funcionarios': result['assetProfile']['fullTimeEmployees'],
                        'Executivos': [{'Cargo':compoff['title'],'Nome':compoff['name']} for compoff in result['assetProfile']['companyOfficers'] ]
                    }
                    info.append(data)

        return info
    
    def __transform_chart(self):
        result=[]
        entries = []
       
        for ticker in range(len(self.__quote)):
            data=self.__get_timestamp(self.__chart)
            entrie = {
                'Ticker': self.__get_ticker(self.__chart),
                'adjclose': self.__get_adjclose(self.__chart),
                'volume': self.__get_volume(self.__chart),
            }
            entries.append(entrie)

        result.append(entries)
        result.append(data)
        return result
   
    def __get_volume(self,payload):
        volume = []

        for content in payload:
            for result in content['chart']['result']:
                for quote in result['indicators']['quote']:
                    for quantidade in quote['volume']:
                        volume.append(quantidade)
      
        return volume
   
    def __get_adjclose(self,payload):
        adjclose_list = []
        
        for content in payload:
            for result in content['chart']['result']:
                for quote in result['indicators']['quote']:
                    for item in quote['close']:
                        adjclose_list.append(item)
    
        return adjclose_list
   
    def __get_ticker(self,payload):
        ticker = ''
        for content in payload:
            for result in content['chart']['result']:
                ticker = result['meta']['symbol']
                
        return ticker
   
    def __timestemp_to_date(self, data):
        dt=datetime.fromtimestamp(data).strftime('%Y-%m-%d %H:%M:%S')
        return dt
    
    def __get_timestamp(self,payload):
        timestamp_list = []
        for content in payload:
            for result in content['chart']['result']:
                for timestamp in result['timestamp']:
                    time=self.__timestemp_to_date(timestamp)
                    timestamp_list.append(time)

        return {
            'Date':timestamp_list
        }
