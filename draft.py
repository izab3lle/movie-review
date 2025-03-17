import pandas as pd
import sqlite3

conn = sqlite3.connect("movie_review_test.db")

query_all = """
    SELECT *
    FROM movies
    WHERE movies.release_date > "01-01-2000"
"""

# Highest rated movies
query_high_rate = """
    SELECT movies.title, reviews.rating
    FROM movies
    INNER JOIN reviews
    WHERE rating >= 4
"""

# Lowest rated movies
query_low_rate = """
    SELECT movies.movie_id, movies.title, reviews.rating, 
    FROM movies
    INNER JOIN reviews
    WHERE rating < 3
"""

query_users_ratings = """
    SELECT users.username, review.rating, reviews.comment
    FROM users
    LEFT JOIN reviews
    ON users.user_id = reviews.user_id
    ORDER BY users.username;
"""

query_avg = """
    SELECT AVG(rating), movies.title
    FROM reviews
    LEFT JOIN movies
"""

pd.read_sql(query_users_ratings, conn)


conn.close()