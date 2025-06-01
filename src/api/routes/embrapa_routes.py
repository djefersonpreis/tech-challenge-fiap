from fastapi import status, APIRouter
from fastapi.responses import JSONResponse, Response

from src.usecases import EmbrapaProducaoUsecase, EmbrapaProducaoRequest
from src.usecases import EmbrapaProcessamentoUsecase, EmbrapaProcessamentoRequest
from src.usecases import EmbrapaComercializacaoUsecase, EmbrapaComercializacaoRequest
from src.usecases import EmbrapaImportacaoUsecase, EmbrapaImportacaoRequest
from src.usecases import EmbrapaExportacaoUsecase, EmbrapaExportacaoRequest

router = APIRouter()


@router.post("/producao")
async def busca_dados_producao(request: EmbrapaProducaoRequest):
    """
    Busca de Informações sobre a Produção de vinhos, sucos e derivados do Rio Grande do Sul
    Origem das informações: [Produção](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02)
    
    Dados retornados:
    - categoria: Categoria do produto (Vinho de Mesa, Suco, Derivados, etc.);
    - item: Nome do produto (Tinto, Seco, Suco de Uva, etc.);
    - quantidade: Quantidade produzida (em litros);
    - ano: Ano de produção.
    """
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
async def busca_dados_processamento(request: EmbrapaProcessamentoRequest):
    """
    Busca de Informações sobre a Processamento de vinhos, sucos e derivados do Rio Grande do Sul
    Origem das informações: [Processamento](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03)
    
    Dados retornados:
    - classificacao: Classificação do produto (Viníferas, Americanas e Híbridas, Uvas de mesa ou Sem Classificação);
    - categoria: Categoria do produto (Tintas, Brancas, Brancas e Rosadas, etc.);
    - item: Nome da uva (Cardinal, Primitivo, Malvasia, etc.);
    - quantidade: Quantidade processada (em Kilogramas);
    - ano: Ano de processamento.
    """
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
        headers["Content-Disposition"] = f"attachment; filename=processamento.csv"
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
async def busca_dados_comercializacao(request: EmbrapaComercializacaoRequest):
    """
    Busca de Informações sobre a Comercialização de vinhos, sucos e derivados do Rio Grande do Sul
    Origem das informações: [Comercialização](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04)
    
    Dados retornados:
    - categoria: Categoria do produto (Vindo de Mesa, Espumantes, Suco de Uvas, etc.);
    - item: Nome do produto (Tinto, Branco, Rosé, etc.);
    - quantidade: Quantidade processada (em Litros);
    - ano: Ano de processamento.
    """
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
        headers["Content-Disposition"] = f"attachment; filename=comercializacao.csv"
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


@router.post("/importacao")
async def busca_dados_importacao(request: EmbrapaImportacaoRequest):
    """
    Busca de Informações sobre a Importação de vinhos, sucos e derivados do Rio Grande do Sul
    Origem das informações: [Importação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05)
    
    Dados retornados:
    - categoria: Categoria do produto (Vinhos de mesa, Espumantes, Uvas frescas, Uvas passas ou Suco de uva);
    - pais: País de origem do produto;
    - quantidade: Quantidade importada (em Kilogramas);
    - valor: Valor da importação (em Dólares Americanos);
    - ano: Ano de importação.
    """
    try:
        usecase = EmbrapaImportacaoUsecase(request.ano)
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
        headers["Content-Disposition"] = f"attachment; filename=importacao.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False)
        return Response(
            headers=headers, content=content, status_code=status.HTTP_200_OK
        )

    except Exception as ex:
        import traceback; traceback.print_exc();
        return JSONResponse(
            content=f"Houve um problema ao realizar a solicitação: {ex}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.post("/exportacao")
async def busca_dados_exportacao(request: EmbrapaExportacaoRequest):
    """
    Busca de Informações sobre a Exportação de vinhos, sucos e derivados do Rio Grande do Sul
    Origem das informações: [Exportação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06)
    
    Dados retornados:
    - categoria: Categoria do produto (Vinhos de mesa, Espumantes, Uvas frescas ou Suco de uva);
    - pais: País de destino da exportação;
    - quantidade: Quantidade exportada (em Kilogramas);
    - valor: Valor da exportação (em Dólares Americanos);
    - ano: Ano de importação.
    """
    try:
        usecase = EmbrapaExportacaoUsecase(request.ano)
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
        headers["Content-Disposition"] = f"attachment; filename=exportacao.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False)
        return Response(
            headers=headers, content=content, status_code=status.HTTP_200_OK
        )

    except Exception as ex:
        import traceback; traceback.print_exc();
        return JSONResponse(
            content=f"Houve um problema ao realizar a solicitação: {ex}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )