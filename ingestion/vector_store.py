from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from config.settings import EMBEDDING_MODEL


def create_vectorstore(docs):

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return FAISS.from_documents(
        docs,
        embeddings
    )