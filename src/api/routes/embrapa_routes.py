from fastapi import status, APIRouter
from fastapi.responses import JSONResponse, Response
from typing import Union, List
from pydantic import Field, BaseModel

from src.usecases import EmbrapaProducaoUsecase

router = APIRouter()

class EmbrapaProducaoRequest(BaseModel):
    """Classe para definir os parâmetros de consulta para a rota de produção da Embrapa."""
    ano: Union[List[int], int, None, str] = Field(
        default=1970,
        description="Ano(s) para filtrar os dados de produção. Aceita um único ano ou uma lista de anos.",
        example=[2020, 2021, 2022, '2020', '2020-2022', '2020, 2021, 2022', '1970-1975,2000,2020-2022']
    )
    download_csv: bool = Field(
        default=False,
        description="Se True, retorna os dados em formato CSV.",
        example=True
    )

# Rota GET /producao onde deverá receber o parâmetro ano na query string
@router.post('/producao')
async def get_dados_producao(request: EmbrapaProducaoRequest):
    """Busca de Informações sobre a Produção de vinhos, sucos e derivados do Rio Grande do Sul"""
    try:
        usecase = EmbrapaProducaoUsecase(request.ano)
        ress = usecase.execute()

        if ress.empty:
            return JSONResponse(content="Não há dados a serem processados", status_code=status.HTTP_200_OK) 
        
        if not request.download_csv:
            return JSONResponse(content=ress.to_dict(orient='records'), status_code=status.HTTP_200_OK)
        
        headers = {}
        headers["Content-Disposition"] = f"attachment; filename=producao.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False) 
        return Response(headers=headers, content=content, status_code=status.HTTP_200_OK)

    except Exception as ex:
        return JSONResponse(content=f'Houve um problema ao realizar a solicitação: {ex}', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)