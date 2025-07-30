# generate_group_embeddings.py
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/section_dict.pkl", "rb") as f:
    section_dict = pickle.load(f)

titles = list(section_dict.keys())
texts = list(section_dict.values())

embeddings = model.encode(texts)

np.save("data/grouped_embeddings.npy", embeddings)

with open("data/grouped_titles.pkl", "wb") as f:
    pickle.dump(titles, f)

with open("data/grouped_texts.pkl", "wb") as f:
    pickle.dump(texts, f)

print("✅ Saved embeddings for all grouped sections.")
