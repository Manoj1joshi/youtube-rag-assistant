import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
from pathlib import Path


HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2") == "True"


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 4
