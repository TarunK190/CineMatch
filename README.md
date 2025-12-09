# 🎬 CineMatch  
> **A Responsible, Genre-Based Movie Recommender with Full MLOps Pipeline**

![MLOps](https://img.shields.io/badge/MLOps-DVC%20%7C%20Docker%20%7C%20CI%20%7C%20Monitoring-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-green)
![License](https://img.shields.io/badge/License-MIT-purple)

Stuck in the endless scroll of streaming platforms? **CineMatch** cuts through the noise — delivering smart, transparent movie recommendations based on **genre similarity** and **IMDB-style ratings**, **without needing your watch history**.

Built with **real machine learning** and **production-grade MLOps**, this project demonstrates how ethical, reproducible, and deployable AI systems should be built.

https://github.com/user-attachments/assets/85e0b35d-9f3a-4f1c-b8c2-0f1a8d3e8f1a

---

## 🔍 Why CineMatch?

Most recommenders amplify popularity bias — pushing blockbusters while burying hidden gems.  
CineMatch is different:

- ✅ **Content-based**: No login or history needed (great for cold-start users)
- ✅ **Transparent**: "Recommended because it shares genres: _Action, Sci-Fi_"
- ✅ **Fair**: Controls popularity bias with a tunable rating boost (`α = 0.3`)
- ✅ **Responsible**: Audits genre representation & avoids unreliable ratings

> “Not just another script — a full-stack ML engineering artifact.”

---

## 🧠 Machine Learning Approach

CineMatch uses **classical unsupervised ML techniques**:

1. **Feature Engineering**: Parse genres → `"Action Sci-Fi Drama"`
2. **Vectorization**: `CountVectorizer` (scikit-learn) → numerical vectors
3. **Similarity Learning**: `cosine_similarity` → find genre neighbors
4. **Hybrid Ranking**:  
   `final_score = similarity + 0.3 × (vote_average / 10)`

✅ This is **real ML** — widely used in industry (e.g., early Netflix, Amazon).

---

## ⚙️ Tech Stack

| Layer          | Technology                     |
|----------------|-------------------------------|
| **ML Core**    | scikit-learn, pandas, rapidfuzz |
| **Backend**    | FastAPI                       |
| **Frontend**   | Streamlit                     |
| **MLOps**      | DVC, Docker, GitHub Actions   |
| **Deployment** | Render (API), Streamlit Cloud |

---

## 🛠️ MLOps Practices Implemented

| Practice               | How It’s Done                                  |
|------------------------|-----------------------------------------------|
| **Reproducibility**    | `requirements.txt` + Docker                   |
| **Data Versioning**    | DVC (Data Version Control)                    |
| **Testing**            | `pytest` for data & logic                     |
| **CI/CD**              | GitHub Actions runs tests on every push        |
| **Monitoring**         | API logs track failures & top queries         |
| **Ethical Auditing**   | Genre distribution analysis + bias mitigation  |
| **Deployment**         | One-click deploy to cloud                     |

---

## 🚀 Live Demo

- **Web App (UI)**: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-username-cinematch.streamlit.app)
- **API Docs**: [FastAPI Swagger](https://cinematch-api.onrender.com/docs)

> 💡 Try: `Inception`, `Parasite`, `The Matrix`

---

## 📥 How to Run Locally

### Prerequisites
- Python 3.10+
- Git

### Steps
```bash
# 1. Clone the repo
git clone https://github.com/your-username/cinematch.git
cd cinematch

# 2. Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)
# source venv/bin/activate    # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download data
# → Get tmdb_5000_movies.csv from Kaggle
# → Place in data/raw/tmdb_5000_movies.csv

# 5. Clean data
python notebooks/clean_data.py

# 6. Start API
uvicorn src.api.main:app --reload

# 7. Start Web App (in new terminal)
streamlit run app/app.py