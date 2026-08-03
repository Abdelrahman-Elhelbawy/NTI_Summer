import streamlit as st
import pandas as pd

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Name", "Age", 'Accepted' ,"Flavor"])

name   = st.text_input("Name")
age    = st.slider("Age", 0, 100, 25)
agree  = st.checkbox("I accept the terms")
flavor = st.selectbox("Pick one", ["Vanilla", "Mango", "Mint"])

if st.button("Submit"):
    new_row = pd.DataFrame([{"Name": name, "Age": age, "Accepted": agree, "Flavor": flavor}])
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
    st.success("Data submitted successfully!")
st.write(st.session_state.data)