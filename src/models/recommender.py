import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process

class genrebasedRecommender:
    def __init__(self, data_path: str, rating_weight: float = 0.3):
        self.df=pd.read_pickle(data_path)
        self.rating_weight=rating_weight

        self.df['genres_clean']=self.df['genres_clean'].fillna("")

        vectorizer= CountVectorizer(tokenizer=lambda x:x.split(" "))

        genre_matrix= vectorizer.fit_transform(self.df['genres_clean'])

        self.similarity_matrix = cosine_similarity(genre_matrix)

        self.titles_lower=self.df['title_lower'].tolist()


    def recommend(self, title: str, top_k: int = 10):
        # Fuzzy match title
        match = process.extractOne(title.lower().strip(), self.titles_lower)
        if not match or match[1] < 80:
            return {"error": "Movie not found"}
        
        idx = self.titles_lower.index(match[0])
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_k+1]

        results = []
        for i, sim in sim_scores:
            row = self.df.iloc[i]
            final_score = sim + self.rating_weight * (row["vote_average"] / 10.0)
            results.append({
                "title": row["title"],
                "genres": row["genres_clean"],
                "rating": round(row["vote_average"], 1),
                "score": round(final_score, 3)
            })
        return sorted(results, key=lambda x: x["score"], reverse=True)

       