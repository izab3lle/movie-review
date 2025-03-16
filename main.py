import pandas as pd
import sqlite3
import utils.table_creation as utils

conn = sqlite3.connect("movie_review_test.db")

# Generating data frames from examples
movies_df = utils.create_movie_table()
users_df = utils.create_user_table()
reviews_df = utils.create_review_table()


# Adding tables do the database
movies_df.to_sql(
    'movies',
    conn,
    if_exists = 'replace',
    index = False,
)

users_df.to_sql(
    'users',
    conn,
    if_exists = 'replace',
    index = False,
)

reviews_df.to_sql(
    'reviews',
    conn,
    if_exists = 'replace',
    index = False,
)

# QUERIES

# Highest rated movies
query_high_rate = """
    SELECT movies.movie_id, movies.title, reviews.rating
    FROM movies
    INNER JOIN reviews
    WHERE rating >= 4
"""

# Lowest rated movies
query_low_rate = """
    SELECT movies.movie_id, movies.title, reviews.rating
    FROM movies
    INNER JOIN reviews
    WHERE rating < 3
"""

# Users
query_all = """
    SELECT *
    FROM reviews
"""

pd.read_sql(query_high_rate, conn)
pd.read_sql(query_low_rate, conn)
pd.read_sql(query_all, conn)


conn.close()