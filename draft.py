import pandas as pd
import sqlite3
import utils.table_creation as utils

conn = sqlite3.connect("movie_review.db")


query_all = """
    SELECT *
    FROM movies
    WHERE movies.release_date > "01-01-2000"
"""

# Highest rating for movies
query_high_rate = """
    SELECT movies.title, reviews.rating
    FROM movies
    INNER JOIN reviews
    ON movies.movie_id = reviews.movie_id
    WHERE rating >= 4
"""
pd.read_sql(query_high_rate, conn)

# Lowest rating for movies
query_low_rate = """
    SELECT movies.title, reviews.rating
    FROM movies
    INNER JOIN reviews
    ON movies.movie_id = reviews.movie_id
    WHERE rating < 3
"""
pd.read_sql(query_low_rate, conn)

query_users_ratings = """
    SELECT users.username, reviews.rating, reviews.comment
    FROM users
    LEFT JOIN reviews
    ON users.user_id = reviews.user_id
    ORDER BY users.username
"""
pd.read_sql(query_users_ratings, conn)

query_avg = """
    SELECT AVG(rating), movies.title
    FROM reviews
    LEFT JOIN movies
"""

pd.read_sql(query_all, conn)

conn.close()