import pandas as pd
import datetime
#import examples
"""
(traduzir pra inglês)
Módulo de funções que criam os
dtaaframes das tabelas
"""

def create_movie_table() -> pd.DataFrame:
    """
    """
    table = pd.DataFrame({
        'movie_id': [1, 2, 3],
        'title': ['f1', 'f2', 'f3'],
        'duraction': [90, 120, 80],
        'director': ['dir1', 'dir2', 'dir3'],
        'genre': ['gen1', 'gen2', 'gen3'],
        'release_date': [
            datetime.date(2024, 12, 6),
            datetime.date(2012, 7, 20),
            datetime.date(2020, 8, 6)
        ]
    })

    return table

def create_user_table() -> pd.DataFrame:
    table = pd.DataFrame({
        'user_id':[1, 2, 3],
        'username':['user1', 'user2', 'user3'],
        'birth_date': [
            datetime.date(2002, 12, 6),
            datetime.date(1998, 7, 20),
            datetime.date(1984, 8, 6)
        ],
        'email': [
            'e1@email.com',
            'e2@email.com',
            'e3@email.com'
        ]
    })

    return table

def create_review_table() -> pd.DataFrame:
    table = pd.DataFrame({
        'user_id':[1, 2, 3],
        'username':['user1', 'user2', 'user3'],
        'birth_date': [
            datetime.date(2002, 12, 6),
            datetime.date(1998, 7, 20),
            datetime.date(1984, 8, 6)
        ],
        'email': [
            'e1@email.com',
            'e2@email.com',
            'e3@email.com'
        ]
    })
    
    return table
#Review