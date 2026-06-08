from config.settings import TOP_K

def get_retriever(vectorstore):

    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": TOP_K,
            "fetch_k": TOP_K * 4,
            "lambda_mult": 0.5}
    )