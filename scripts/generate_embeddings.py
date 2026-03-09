import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb

df = pd.read_csv("data/scraped_products.csv")

df["search_text"] = df["name"] + " " + df["description"]

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")

embeddings = model.encode(df["search_text"].tolist())

client = chromadb.Client()

collection = client.create_collection("lost_items")

for i, row in df.iterrows():

    collection.add(
        ids=[str(i)],
        documents=[row["search_text"]],
        metadatas=[{"image": row["image"]}],
        embeddings=[embeddings[i].tolist()]
    )

print("Embeddings stored successfully")
