from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace
)

from config.settings import (
    HF_TOKEN,
    LLM_MODEL
)


def load_llm():

    llm = HuggingFaceEndpoint(
        repo_id=LLM_MODEL,
        task="text-generation",
        huggingfacehub_api_token=HF_TOKEN
    )

    return ChatHuggingFace(
        llm=llm
    )