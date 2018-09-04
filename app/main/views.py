from flask import render_template , request , redirect , url_for
from . import main
from ..request import get_movies , get_movie ,search_movie

from ..models import Review
from .forms import ReviewForm



    # *** OUR VIEWS ***
'''
    First function to be called once the app fires
'''
@main.route('/')
def index():
    title = 'pythonFlask App'

    #get popular , upcoming and nowshowing movies
    popular_ones = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    nowshowing = get_movies('now_playing')

    search_movie = request.args.get('movie-query')

    if search_movie :
        return redirect(url_for('main.search_this_movie',movie_name=search_movie))
    else:
        return render_template('index.html',title = title, popular = popular_ones, upcoming = upcoming_movie , nowshowing=nowshowing)


#    ********** VIEWS FOR THE ABOUT PAGE *********** 
'''
    The about page . Rendered whenever about is added to path
'''
@main.route('/about')
def about():
    message = "von MUTINDA"
    return render_template('about.html',message = message)

@main.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = get_movie(movie_id)
    title = f'{movie.title}'

    reviews = Review.get_review(movie_id)

    return render_template('movie.html',movie=movie ,title=title ,reviews = reviews )


'''
    The page to be populated with searched movies
'''
@main.route('/search/<movie_name>')
def search_this_movie(movie_name):

    movies_list = movie_name.split(" ") 

    movie_format = "+".join(movies_list)

    title = f" Search Results for {movie_name}"

    # search_movie = request.args.get('movie-query')
    searched = search_movie(movie_format)

    return render_template('searched.html', searched = searched , title = title , search = movie_name )



'''
    there should be docstring here my friend so that your code can be understood by others .
'''
@main.route('/movie/review/new/<int:id>' , methods = ['GET' , 'POST']) 
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        new_review = Review(movie.id ,title,movie.poster,review)
        new_review.save_review()

        return redirect(url_for('.movie', movie_id = movie.id))

    title = f'{movie.title} Review'

    return render_template('new_review.html',form =form ,movie=movie)