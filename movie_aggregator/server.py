import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests
import asyncio
import aiohttp

load_dotenv()  # Carrega as variáveis de ambiente do .env

app = Flask(__name__)

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

async def fetch_omdb_data(title, year, session):
    # Busca dados do OMDB.
    omdb_url = f"http://www.omdbapi.com/?t={title}&y={year}&apikey={OMDB_API_KEY}"
    try:
        async with session.get(omdb_url) as response:
            response.raise_for_status()  # Lança exceção para status HTTP de erro
            data = await response.json()
            if data.get("Error"):
                return None  # Indica que não encontrou o filme
            return data
    except (aiohttp.ClientError, aiohttp.ClientResponseError) as e:
        print(f"Erro ao buscar no OMDB: {e}")
        return None


async def fetch_tmdb_reviews(title, year, session):
    # Busca reviews do TMDB (requer busca do ID do filme primeiro).
    # Primeiro, busca o ID do filme no TMDB
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}&year={year}"
    try:
        async with session.get(search_url) as response:
            response.raise_for_status()
            search_data = await response.json()
            results = search_data.get("results")
            if results:
                movie_id = results[0].get("id")  # Pega o ID do primeiro resultado
            else:
                return []  # Não encontrou o filme no TMDB
    except (aiohttp.ClientError, aiohttp.ClientResponseError) as e:
        print(f"Erro ao buscar filme no TMDB: {e}")
        return []

    # Agora busca as reviews usando o ID do filme
    if movie_id:
        reviews_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={TMDB_API_KEY}"
        try:
            async with session.get(reviews_url) as response:
                response.raise_for_status()
                reviews_data = await response.json()
                reviews = [review.get("content") for review in reviews_data.get("results", [])]
                return reviews[:3]  # Retorna no máximo 3 reviews
        except (aiohttp.ClientError, aiohttp.ClientResponseError) as e:
            print(f"Erro ao buscar reviews no TMDB: {e}")
            return []
    else:
        return []

@app.route('/movie')
async def get_movie_data():
    # Endpoint principal para buscar informações do filme.
    title = request.args.get('title')
    year = request.args.get('year', type=int)

    if not title or not year:
        return jsonify({"error": "Título e ano são obrigatórios"}), 400

    async with aiohttp.ClientSession() as session:
        omdb_task = asyncio.create_task(fetch_omdb_data(title, year, session))
        tmdb_task = asyncio.create_task(fetch_tmdb_reviews(title, year, session))

        omdb_result, tmdb_result = await asyncio.gather(omdb_task, tmdb_task)

    if not omdb_result:
        return jsonify({"error": "Filme não encontrado no OMDB"}), 404

    movie_data = {
        "titulo": omdb_result.get("Title"),
        "ano": int(omdb_result.get("Year")),
        "sinopse": omdb_result.get("Plot"),
        "reviews": tmdb_result
    }

    return jsonify(movie_data)

if __name__ == '__main__':
    app.run(debug=True)