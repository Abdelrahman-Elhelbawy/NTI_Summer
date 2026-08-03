import streamlit as st
import pandas as pd
import requests

API = "http://127.0.0.1:8000"

session = requests.Session()
session.trust_env = False          

name   = st.text_input("Name")
age    = st.slider("Age", 0, 100, 25)
agree  = st.checkbox("I accept the terms")
flavor = st.selectbox("Pick one", ["Vanilla", "Mango", "Mint"])

if st.button("Submit"):
    r = session.post(f"{API}/submit",
                     json={"name": name, "age": age, "agree": agree, "flavor": flavor})
    st.success(f"Saved! {r.json()['stored']} total")

try:
    rows = session.get(f"{API}/submissions").json()
    st.dataframe(pd.DataFrame(rows))
except requests.exceptions.ConnectionError:
    st.warning("API isn't running — start it with uvicorn first.")