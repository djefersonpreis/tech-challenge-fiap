from src.utils.scrape_utils import scrape_table
from typing import Union, List
import re
import pandas as pd

class EmbrapaProcessamentoUsecase():
    """
    Classe responsável por executar os processos da rota get_dados_processamento
    """
    def __init__(self, ano: Union[List[int], int, None, str]) -> None:
        self.__TAB_ID = 'opt_03'
        self.ano = ano

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações da sessão [Processamento] -> {http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03}

        returns: 
            dataset_processamento (pd.DataFrame): Dataset com as informações de Processamento
        """
        
        urls_buscas = []
        
        if isinstance(self.ano, list):
            for a in self.ano:
                urls_buscas.append([f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={self.__TAB_ID}&ano={a}', a])
        elif isinstance(self.ano, str):
            range_years = [int(a) for a in re.findall(r'\b\d{4}\b', self.ano)]
            range_years.sort()
            if isinstance(range_years, list):
                for a in range(range_years[0], range_years[-1] + 1):
                    urls_buscas.append([f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={self.__TAB_ID}&ano={a}', a])
            else:
                urls_buscas.append([f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={self.__TAB_ID}&ano={range_years}', range_years])
        else:
            urls_buscas.append([f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={self.__TAB_ID}&ano={self.ano}', self.ano])
            
        dataset_processamento = pd.DataFrame()
        for url, ano in urls_buscas:
            df = scrape_table(url, ano)
            if df is not None:
                dataset_processamento = pd.concat([dataset_processamento, df], ignore_index=True)
        
        if dataset_processamento.empty:
            raise ValueError("Não há dados a serem processados para o ano informado.")
        
        dataset_processamento = dataset_processamento.drop_duplicates().reset_index(drop=True)
        dataset_processamento['quantidade'] = dataset_processamento['quantidade'].astype(int)
        dataset_processamento = dataset_processamento.sort_values(by=['categoria', 'item']).reset_index(drop=True)
        return dataset_processamento
        
