from fastapi import FastAPI

from .routes import router
import os

app = FastAPI(
    title="API para disponibilização de dados da Vitivinicultura Embrapa - Desafio Tech Challenge FIAP",
    description="A API realiza o processo de Scrapping dos dados de vitivinicultura do site da Embrapa, e disponibiliza as mesmas para consulta. Dividindo em informações de Produção, Processamento, Comercialização, Importação e Exportação.",
    version=os.getenv("API_VERSION", "") or "undefined",
)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
