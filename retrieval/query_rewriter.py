from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


rewrite_prompt = PromptTemplate(
    template="""
You are a search query optimizer.

Rewrite the user's question into a concise search query
that would retrieve relevant information.

Question:
{question}

Search Query:
""",
    input_variables=["question"]
)


def build_query_rewriter(llm):

    chain = (
        rewrite_prompt
        | llm
        | StrOutputParser()
    )

    return chain