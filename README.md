# Tech Challenge FIAP - API pública de consulta de dados da Vitivinicultura

**Origem dos dados:** [Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)

## Visão de Projeto

A ideia do projeto é a criação de uma API pública de consulta nos dados do site nas respectivas abas:
* [Produção](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02)
* [Processamento](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03)
* [Comercialização](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04)
* [Importação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05)
* [Exportação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06)
A API vai servir para alimentar uma base de dados que futuramente será usada para um modelo de Machine Learning.

----

### Sobre o Projeto
- O projeto foi criado utilizando o framework Python [FastAPI](https://fastapi.tiangolo.com/) no formato de API REST para busca de informações.
- Foi utilizando estrutura [Docker](https://www.docker.com/) para facilitar o processo de desenvolvimento e deploy da aplicação.
- Realizado publicação do projeto na [Render](https://render.com/) para disponibilizar seu acesso e validar seu funcionamento.

**Disponibilização do Projeto**:
- [Documentação do Projeto](https://tech-challenge-fiap-8tu4.onrender.com/redoc) contendo todas as enstruturas de entrada, retorno e explicações sobre cada end-point disponível.
- Pode-se realizar testes executando as APIs a partir [Desta documentação](https://tech-challenge-fiap-8tu4.onrender.com/docs).
- End-points da aplicação:
  - [[POST /api/producao]](https://tech-challenge-fiap-8tu4.onrender.com/docs#/Embrapa/get_dados_producao_api_producao_post) -> Busca de informações da sessão de [Produção](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02)
  - [[POST /api/processamento]](https://tech-challenge-fiap-8tu4.onrender.com/docs#/Embrapa/get_dados_processamento_api_processamento_post) -> Busca de informações da sessão de [Processamento](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03)
  - [[POST /api/comercializacao]](https://tech-challenge-fiap-8tu4.onrender.com/docs#/Embrapa/get_dados_comercializacao_api_comercializacao_post) -> Busca de informações da sessão de [Comercialização](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04)
  - [[POST /api/importacao]](https://tech-challenge-fiap-8tu4.onrender.com/docs#/Embrapa/get_dados_importacao_api_importacao_post) -> Busca de informações da sessão de [Importação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05)
  - [[POST /api/exportacao]](https://tech-challenge-fiap-8tu4.onrender.com/docs#/Embrapa/get_dados_exportacao_api_exportacao_post) -> Busca de informações da sessão de [Exportação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06)

----

### Execução do projeto (local):

**Necessário**: Aplicação Docker instalada na máquina ou via WSL.

**Etapas para Execução:**:
```shell
docker compose up --build
```

----

### Estrutura do Projeto
~~~~
├── data ---------------------- Arquivos com dados pré-processados
├── src ----------------------- Pasta Raiz do projeto
│   ├── api ------------------- Responsável por conter as definições e end-points da aplicação.
│   |   ├── routes ------------ Responsável pelos End-points da aplicação.
│   |   └── server.py --------- Responsável pelas definições e instância dos end-points da aplicação.
│   ├── usecases -------------- Contém os casos de uso da API.
│   |   ├── embrapa_* ---------
│   |   |   ├── __init__.py --- Classe de execução do respectivo UseCase, contendo o processo de tratamento e mineração dos dados
│   |   |   └── dtos.py ------- Classes de definição das entradas de dados aceitas nos respectivos end-points.
│   |   └── ... --------------- Outros casos de uso.
│   └── utils ----------------- Contém os casos de uso da API.
│       └── scrape_utils.py --- Funções genéricas comuns para mineração dos dados.
|
├── .gitignore ---------------- Arquivo de configuração do Git para ignorar arquivos específicos.
├── docker-compose.yaml ------- Arquivo Docker Compose para facilitar a execução do projeto em ambiente de desenvolvimento.
├── Dockerfile ---------------- Arquivo Dockerfile com a definição do sistema operacional e etapas para preparação e execução do projeto nos ambientes de desenvolvimento e deploy. 
├── poetry.lock --------------- Arquivo Poetry utilizado para garantir a imutabilidade das versões das dependências python no projeto.
├── pyproject.toml ------------ Arquivo de definição do projeto Poetry contendo as configurações e dependências fundamentais do projeto.
└── README.md ----------------- Documentação principal do projeto.
