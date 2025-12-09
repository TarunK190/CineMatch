import pandas as pd
import ast
import os

df = pd.read_csv('data/raw/tmdb_5000_movies.csv')

def parse_genres(x):
    try:
        genres= ast.literal_eval(x)
        return " ".join([g["name"] for g in genres])

    except:
        return ""

df['genres_clean']=df['genres'].apply(parse_genres)

df=df[df['vote_count']>=50 ]

df=df[['title','genres_clean','vote_average']].dropna()

df=df.drop_duplicates('title')

df['title_lower']=df['title'].str.lower().str.strip()

os.makedirs('data/processed',exist_ok=True)
df.to_pickle('data/processed/movies_clean.pkl')

print(f'Cleaned {len(df)} movies and saved to data/processed/movies_cleal.pkl')