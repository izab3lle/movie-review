import pandas as pd
import datetime
import examples as ex
from examples import users_data
"""
(traduzir pra inglês)
Módulo de funções que criam os
dtaaframes das tabelas
"""


def create_movie_table() -> pd.DataFrame:
    """
    """
    table = pd.DataFrame({
        'movie_id': [1, 2, 3, 4, 5, 6, 7, 8],
        'title': ex.movie_titles,
        'running_time': ex.movie_durations,
        'director': ex.movie_directors,
        'genre': ex.movie_genres,
        'release_date': ex.movie_release_dates,
    })

    return table

def create_user_table() -> pd.DataFrame:
    table = pd.DataFrame({
        'user_id':[1, 2, 3, 4, 5],
        'username': users_data['usernames'],
        'birth_date': users_data['birthdates'],
        'email': users_data['emails']
    })

    return table

def create_review_table() -> pd.DataFrame:
    table = pd.DataFrame({
        'review_id':[1, 2, 3],
        'user_id':[1, 2, 3],
        'movie_id':[1, 1, 3],
        'comment':['ruim', 'cinema puro', 'ok medio'],
        'rating':[2, 5, 3]
    })
    
    return table
#Review