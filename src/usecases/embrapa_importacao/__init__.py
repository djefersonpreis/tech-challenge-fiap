from src.utils.scrape_utils import scrape_table_importacao_comercializacao
from typing import Union, List
import re
import pandas as pd

class EmbrapaImportacaoUsecase():
    """
    Classe responsável por executar os processos da rota get_dados_importacao
    """
    def __init__(self, ano: Union[List[int], int, None, str]) -> None:
        self.__TAB_ID = 'opt_05'
        self.__categorias = [
            { 'id': 'subopt_01', 'nome': 'Vinhos de mesa' },
            { 'id': 'subopt_02', 'nome': 'Espumantes' },
            { 'id': 'subopt_03', 'nome': 'Uvas frescas' },
            { 'id': 'subopt_04', 'nome': 'Uvas passas' },
            { 'id': 'subopt_05', 'nome': 'Suco de uva' }
        ]
        self.ano = ano

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações da sessão [Importação] -> {http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05}

        returns: 
            dataset_importacao (pd.DataFrame): Dataset com as informações de Importação
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
            
        #
            
        dataset_importacao = pd.DataFrame()
        for url, ano in urls_buscas:
            for categoria in self.__categorias:
                url = f"{url}&subopcao={categoria['id']}"
                df = scrape_table_importacao_comercializacao(url, ano)
                if df is not None:
                    df['categoria'] = categoria['nome']
                    dataset_importacao = pd.concat([dataset_importacao, df], ignore_index=True)
        
        if dataset_importacao.empty:
            raise ValueError("Não há dados a serem processados para o ano informado.")
        
        dataset_importacao = dataset_importacao.drop_duplicates().reset_index(drop=True)
        dataset_importacao['quantidade'] = dataset_importacao['quantidade'].astype(int)
        dataset_importacao = dataset_importacao.sort_values(by=['categoria','pais']).reset_index(drop=True)
        return dataset_importacao
        
