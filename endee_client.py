import json
import os
import numpy as np

DATA_FILE = "endee_store.json"

def create_index(name, dim=384):
    if not os.path.exists(DATA_FILE):
        json.dump({}, open(DATA_FILE, "w"))
    print(f"Index '{name}' ready.")

def upsert(index, vectors):
    try:
        store = json.load(open(DATA_FILE))
    except:
        store = {}
    store[index] = store.get(index, [])
    store[index].extend(vectors)
    json.dump(store, open(DATA_FILE, "w"))
    print(f"Stored {len(vectors)} vectors.")

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def search(index, query_vec, top_k=4):
    try:
        store = json.load(open(DATA_FILE))
    except:
        return {"matches": []}
    vectors = store.get(index, [])
    scored = []
    for v in vectors:
        score = cosine_similarity(query_vec, v["values"])
        scored.append((score, v))
    scored.sort(reverse=True, key=lambda x: x[0])
    matches = [v for _, v in scored[:top_k]]
    return {"matches": matches}
