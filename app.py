import streamlit as st

from retrieval.multi_retriever import retrieve_documents
from utils.helper import get_video_id
from ingestion.transcript_loader import get_transcript
from ingestion.splitter import split_text
from ingestion.vector_store import create_vectorstore
from retrieval.retriever import get_retriever
from generation.llm import load_llm
from generation.qa_chain import build_qa_chain
from retrieval.query_rewriter import build_query_rewriter
from retrieval.reranker import rerank_documents
from retrieval.bm25_retriever import create_bm25_retriever
from retrieval.time_router import detect_time_query
from retrieval.time_retriever import retrieve_by_time
from utils.debug_panel import render_debug_panel
from evaluation.tracing import trace_query_rewriter,trace_retrieval,trace_reranking, generate_answer
st.title("Youtube RAG")


video_input = st.text_input(
    "Youtube URL"
)

question = st.text_input(
    "Question"
)




if st.button("Generate"):

    video_id = get_video_id(
        video_input
    )

    transcript = get_transcript(
        video_id
    )
    debug_info = {}
    debug_info["question"] = question
    docs = split_text(transcript)
    vectorstore = create_vectorstore(docs)

    retriever = get_retriever(
        vectorstore
    )

    bm25_retriever = create_bm25_retriever(docs)

    llm = load_llm()
    qa_chain = build_qa_chain(llm)

    target_time = detect_time_query(question)

    if target_time is not None:

        rewritten_question = question

        docs = retrieve_by_time(target_time,docs)

    else:

        query_rewriter = build_query_rewriter(llm)

        rewritten_question = trace_query_rewriter(query_rewriter, question)

        debug_info["rewritten_query"] = rewritten_question

        retrieved_docs, queries = trace_retrieval(
            retrieve_documents,
            rewritten_question,
            query_rewriter,
            retriever,
            bm25_retriever,
            llm
        )

        debug_info["generated_queries"] = queries
        docs = trace_reranking(
            rerank_documents,
            question,
            retrieved_docs,
        )
        debug_info["retrieved_docs"] = [
            doc.page_content[:300]
            for doc in retrieved_docs
        ]
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )
    answer = generate_answer(qa_chain, context, question)
    
    st.write(answer)
    render_debug_panel(debug_info)
    st.subheader("Sources")
    for doc in docs:

        start = int(
            doc.metadata["start"]
        )

        minutes = start // 60

        seconds = start % 60

        timestamp = (
            f"{minutes:02}:{seconds:02}"
        )

        youtube_link = (
            f"https://www.youtube.com/watch?v={video_id}&t={start}s"
        )

        st.markdown(
            f"[{timestamp}]({youtube_link})"
        )

        st.write(
            doc.page_content[:300] + "..."
        )
