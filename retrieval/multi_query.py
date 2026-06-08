from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


multi_query_prompt = PromptTemplate(
    template="""
Generate 4 alternative search queries
for the following user question.

Question:
{question}

Return one query per line.
""",
    input_variables=["question"]
)


def build_multi_query_generator(llm):

    chain = (
        multi_query_prompt
        | llm
        | StrOutputParser()
    )

    return chain


def parse_queries(text):

    queries = [
        q.strip()
        for q in text.split("\n")
        if q.strip()
    ]

    return queries