import requests
from django.conf import settings


def get_films():
    """
    Get all movies from ghibli API
    :return:
    """
    films_url = settings.GHIBLI_API_ROOT_ENDPOINT + "films"
    films = requests.get(films_url)
    return films


def get_people():
    """
    Get all characters from ghibli API
    :return:
    """
    people_url = settings.GHIBLI_API_ROOT_ENDPOINT + "people"
    people = requests.get(people_url)
    return people


def update_people_in_films(films, people):
    """
    Correct people field of each film. Each film has film url and each people have films url list that he/she appeared
    Given all films and people as parameter, find people who appeared in film by comparing film url
    :param films:
    :param people:
    :return:
    """
    _films = []
    for film in films:
        people_in_film = []
        for character in people:
            if film["url"] in character["films"]:
                people_in_film.append(character["url"])

        film["people"] = people_in_film
        _films.append(film)

    return _films
