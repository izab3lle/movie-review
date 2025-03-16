#MOVIE TABLE
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  

users_path = os.path.join(BASE_DIR, "files", "users.txt")
movies_path = os.path.join(BASE_DIR, "files", "movies.txt")
reviews_path = os.path.join(BASE_DIR, "files", "reviews.txt")

def to_date_array(array) -> list:
    array = [
        datetime.strptime(date , '%m-%d-%Y') \
        for date in array
    ]

    return array

def to_int_array(array) -> list:
    array = [int(interger) for interger in array]

    return array

# EXAMPLE DICTIONARIES

def get_users_data() -> dict:
    with open(users_path, "r") as file:
        users = [line.rstrip() for line in file]

    users_data = {
        'user_id': list(range(1, 6)),
        'username': users[0:5],
        'email': users[5:10],
        'birthdate':  users[10:15]
    }

    users_data['birthdate'] = to_date_array(users_data['birthdate'])

    return users_data


def get_movies_data() -> dict:
    with open(movies_path, "r") as file:
        movies = [line.rstrip() for line in file]
    
    movies_data = {
        'movie_id': list(range(1, 9)),
        'title': movies[0:8],
        'director': movies[8:16],
        'genre': movies[16:24],
        'release_date': movies[24:32],
        'runtime': movies[32:40],
    }

    movies_data['release_date'] = to_date_array(movies_data['release_date'])
    movies_data['runtime'] = to_int_array(movies_data['runtime'])

    return movies_data

def get_reviews_data() -> dict:
    with open(reviews_path, "r") as file:
        reviews = [line.rstrip() for line in file]
    
    reviews_data = {
        'review_id':list(range(1, 21)),
        'user_id':[1, 1, 1, 1, 1, 1,
                   2, 2, 2,
                   3, 3, 3, 3, 3, 3,
                   5, 5, 5, 5, 5],
        'movie_id':[1, 4, 5, 6, 7, 8,
                    1, 2, 3,
                    1, 2, 5, 6, 7, 8,
                    1, 4, 6, 7, 8],
        'comment': reviews,
        'rating':[3.9, 4.5, 4, 3.2, 4, 5,
                  5, 4.8, 5,
                  2, 3.7, 1, 1.5, 2, 1,
                  4, 4, 3.9, 5, 4]
    }

    return reviews_data
