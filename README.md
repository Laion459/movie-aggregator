# Serviço Agregador de Dados de Filmes

Este projeto implementa um serviço que busca informações de filmes de duas APIs públicas (OMDB e TMDB) e as agrega em uma única resposta.

## Funcionalidades

*   Busca informações de filmes (título, ano, sinopse, reviews) das APIs OMDB e TMDB.
*   Exibe os dados formatados no terminal.
*   Permite ao usuário inserir o título e o ano do filme manualmente.
*   Oferece uma lista predefinida de filmes para facilitar os testes.
*   Permite repetir a consulta com os mesmos dados.
*   Interface de menu interativa no terminal.

## Requisitos

*   Python 3.7+
*   Bibliotecas listadas em `requirements.txt`
*   Chaves de API válidas para OMDB e TMDB

## Instalação

1.  Clone o repositório:

    ```bash
    git clone https://github.com/Laion459/movie-aggregator
    cd movie_aggregator
    ```

2.  Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:

    ```
    OMDB_API_KEY=sua_chave_omdb
    TMDB_API_KEY=sua_chave_tmdb
    ```

    **Importante:** As chaves de API são confidenciais e não devem ser compartilhadas publicamente.

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    pip install aiohttp  # Para requisições assíncronas
    pip install "flask[async]"  # Para suporte a async no Flask
    pip install python-dotenv # Para carregar variáveis de ambiente
    ```

## Execução

1.  Inicie o servidor:

    ```bash
    python server.py
    ```

    O servidor Flask será iniciado e estará disponível em `http://127.0.0.1:5000`.

2.  Inicie o cliente em outro terminal:

    ```bash
    python client.py
    ```

    O cliente exibirá um menu interativo no terminal.
    ![image](https://github.com/user-attachments/assets/eecf2075-6146-4b8b-96a4-113572ed3b9a)


## Uso

1.  **Inserir nome e ano manualmente:**

    *   Digite `1` e pressione Enter.
    *   Digite o título do filme e pressione Enter.
    *   Digite o ano do filme e pressione Enter.
  
    ![image](https://github.com/user-attachments/assets/c105d982-e73e-4e8b-8379-bff9d41e9cfa)


2.  **Escolher um filme da lista:**

    *   Digite `2` e pressione Enter.
    *   Digite o número do filme na lista e pressione Enter.
    ![image](https://github.com/user-attachments/assets/9a8be2e3-5019-46d3-906d-270bf856529a)


3.  **Nova consulta com os mesmos dados:**

    *   Digite `3` e pressione Enter.
    *   Esta opção repetirá a consulta com o último filme pesquisado.

4.  **Sair:**

    *   Digite `4` e pressione Enter.

## Estrutura do Projeto
![image](https://github.com/user-attachments/assets/a26a5d27-c54c-4009-942d-4bde44011b39)

    movie_aggregator/
        ├── client.py               # Código do cliente (interface de linha de comando)
        ├── server.py               # Código do servidor (API Flask)
        ├── .env                    # Arquivo com as chaves de API
        ├── requirements.txt        # Lista de dependências do projeto
        ├── .gitignore              # Lista de ignora arquivos do projeto
        ├── example.env             # Arquivo para exemplo de chaves de cada API
    ├── LICENSE                     # License Apache 2.0
    └── README.md                   # Este arquivo


## Notas

*   O servidor roda por padrão na porta 5000.
*   O cliente envia requisições para o servidor local na porta 5000.
*   O arquivo `.env` deve conter suas chaves de API para OMDB e TMDB.
*   Certifique-se de ter o Python e o `pip` instalados corretamente.

## Licença

Este projeto está licenciado sob a Apache License, Version 2.0.
