# author: Munkhorgil Tumurchudur
# description: Top Movies & Reviews (CS178 ProjectOne)
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    try:
        top_movies = get_top_movies()
        return render_template('home.html', movies=top_movies)
    except Exception as e:
        return f"An error occurred: {str(e)}"



@app.route('/genres', methods=['GET'])
def genres():
    try:
        genre_id = request.args.get('genre_id')
        genres = get_genres()
        movies = []
        if genre_id:
            movies = get_movies_by_genre(genre_id)
        return render_template('genres.html', genres=genres, movies=movies, selected_genre=genre_id)
    except Exception as e:
        return f"Error: {e}"



# Movie Review in the DynamoDB


@app.route('/add-review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        movie_title = request.form['movie_title']
        username = request.form['username']
        rating = request.form['rating']
        review_text = request.form['review_text']
        create_review(movie_title, username, rating, review_text)
        flash('Review added successfully!', 'success')
        return redirect(url_for('reviews'))
    else:
        movies = get_all_movies()
        return render_template('add_review.html', movies=movies)


@app.route('/reviews')
def reviews():
    all_reviews = print_all_reviews()
    return render_template('reviews.html', reviews=all_reviews)


@app.route('/edit-review/<review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    if request.method == 'POST':
        rating = request.form['rating']
        review_text = request.form['review_text']
        update_review(review_id, rating, review_text)
        flash('Review updated!', 'success')
        return redirect(url_for('reviews'))
    else:
        review = get_review(review_id)
        return render_template('edit_review.html', review=review)


@app.route('/delete-review/<review_id>')
def remove_review(review_id):
    delete_review(review_id)
    flash('Review deleted!', 'warning')
    return redirect(url_for('reviews'))



# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)