from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Answer only from context.

If answer is unavailable,
say "I don't know."

Context:
{context}

Question:
{question}
""",
    input_variables=[
        "context",
        "question"
    ]
)
