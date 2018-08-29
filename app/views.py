from flask import render_template
from app import app
from .request import get_movies , get_movie ,search_movie

    # *** OUR VIEWS ***
'''
    Firts function to be called once the app fires
'''
@app.route('/')
def index():
    title = 'pythonFlask App'

    #get popular movies
    popular_ones = get_movies('popular')
    # print(popular_ones)
    upcoming_movie = get_movies('upcoming')

    return render_template('index.html',title = title, popular = popular_ones, upcoming = upcoming_movie)


'''
    The about page . Rendered whenever about is added to path
'''
@app.route('/about')
def about():
    message = "von MUTINDA"
    return render_template('about.html',message = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = get_movie(movie_id)
    title = f'{movie.title}'

    return render_template('movie.html',movie=movie ,title=title )


'''
    The page to be populated with searched movies
'''
@app.route('/search/<movie_name>')
def search_this_movie(movie_name):

    movies_list = movie_name.split(" ") 

    movie_format = "+".join(movies_list)

    searched = search_movie(movie_format)

    title = f" Search Results for {movie_name}"

    return render_template('searched.html', searched = searched , title = title )