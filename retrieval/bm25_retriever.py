from langchain_community.retrievers import BM25Retriever


def create_bm25_retriever(docs):

    retriever = BM25Retriever.from_documents(
        docs
    )

    retriever.k = 10

    return retriever