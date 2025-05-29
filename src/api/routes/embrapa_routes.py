from fastapi import status, APIRouter
from fastapi.responses import JSONResponse, Response

from src.usecases import EmbrapaProducaoUsecase, EmbrapaProducaoRequest
from src.usecases import EmbrapaProcessamentoUsecase, EmbrapaProcessamentoRequest
from src.usecases import EmbrapaComercializacaoUsecase, EmbrapaComercializacaoRequest

router = APIRouter()


@router.post("/producao")
async def get_dados_producao(request: EmbrapaProducaoRequest):
    """Busca de Informações sobre a Produção de vinhos, sucos e derivados do Rio Grande do Sul"""
    try:
        usecase = EmbrapaProducaoUsecase(request.ano)
        ress = usecase.execute()

        if ress.empty:
            return JSONResponse(
                content="Não há dados a serem processados",
                status_code=status.HTTP_200_OK,
            )

        if not request.download_csv:
            return JSONResponse(
                content=ress.to_dict(orient="records"), status_code=status.HTTP_200_OK
            )

        headers = {}
        headers["Content-Disposition"] = f"attachment; filename=producao.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False)
        return Response(
            headers=headers, content=content, status_code=status.HTTP_200_OK
        )

    except Exception as ex:
        return JSONResponse(
            content=f"Houve um problema ao realizar a solicitação: {ex}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.post("/processamento")
async def get_dados_processamento(request: EmbrapaProcessamentoRequest):
    """Busca de Informações sobre a Processamento de vinhos, sucos e derivados do Rio Grande do Sul"""
    try:
        usecase = EmbrapaProcessamentoUsecase(request.ano)
        ress = usecase.execute()

        if ress.empty:
            return JSONResponse(
                content="Não há dados a serem processados",
                status_code=status.HTTP_200_OK,
            )

        if not request.download_csv:
            return JSONResponse(
                content=ress.to_dict(orient="records"), status_code=status.HTTP_200_OK
            )

        headers = {}
        headers["Content-Disposition"] = f"attachment; filename=producao.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False)
        return Response(
            headers=headers, content=content, status_code=status.HTTP_200_OK
        )

    except Exception as ex:
        return JSONResponse(
            content=f"Houve um problema ao realizar a solicitação: {ex}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.post("/comercializacao")
async def get_dados_comercializacao(request: EmbrapaComercializacaoRequest):
    """Busca de Informações sobre a Comercialização de vinhos, sucos e derivados do Rio Grande do Sul"""
    try:
        usecase = EmbrapaComercializacaoUsecase(request.ano)
        ress = usecase.execute()

        if ress.empty:
            return JSONResponse(
                content="Não há dados a serem processados",
                status_code=status.HTTP_200_OK,
            )

        if not request.download_csv:
            return JSONResponse(
                content=ress.to_dict(orient="records"), status_code=status.HTTP_200_OK
            )

        headers = {}
        headers["Content-Disposition"] = f"attachment; filename=producao.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False)
        return Response(
            headers=headers, content=content, status_code=status.HTTP_200_OK
        )

    except Exception as ex:
        return JSONResponse(
            content=f"Houve um problema ao realizar a solicitação: {ex}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
