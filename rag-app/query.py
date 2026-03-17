from sentence_transformers import SentenceTransformer
from endee_client import search

model = SentenceTransformer("all-MiniLM-L6-v2")
INDEX = "rag-docs"

def ask(question):
    q_emb = model.encode(question).tolist()
    results = search(INDEX, q_emb, top_k=4)
    matches = results.get("matches", [])
    if not matches:
        return "No relevant information found.", []
    context = "\n\n".join([m["metadata"]["text"] for m in matches])
    answer = f"Based on the documents:\n\n{context}"
    return answer, matches

