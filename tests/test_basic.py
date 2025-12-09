from src.models.recommender import genrebasedRecommender

def test_inception():
    rec = genrebasedRecommender("data/processed/movies_clean.pkl")
    results = rec.recommend("Inception", top_k=3)
    assert "error" not in str(results)
    assert len(results) == 3
    assert all(r["rating"] >= 0 for r in results)
    print("✅ Test passed!")