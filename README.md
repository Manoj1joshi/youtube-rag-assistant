# YouTube RAG Assistant

A Retrieval-Augmented Generation (RAG) application that answers questions from YouTube videos using transcript-based retrieval, hybrid search, reranking, and timestamp-aware retrieval.

## Features

* Extracts transcripts directly from YouTube videos
* Splits transcripts into semantic chunks
* Stores embeddings using FAISS vector search
* Hybrid Retrieval (Pinecone + BM25)
* Query Rewriting for improved retrieval
* Cross-Encoder Reranking
* Timestamp-Aware Retrieval
* Streamlit-based user interface
* LangSmith tracing support for debugging and evaluation

## Tech Stack

* Python
* Streamlit
* LangChain
* Hugging Face
* Pinecone
* BM25
* Cross Encoder Reranking
* YouTube Transcript API
* Github

## Project Architecture

User Question
↓
Query Rewriting
↓
Hybrid Retrieval (FAISS + BM25)
↓
Cross-Encoder Reranking
↓
Context Generation
↓
LLM Response

For timestamp-based queries:

User Question
↓
Time Query Detection
↓
Timestamp Retrieval
↓
Transcript Context
↓
LLM Response

## Example Queries

* What does the speaker say about motivation?
* Summarize the key ideas discussed in the video.
* What is discussed during the second hour?
* What happens at 1:35:20?
* What are the main takeaways from the interview?

## Installation

Clone the repository:

git clone https://github.com/Manoji1joshi/youtube-rag-assistant.git

Navigate to the project folder:

cd youtube-rag-assistant

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a `.env` file:

HUGGINGFACEHUB_API_TOKEN=your_token_here

LANGCHAIN_API_KEY=your_key_here

LANGCHAIN_PROJECT=your_project_name

LANGCHAIN_TRACING_V2=True

## Run the Application

streamlit run app.py

## Future Improvements

* Multi-video knowledge base
* Video chapter detection
* Better temporal reasoning
* Transcript summarization pipeline
* Evaluation dashboard using RAGAS

## Repository Structure

├── ingestion/

├── retrieval/

├── generation/

├── evaluation/

├── utils/

├── config/

├── app.py

├── requirements.txt

└── README.md
