import streamlit as st
import requests

st.title("🎬 CineMatch")
title = st.text_input("Enter a movie title:")

if title:
    try:
        resp = requests.get(f"http://localhost:8000/recommend/{title}")
        if resp.ok:
            for r in resp.json()["recommendations"]:
                st.write(f"**{r['title']}** | ⭐ {r['rating']}")
        else:
            st.error("Movie not found")
    except:
        st.error("API not running. Run: uvicorn src.api.main:app")