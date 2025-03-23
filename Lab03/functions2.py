import random
import itertools
import math

# Dictionary of movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Task 1: Check if a movie's IMDB score is above 5.5
def is_high_rated(movie):
    return movie["imdb"] > 5.5

# Task 2: Get list of high-rated movies
def high_rated_movies(movie_list):
    return [movie for movie in movie_list if is_high_rated(movie)]

# Task 3: Get movies by category
def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"].lower() == category.lower()]

# Task 4: Compute average IMDB score
def average_imdb(movie_list):
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list) if movie_list else 0

# Task 5: Compute average IMDB score for a category
def average_imdb_by_category(movie_list, category):
    category_movies = movies_by_category(movie_list, category)
    return average_imdb(category_movies)

# Task 6: Import and use functions
if __name__ == "__main__":
    print(is_high_rated(movies[0]))  # Check if the first movie is high rated
    print(high_rated_movies(movies))  # List of high-rated movies
    print(movies_by_category(movies, "Romance"))  # List of Romance movies
    print(average_imdb(movies))  # Average IMDB score of all movies
    print(average_imdb_by_category(movies, "Romance"))  # Average IMDB score of Romance movies
