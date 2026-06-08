from retrieval.hybrid_retriever import (
    hybrid_retrieve
)

from retrieval.multi_query import (
    build_multi_query_generator,
    parse_queries
)


def retrieve_documents(
        question,
        query_rewriter,
        vector_retriever,
        bm25_retriever,
        llm
):

    rewritten_question = (
        query_rewriter.invoke(question)
    )

    generator = (
        build_multi_query_generator(llm)
    )

    generated = generator.invoke(
        rewritten_question
    )

    queries = parse_queries(
        generated
    )

    queries.append(
        rewritten_question
    )

    all_docs = []

    seen = set()

    for query in queries:

        docs = hybrid_retrieve(
            query,
            vector_retriever,
            bm25_retriever
        )

        for doc in docs:

            if doc.page_content not in seen:

                seen.add(
                    doc.page_content
                )

                all_docs.append(doc)

    return all_docs, queries