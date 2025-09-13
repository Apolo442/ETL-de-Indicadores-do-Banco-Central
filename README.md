# ETL de Indicadores Econômicos do Banco Central

![Python](https://img.shields.io/badge/Python-3.11-blue.svg?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.5.3-150458.svg?logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.31.0-3776AB.svg?logo=python&logoColor=white)
![Schedule](https://img.shields.io/badge/Schedule-1.2.0-lightgrey.svg?logo=clockify&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-0db7ed.svg?logo=docker&logoColor=white)


Este projeto implementa um pipeline de ETL (Extração, Transformação e Carga) para coletar diariamente indicadores econômicos da API de Dados Abertos do Banco Central do Brasil (BCB). A aplicação é containerizada com Docker para garantir portabilidade e consistência na execução.

## 📜 Funcionalidades

- **Extração (Extract):** Coleta os dados mais recentes para os indicadores SELIC, IPCA e Dólar (venda) diretamente da API do BCB.
- **Transformação (Transform):** Utiliza a biblioteca Pandas para estruturar os dados em um formato padronizado com as colunas: `nome_indicador`, `data_referencia`, `valor_indicador`.
- **Carga (Load):** Salva o DataFrame processado em um arquivo no formato CSV.
- **Agendamento:** O script é configurado para executar automaticamente todos os dias às 08:00 (horário de Brasília).
- **Containerização:** A aplicação e todas as suas dependências são empacotadas em uma imagem Docker para fácil execução em qualquer ambiente.
- **Robustez:** Inclui tratamento de erros para falhas de conexão com a API e logging para monitoramento da execução.

## 🛠️ Tecnologias Utilizadas

- `Python 3.11`
- `Pandas`
- `Requests`
- `Schedule`
- `Docker`

## 🚀 Como Executar

Para executar este projeto, você precisará ter o Git e o Docker Desktop instalados e em execução na sua máquina.

**1. Clone o repositório:**
```
git clone URL_DO_SEU_REPOSITORIO.git
cd nome-do-repositorio
```

**2. Construa a imagem Docker:**
```
docker build -t et-indicadores-bcb .
```

**3. Execute o container:***
Este comando irá iniciar o container em segundo plano. O volume (-v) garante que os arquivos CSV gerados dentro do container sejam salvos na sua pasta data local.


Para Windows (PowerShell):
```

docker run -d --name etl-indicadores -v "${pwd}\data":/app/data etl-indicadores-bcb
```

Para Linux ou macOS:
```
docker run -d --name etl-indicadores -v "$(pwd)/data":/app/data etl-indicadores-bcb
```

**4. Verifique a execução:***
O container agora está rodando e aguardando o horário agendado (08:00) para executar. Para verificar os logs e confirmar que o agendador iniciou:

```
docker logs etl-indicadores
```
O arquivo indicadores_AAAA-MM-DD.csv será gerado na pasta data/ após a primeira execução.
```
nome_indicador,data_referencia,valor_indicador
SELIC,2025-09-11,0.055131
IPCA,08/2025,0.25
DOLAR,2025-09-11,5.44
```
