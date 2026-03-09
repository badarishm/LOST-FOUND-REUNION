import streamlit as st
from search_engine import search

st.title("Lost & Found Semantic Search")

query = st.text_input("Describe your lost item")

if query:
    results = search(query)

    st.subheader("Top Matches")

    for i, item in enumerate(results["documents"][0]):
        image_path = results["metadatas"][0][i]["image"]

        st.markdown(f"### Match {i+1}")
        st.image(image_path, width=200)
        st.write(item)
