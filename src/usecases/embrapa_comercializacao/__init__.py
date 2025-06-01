import logging
from src.utils.scrape_utils import scrape_table
from typing import Union, List
import re
import pandas as pd

class EmbrapaComercializacaoUsecase():
    """
    Classe responsável por executar os processos da rota get_dados_comercializacao
    """
    def __init__(self, ano: Union[List[int], int, None, str]) -> None:
        self.__TAB_ID = 'opt_04'
        self.ano = ano

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações da sessão [Comercialização] -> {http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04}

        returns: 
            dataset_comercializacao (pd.DataFrame): Dataset com as informações de Comercialização
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
            
        dataset_comercializacao = pd.DataFrame()
        try: 
            for url, ano in urls_buscas:
                if ano >= 1970 and ano <= 2024:
                    df = scrape_table(url, ano)
                    if df is not None:
                        dataset_comercializacao = pd.concat([dataset_comercializacao, df], ignore_index=True)
                            
        except Exception as e:
            logging.error(f"Erro ao processar os dados de Comercialização: {e}")
            logging.info("Buscando informações em dados processados anteriormente...")
            df = pd.read_csv('/app/data/comercializacao.csv')
            dataset_comercializacao = df[df['ano'].isin([ano for _, ano in urls_buscas])]
        
        if dataset_comercializacao.empty:
            raise ValueError("Não há dados a serem processados para o ano informado.")
        
        dataset_comercializacao = dataset_comercializacao.drop_duplicates().reset_index(drop=True)
        dataset_comercializacao['quantidade'] = dataset_comercializacao['quantidade'].astype(int)
        dataset_comercializacao = dataset_comercializacao.sort_values(by=['categoria', 'item']).reset_index(drop=True)
        return dataset_comercializacao
        
