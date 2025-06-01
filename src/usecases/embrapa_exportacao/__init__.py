import logging
from src.utils.scrape_utils import scrape_table_importacao_exportacao
from typing import Union, List
import re
import pandas as pd

class EmbrapaExportacaoUsecase():
    """
    Classe responsável por executar os processos da rota get_dados_exportacao
    """
    def __init__(self, ano: Union[List[int], int, None, str]) -> None:
        self.__TAB_ID = 'opt_06'
        self.__categorias = [
            { 'id': 'subopt_01', 'nome': 'Vinhos de mesa' },
            { 'id': 'subopt_02', 'nome': 'Espumantes' },
            { 'id': 'subopt_03', 'nome': 'Uvas frescas' },
            { 'id': 'subopt_04', 'nome': 'Suco de uva' }
        ]
        self.ano = ano

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações da sessão [Exportacao] -> {http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_6}

        returns: 
            dataset_exportacao (pd.DataFrame): Dataset com as informações de Exportacao
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
            
        dataset_exportacao = pd.DataFrame()
        try:
            for url, ano in urls_buscas:
                if ano >= 1970 and ano <= 2024:
                    for categoria in self.__categorias:
                        url = f"{url}&subopcao={categoria['id']}"
                        df = scrape_table_importacao_exportacao(url, ano)
                        if df is not None:
                            df['categoria'] = categoria['nome']
                            dataset_exportacao = pd.concat([dataset_exportacao, df], ignore_index=True)
                            
        except Exception as e:
            logging.error(f"Erro ao processar os dados de exportação: {e}")
            logging.info("Buscando informações em dados processados anteriormente...")
            df = pd.read_csv('/app/data/exportacao.csv')
            dataset_exportacao = df[df['ano'].isin([ano for _, ano in urls_buscas])]
        
        if dataset_exportacao.empty:
            raise ValueError("Não há dados a serem processados para o ano informado.")
        
        dataset_exportacao = dataset_exportacao.drop_duplicates().reset_index(drop=True)
        dataset_exportacao['quantidade'] = dataset_exportacao['quantidade'].astype(int)
        dataset_exportacao = dataset_exportacao.sort_values(by=['categoria','pais']).reset_index(drop=True)
        return dataset_exportacao
        
