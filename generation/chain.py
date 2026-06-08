from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda,
    RunnablePassthrough
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from generation.prompt import prompt


def format_docs(docs):

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


def build_chain(
        retriever,
        model
):

    chain = (
        RunnableParallel(
            {
                "context":
                retriever
                | RunnableLambda(format_docs),

                "question":
                RunnablePassthrough()
            }
        )
        | prompt
        | model
        | StrOutputParser()
    )

    return chain
