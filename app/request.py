from app import app
import urllib.request , json
from .models import movie

# api_key = app.config[]
api_key = 'd06d2ddbf8bcece8cb4d618c139b2bcf'

Movie = movie.Movie

base_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

def get_movies(category):
    
    movie_url = base_url.format(category,api_key)
    # movie_url = base_url+category+api_key

    with urllib.request.urlopen(movie_url) as url:
        movie_data = url.read()
        movie_response = json.loads(movie_data)

        movie_results = None

        if movie_response['results']:
            movie_list = movie_response['results']
            movie_results = process_results(movie_list)

    return movie_results

def process_results(movie_response):
    movie_results = []

    for movie_item in movie_response:
        ide = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(ide,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results



def get_movie(id):
    details_url = base_url.format(id,api_key)

    # get_movie_data = None

    with urllib.request.urlopen(details_url) as url:
        movie_data = url.read()
        movie_response = json.loads(movie_data)

        movie_object = None

        if movie_response :
            title = movie_response.get('title') 
            ide = movie_response.get("id")
            overview = movie_response.get('overview')
            poster = movie_response.get('poster_path')
            vote_average = movie_response.get('vote_average')
            vote_count = movie_response.get('vote_count')

            movie_object = Movie(ide,title,overview,poster,vote_average,vote_count)

    return movie_object