#  Lost & Found Reunion – Multi-Modal Semantic Search

This project implements a **multi-modal semantic search engine for lost items**.  
It allows users to search for lost products using natural language descriptions and retrieves the most similar items based on **semantic similarity of text embeddings**.

The system combines **web scraping, embeddings, vector search, and AI models** to find the most relevant matches.

---

#  Project Overview

The system works in the following pipeline:

1. **Web Scraping**
   - Product data and images are collected from an e-commerce website.
   - The scraped data includes:
     - Product name
     - Product description
     - Product image

2. **Dataset Creation**
   - The scraped data is stored in a CSV file.

3. **Embedding Generation**
   - Product descriptions are converted into **vector embeddings** using a Sentence Transformer model.

4. **Vector Database**
   - The embeddings are stored in a **vector database (ChromaDB)**.

5. **Semantic Search**
   - When a user enters a query describing a lost item, the system:
     - Converts the query into an embedding
     - Compares it with stored embeddings
     - Retrieves the most similar items

6. **Search Results**
   - The system returns the **top matching products with images and descriptions**.

---

# Technologies Used

- Python
- Sentence Transformers
- ChromaDB
- Pandas
- BeautifulSoup (Web Scraping)
- Requests
- Streamlit (optional UI)

---

# Project Structure
│
├── data
│ └── scraped_products.csv
│
├── images
│ └── product images
│
├── scrape_products.py
├── generate_embeddings.py
├── search_engine.py
├── app.py
├── requirements.txt
└── README.md
