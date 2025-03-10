import pandas as pd
import sqlite3
import utils.table_creation as utils

conn = sqlite3.connect("movie_review.db")

#movies_df = utils.create_movie_table()
users_df = utils.create_user_table()

"""
movies_df.to_sql(
    'movies',
    conn,
    if_exists = 'replace',
    index = False,
)
"""

users_df.to_sql(
    'users',
    conn,
    if_exists = 'replace',
    index = False,
)

query = """
    SELECT *
    FROM movies
    WHERE release_date > "2012-07-20"
"""

query_users = """
    SELECT *
    FROM users
"""

pd.read_sql(query, conn)


