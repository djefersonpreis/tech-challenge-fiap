from typing import Union, List
from pydantic import Field, BaseModel


class EmbrapaProcessamentoRequest(BaseModel):
    """Classe para definir os parâmetros de consulta para a rota de Processamento da Embrapa."""

    ano: Union[List[int], int, None, str] = Field(
        default=1970,
        description="Ano(s) para filtrar os dados de Processamento. Aceita um único ano ou uma lista de anos.",
        example=[
            2020,
            2021,
            2022,
            "2020",
            "2020-2022",
            "2020, 2021, 2022",
            "1970-1975,2000,2020-2022",
        ],
    )
    download_csv: bool = Field(
        default=False,
        description="Se True, retorna os dados em formato CSV. Caso contrário, retorna os dados em formato JSON.",
        example=True,
    )
