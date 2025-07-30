# import os
# import pickle
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# from groq import Groq
# import faiss
# import numpy as np

# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# groq_client = Groq(api_key=GROQ_API_KEY)

# # Load structured section dictionary
# with open("data/section_dict.pkl", "rb") as f:
#     section_dict = pickle.load(f)

# titles = list(section_dict.keys())

# # Optional: fallback FAISS if title not matched
# model = SentenceTransformer("all-MiniLM-L6-v2")
# title_embeddings = model.encode(titles)
# faiss_index = faiss.IndexFlatL2(title_embeddings.shape[1])
# faiss_index.add(np.array(title_embeddings))

# # def generate_answer(query):
# #     # Check for exact title match
# #     if query in section_dict:
# #         return f"**{query}**\n\n{section_dict[query]}"

# #     # Fallback: semantic search
# #     query_vec = model.encode([query])
# #     D, I = faiss_index.search(np.array(query_vec), 1)
# #     best_match = titles[I[0][0]]
# #     return f"**{best_match}**\n\n{section_dict[best_match]}"





# def highlight_qa(text: str) -> str:
#     lines = text.strip().split("\n")
#     output = []
#     for line in lines:
#         if "Question:" in line:
#             q = line.split("Question:")[-1].strip()
#             output.append(f"**🟨 Question:** {q}")
#         elif "Answer:" in line:
#             a = line.split("Answer:")[-1].strip()
#             output.append(f"**🟩 Answer:** {a}")
#         else:
#             output.append(line.strip())
#     return "\n\n".join(output)





# def generate_answer(query):
#     # Check for exact title match
#     if query in section_dict:
#         raw = section_dict[query]
#         formatted = highlight_qa(raw)
#         return f"**{query}**\n\n{formatted}"

#     # Fallback: semantic search
#     query_vec = model.encode([query])
#     D, I = faiss_index.search(np.array(query_vec), 1)
#     best_match = titles[I[0][0]]
#     raw = section_dict[best_match]
#     formatted = highlight_qa(raw)
#     return f"**{best_match}**\n\n{formatted}"







import os
import pickle
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -------------------- Load Setup --------------------

load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load structured section dictionary
with open("data/section_dict.pkl", "rb") as f:
    section_dict = pickle.load(f)

titles = list(section_dict.keys())
title_embeddings = model.encode(titles)

faiss_index = faiss.IndexFlatL2(title_embeddings.shape[1])
faiss_index.add(np.array(title_embeddings))


# -------------------- Format Q&A --------------------

import re

def highlight_qa(text: str) -> str:
    lines = text.strip().split("\n")
    output = []

    for line in lines:
        line = line.strip()
        if re.search(r"\bQuestion[:：\-]", line, re.IGNORECASE):
            q = re.split(r"Question[:：\-]", line, 1)[-1].strip()
            output.append(f"🟨 **Question:** {q}")
        elif re.search(r"\bAnswer[:：\-]", line, re.IGNORECASE):
            a = re.split(r"Answer[:：\-]", line, 1)[-1].strip()
            output.append(f"🟩 **Answer:** {a}")
        else:
            output.append(line)

    return "\n\n".join(output)


# -------------------- Main Answer Function --------------------

def generate_answer(query):
    # Exact match
    if query in section_dict:
        raw = section_dict[query]
        formatted = highlight_qa(raw)
        return f"### 📘 {query}\n\n{formatted}"

    # Semantic fallback
    query_vec = model.encode([query])
    D, I = faiss_index.search(np.array(query_vec), 1)
    best_match = titles[I[0][0]]
    raw = section_dict[best_match]
    formatted = highlight_qa(raw)
    return f"### 📘 {best_match}\n\n{formatted}"
