import requests
import json

def get_movies():
    initial_data = json.loads(requests.get('https://swapi.co/api/films').text)
    params = ["title", "release_date", "director", "producer", "episode_id", "url"]
    processed_data = sorted([{param : film[param] for param in params} for film in initial_data["results"]], key=lambda x: x["episode_id"])
    return processed_data

def get_movie(movie_url):
    movie_data = json.loads(requests.get(movie_url).text)

def get_names_from_url_list(character_name):
