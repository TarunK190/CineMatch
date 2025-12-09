from fastapi import FastAPI, HTTPException
from src.models.recommender import genrebasedRecommender

app = FastAPI()
recommender = genrebasedRecommender("data/processed/movies_clean.pkl")

@app.get("/recommend/{title}")
def recommend(title: str, top_k: int = 10):
    if top_k < 1 or top_k > 20:
        raise HTTPException(400, "top_k must be 1-20")
    results = recommender.recommend(title, top_k)
    if "error" in results:
        raise HTTPException(404, results["error"])
    return {"recommendations": results}