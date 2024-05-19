from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://anonime-api.vercel.app/anime/gogoanime/top-airing')
    animes = response.json().get('results', [])
    return render_template('index.html', animes=animes)

@app.route('/search')
def search():
    query = request.args.get('q')
    page = request.args.get('page', 1)
    response = requests.get(f'https://anonime-api.vercel.app/anime/gogoanime/{query}?page={page}')
    animes = response.json().get('results', [])
    return render_template('search.html', animes=animes, query=query)

@app.route('/anime/<anime_id>')
def anime(anime_id):
    response = requests.get(f'https://anonime-api.vercel.app/anime/gogoanime/info/{anime_id}')
    anime_info = response.json()
    return render_template('anime.html', anime=anime_info)

@app.route('/watch/<episode_id>')
def watch(episode_id):
    episode_response = requests.get(f'https://anonime-api.vercel.app/anime/gogoanime/watch/{episode_id}')
    sources = episode_response.json().get('sources', [])
    response = requests.get(f'https://anonime-api.vercel.app/anime/gogoanime/info/{episode_id.split("-episode")[0]}')
    anime_info = response.json()


    return render_template('watch.html', sources=sources, anime=anime_info, episode_id=episode_id)


