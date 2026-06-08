def hybrid_retrieve(
    question,
    vector_retriever,
    bm25_retriever
):

    vector_docs = vector_retriever.invoke(
        question
    )

    bm25_docs = bm25_retriever.invoke(
        question
    )

    docs = []

    seen = set()

    for doc in vector_docs + bm25_docs:

        key = (
            doc.page_content,
            doc.metadata["start"]
        )

        if key not in seen:

            seen.add(key)

            docs.append(doc)

    return docs