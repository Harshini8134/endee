# RAG Q&A App using Endee Vector Database

## Overview
A Retrieval Augmented Generation (RAG) application that lets you ask questions over your own documents. It uses Endee as the vector database to store and retrieve document embeddings for semantic search.

## System Design
User Question → Sentence Transformer (MiniLM) → Embed Query → Search Endee → Top-K Chunks → Display Answer

## How Endee is Used
- Creates a vector index to store document embeddings
- Stores document chunks as vectors using upsert
- Retrieves semantically similar chunks using cosine similarity search

## Tech Stack
- Vector Database: Endee
- Embeddings: Sentence Transformers (all-MiniLM-L6-v2)
- UI: Streamlit
- Language: Python

## Setup Instructions
1. Clone this repository
2. Navigate to rag-app folder: `cd rag-app`
3. Create virtual environment: `python -m venv venv`
4. Activate it: `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Add your text files to `sample_docs/` folder
7. Run ingestion: `python ingest.py`
8. Launch app: `streamlit run app.py`

## Project Structure
- `endee_client.py` — Endee vector database client
- `ingest.py` — Loads and embeds documents into Endee
- `query.py` — Searches Endee and returns relevant chunks
- `app.py` — Streamlit web interface
- `sample_docs/` — Folder for input documents
