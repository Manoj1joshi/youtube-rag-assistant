from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import CHUNK_SIZE,CHUNK_OVERLAP
from langchain_core.documents import Document

def split_text(transcript):
    parent_docs = []
    current_text = []
    start_time = None

    for item in transcript:
        if start_time is None:
            start_time = item.start
        current_text.append(item.text)
        # create parent block every ~1000 chars
        if len(" ".join(current_text)) >= 1000:
            parent_docs.append(
                Document(
                    page_content=" ".join(current_text),
                    metadata={
                        "start": start_time,
                        "end": item.start
                    }
                )
            )
            current_text = []
            start_time = None
    # last block
    if current_text:

        parent_docs.append(
            Document(
                page_content=" ".join(current_text),
                metadata={
                    "start": start_time,
                    "end": transcript[-1].start
                }
            )
        )
    splitter = RecursiveCharacterTextSplitter(
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            ", ",
            " "
        ],
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    child_docs = splitter.split_documents(
        parent_docs
    )
    return child_docs