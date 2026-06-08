from langchain_core.output_parsers import StrOutputParser

from generation.prompt import prompt


def build_qa_chain(llm):

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain