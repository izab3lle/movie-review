import pandas as pd
import datetime
import utils.examples as ex

"""
(traduzir pra inglês)
Módulo de funções que criam os
dataframes das tabelas
"""

def create_movie_table() -> pd.DataFrame:
    movies = ex.get_movies_data()
    table = pd.DataFrame(movies)

    return table

def create_user_table() -> pd.DataFrame:
    users = ex.get_users_data()
    table = pd.DataFrame(users)

    return table

def create_review_table() -> pd.DataFrame:
    reviews = ex.get_reviews_data()
    table = pd.DataFrame(reviews)

    return table