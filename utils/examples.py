#MOVIE TABLE

movie_titles = ['The Lord of the Rings: The Fellowship of The Ring',
                'The Lord of the Rings: The Two Towers',
                'The Lord of the Rings: The Return of The King',
                'Pulp Fiction',
                'The Godfather',
                'Forrest Gump',
                'Gladiator',
                'Interstellar']

movie_directors = ['Peter Jackson', 'Peter Jackson', 'Peter Jackson',
                   'Quentin Tarantino',
                   'Francis Ford Coppola',
                   'Robert Zemeckis',
                   'Ridley Scott',
                   'Christopher Nolan']

movie_genres = ['Fantasy',
                'Fantasy',
                'Fantasy',
                'Drama',
                'Drama',
                'Comedy',
                'Action',
                'Sci-fi']

movie_release_dates = ['12-19-2001',
                       '12-19-2002',
                       '12-17-2003',
                       '10-14-1994',
                       '03-24-1972',
                       '07-06-1994',
                       '05-05-2000',
                       '11-07-2014']

movie_durations = [178, 179, 201, 154, 175, 142, 155, 169]

with open("/workspaces/movie-review/files/users.txt") as file:
    users = [line.rstrip() for line in file]

users_data = {
    'usernames': users[0:4],
    'emails': users[5:9],
    'birthdates': users[10:15]
}