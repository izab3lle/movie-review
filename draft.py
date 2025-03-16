import pandas as pd
import sqlite3
import utils.table_creation as utils

conn = sqlite3.connect("movie_review_test.db")

query_all = """
    SELECT *
    FROM movies
    WHERE movies.release_date > "01-01-2000"
"""

# Lowest rated movies
query_low_rate = """
    SELECT movies.movie_id, movies.title, reviews.rating
    FROM movies
    INNER JOIN reviews
    WHERE rating < 3
"""

pd.read_sql(query_all, conn)


conn.close()