from sentence_transformers import (CrossEncoder)

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(question,docs,top_k=5):
    pairs = [(question,doc.page_content)for doc in docs]
    scores = model.predict(pairs)
    ranked = sorted(zip(scores, docs),reverse=True,key=lambda x: x[0])

    return [doc for _, doc in ranked[:top_k]]