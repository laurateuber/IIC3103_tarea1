import requests
import json

def get_movies():
    initial_data = json.loads(requests.get('https://swapi.co/api/films').text)
    params = ["title", "release_date", "director", "producer", "episode_id", "url"]
    processed_data = sorted([{param : film[param] for param in params} for film in initial_data["results"]], key=lambda x: x["episode_id"])
    return processed_data

def get_movie(movie_url):
    url = 'https://swapi.co/api/films/{0}'.format(movie_url)
    initial_data = json.loads(requests.get(url).text)
    params = ["title", "release_date", "director", "producer", "episode_id", "url",
    "opening_crawl", "created", "edited"]
    obj_params = ["characters", "planets", "starships"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data.update({param : get_info_from_urls(initial_data[param])for param in obj_params})
    return processed_data

def get_character(character_url_id):
    url = 'https://swapi.co/api/people/{0}'.format(character_url_id)
    initial_data = json.loads(requests.get(url).text)
    params = ["name", "height", "mass", "hair_color", "skin_color", "eye_color",
    "birth_year", "gender", "created", "edited"]
    obj_params = ["films", "starships"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data.update({param : get_info_from_urls(initial_data[param])for param in obj_params})
    processed_data.update({"homeworld" : get_info_from_urls([initial_data["homeworld"]])})
    return processed_data

def get_planet(planet_url_id):
    url = 'https://swapi.co/api/planets/{0}'.format(planet_url_id)
    initial_data = json.loads(requests.get(url).text)
    params = ["name", "rotation_period", "orbital_period", "diameter", "climate", "gravity",
    "terrain", "surface_water", "population", "created", "edited"]
    obj_params = ["films", "residents"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data.update({param : get_info_from_urls(initial_data[param])for param in obj_params})
    return processed_data

def get_starship(starship_url_id):
    url = 'https://swapi.co/api/starships/{0}'.format(starship_url_id)
    initial_data = json.loads(requests.get(url).text)
    params = ["name", "model", "manufacturer", "cost_in_credits", "length", "max_atmosphering_speed",
    "crew", "passengers", "cargo_capacity", "consumables", "created", "edited", "hyperdrive_rating",
    "MGLT", "starship_class"]
    obj_params = ["films", "pilots"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data.update({param : get_info_from_urls(initial_data[param])for param in obj_params})
    return processed_data

def get_info_from_urls(url_list):
    processed_data = []
    for url in url_list:
        par_name = "name"
        initial_data = json.loads(requests.get(url).text)
        lista = url.split("/")
        if "planet" in lista:
            print("entrooo")
        if "films" in lista:
            par_name = "title"
        url_id = url.strip().split('/')[-2]
        processed_data.append({"url_id": url_id, par_name : initial_data[par_name]})
    return processed_data
