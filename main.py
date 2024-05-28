from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load movies data
with open('data/movies.json', 'r') as f:
    movies = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    liked_movie_title = request.json['title']
    liked_movie = next((movie for movie in movies if movie['title'].lower() == liked_movie_title.lower()), None)
    
    if liked_movie:
        liked_genres = set(liked_movie['genre'])
        recommended_movies = [
            movie for movie in movies
            if movie['id'] != liked_movie['id'] and liked_genres.intersection(movie['genre'])
        ]
    else:
        recommended_movies = []

    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
