import pandas as pd


movies = []

with open('movies.txt', 'r') as fs:
    for line in fs.readlines():
        line = line.strip()
        movie_name = line[:-6].rstrip()
        year = line[-6:].lstrip("(").rstrip(")")
        movies.append({
            "name": movie_name,
            "year": year
        })

frame = pd.DataFrame.from_dict(movies)

frame.to_csv("movies.csv")
