# Imagem Docker para preparação das dependências do projeto Python
FROM python:3.12-alpine as requirements-stage
WORKDIR /tmp

RUN pip install poetry
RUN poetry self add poetry-plugin-export
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --without-hashes -o requirements.txt

# Imagem Docker para a aplicação
FROM python:3.12-alpine AS build

WORKDIR /app
COPY --from=requirements-stage /tmp/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src
COPY ./data /app/data

ARG api_version=""
ENV API_VERSION=${api_version}
EXPOSE 5000
CMD ["python", "-m", "uvicorn", "src.api.server:app", "--host", "0.0.0.0", "--port", "5000"]
