from langsmith import traceable

@traceable(name="Query Rewriter")
def trace_query_rewriter(chain, question):
    return chain.invoke(question)

@traceable(name="Multi Query Retrieval")
def trace_retrieval(retriever_fn,question,*args):
    return retriever_fn(question,*args)

@traceable(name="Reranking")
def trace_reranking(reranker,question,docs):
    return reranker(question,docs)

@traceable(name="Answer Generation")
def generate_answer(qa_chain,context,question):

    return qa_chain.invoke({
            "context": context,
            "question": question
        })