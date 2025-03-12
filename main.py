import pandas as pd
import sqlite3
import utils.table_creation as utils

conn = sqlite3.connect("movie_review.db")

#movies_df = utils.create_movie_table()
#users_df = utils.create_user_table()
reviews_df = utils.create_review_table()

reviews_df.to_sql(
    'reviews',
    conn,
    if_exists = 'replace',
    index = False,
)

query = """
    SELECT *
    FROM reviews
    WHERE rating > 2
"""

query_all = """
    SELECT *
    FROM reviews
"""

pd.read_sql(query_all, conn)


