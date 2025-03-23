import requests  # Biblioteca para fazer requisições HTTP
import os  # Biblioteca para interagir com o sistema operacional
from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente do arquivo .env

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lista de filmes predefinidos para facilitar os testes
FILMES_PARA_TESTE = [
    {"titulo": "The Matrix", "ano": 1999},
    {"titulo": "The Fast and the Furious", "ano": 2001},
    {"titulo": "Guardians of the Galaxy Vol. 2", "ano": 2017},
    {"titulo": "Spider-Man: Into the Spider-Verse", "ano": 2018},
    {"titulo": "Parasite", "ano": 2019},
    {"titulo": "Tenet", "ano": 2020},
    {"titulo": "Dune", "ano": 2021},
    {"titulo": "Everything Everywhere All at Once", "ano": 2022},
    {"titulo": "Oppenheimer", "ano": 2023},
    {"titulo": "Barbie", "ano": 2023},
    {"titulo": "Inception", "ano": 2010},
    {"titulo": "Interstellar", "ano": 2014},
    {"titulo": "The Shawshank Redemption", "ano": 1994},
    {"titulo": "The Dark Knight", "ano": 2008},
    {"titulo": "Pulp Fiction", "ano": 1994},
    {"titulo": "Forrest Gump", "ano": 1994},
    {"titulo": "Fight Club", "ano": 1999},
    {"titulo": "The Lord of the Rings: The Fellowship of the Ring", "ano": 2001},
    {"titulo": "The Godfather", "ano": 1972},
    {"titulo": "Back to the Future", "ano": 1985}
]

def get_movie_data(title, year):
    """
    Envia uma requisição para o servidor e retorna os dados do filme.

    Args:
        title (str): Título do filme.
        year (int): Ano do filme.

    Returns:
        dict: Dicionário com os dados do filme, ou None em caso de erro.
    """
    url = f"http://127.0.0.1:5000/movie?title={title}&year={year}"  # URL do servidor Flask
    try:
        response = requests.get(url)  # Faz a requisição GET
        response.raise_for_status()  # Lança uma exceção em caso de erro HTTP (status >= 400)
        return response.json()  # Converte a resposta JSON em um dicionário Python
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")  # Imprime o erro
        return None  # Retorna None em caso de erro

def show_data(movie_title, movie_data):
    """
    Formata e exibe os dados do filme no terminal.

    Args:
        movie_title (str): Título do filme.
        movie_data (dict): Dicionário com os dados do filme.
    """
    print(f"\n{'#' * 100}")  # Imprime uma linha separadora
    print(f" - {movie_title.upper()}")  # Imprime o título do filme em maiúsculas
    print(f"{'#' * 100}")  # Imprime outra linha separadora

    if movie_data:  # Verifica se os dados do filme foram obtidos com sucesso
        print(f"Título: {movie_data['titulo']}")  # Imprime o título
        print(f"Ano: {movie_data['ano']}")  # Imprime o ano
        print(f"Sinopse: {movie_data['sinopse']}")  # Imprime a sinopse

        print("\nReviews:")  # Imprime o cabeçalho das reviews
        if movie_data['reviews']:  # Verifica se há reviews
            for indice, review in enumerate(movie_data['reviews']):  # Itera sobre as reviews
                print(f"  {indice + 1}. {review[:200]}...")  # Imprime o número da review e os primeiros 200 caracteres
                print("  " + "_" * 100)  # Imprime uma linha separadora
        else:
            print("  Nenhuma review encontrada.")  # Imprime uma mensagem se não houver reviews

    else:
        print("Não foi possível obter os dados do filme.")  # Imprime uma mensagem de erro

    print(f"{'#' * 100}\n")  # Imprime uma linha separadora

def get_user_choice():
    """
    Exibe o menu e retorna a escolha do usuário.

    Returns:
        str: A escolha do usuário (1, 2, 3 ou 4).
    """
    print("\nMENU:")  # Imprime o cabeçalho do menu
    print("1 - Inserir nome e ano manualmente")  # Imprime a opção 1
    print("2 - Escolher um filme da lista")  # Imprime a opção 2
    print("3 - Nova consulta com os mesmos dados")  # Imprime a opção 3
    print("4 - Sair")  # Imprime a opção 4

    while True:  # Loop para garantir que o usuário digite uma opção válida
        choice = input("Escolha uma opção: ")  # Solicita a escolha do usuário
        if choice in ["1", "2", "3", "4"]:  # Verifica se a escolha é válida
            return choice  # Retorna a escolha
        else:
            print("Opção inválida. Tente novamente.")  # Imprime uma mensagem de erro

def choose_movie_from_list():
    """
    Exibe a lista de filmes e permite que o usuário escolha um.

    Returns:
        dict: Um dicionário com o título e o ano do filme escolhido.
    """
    print("\nLista de Filmes para Teste:")  # Imprime o cabeçalho da lista de filmes
    for indice, filme in enumerate(FILMES_PARA_TESTE):  # Itera sobre a lista de filmes
        print(f"{indice + 1}. {filme['titulo']} ({filme['ano']})")  # Imprime o número, título e ano do filme

    while True:  # Loop para garantir que o usuário digite uma opção válida
        try:
            choice = int(input("Escolha o número do filme: "))  # Solicita o número do filme
            if 1 <= choice <= len(FILMES_PARA_TESTE):  # Verifica se o número é válido
                return FILMES_PARA_TESTE[choice - 1]  # Retorna o filme escolhido
            else:
                print("Número inválido. Tente novamente.")  # Imprime uma mensagem de erro
        except ValueError:
            print("Entrada inválida. Digite um número.")  # Imprime uma mensagem de erro

if __name__ == '__main__':
    """
    Função principal que executa o loop do menu e interage com o usuário.
    """
    movie_title = None  # Variável para armazenar o título do filme
    movie_year = None  # Variável para armazenar o ano do filme

    while True:  # Loop principal do programa
        choice = get_user_choice()  # Obtém a escolha do usuário

        if choice == "1":  # Se o usuário escolher inserir o nome e o ano manualmente
            movie_title = input("Digite o título do filme: ")  # Solicita o título do filme
            while True:  # Loop para garantir que o usuário digite um ano válido
                try:
                    movie_year = int(input("Digite o ano do filme: "))  # Solicita o ano do filme
                    break  # Sai do loop se o ano for válido
                except ValueError:
                    print("Ano inválido. Digite um número.")  # Imprime uma mensagem de erro

        elif choice == "2":  # Se o usuário escolher um filme da lista
            filme_escolhido = choose_movie_from_list()  # Obtém o filme escolhido da lista
            movie_title = filme_escolhido['titulo']  # Define o título do filme
            movie_year = filme_escolhido['ano']  # Define o ano do filme

        elif choice == "3":  # Se o usuário escolher repetir a consulta com os mesmos dados
            if movie_title is None or movie_year is None:  # Verifica se um filme foi consultado anteriormente
                print("Nenhum filme consultado anteriormente.")  # Imprime uma mensagem se nenhum filme foi consultado
                continue  # Volta para o início do loop

        elif choice == "4":  # Se o usuário escolher sair
            print("Saindo...")  # Imprime uma mensagem de saída
            break  # Sai do loop

        if movie_title and movie_year:  # Se o título e o ano do filme foram definidos
            movie_data = get_movie_data(movie_title, movie_year)  # Obtém os dados do filme
            show_data(movie_title, movie_data)  # Exibe os dados do filme