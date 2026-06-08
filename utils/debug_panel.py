import streamlit as st


def render_debug_panel(debug_info):

    with st.sidebar:

        st.header("Retrieval Debug")

        # -----------------------
        # Original Query
        # -----------------------

        if "question" in debug_info:

            st.subheader(
                "Original Query"
            )

            st.write(
                debug_info["question"]
            )

        # -----------------------
        # Rewritten Query
        # -----------------------

        if "rewritten_query" in debug_info:

            st.subheader(
                "Rewritten Query"
            )

            st.write(
                debug_info["rewritten_query"]
            )

        # -----------------------
        # Generated Queries
        # -----------------------

        if "generated_queries" in debug_info:

            st.subheader(
                "Generated Queries"
            )

            for query in debug_info[
                "generated_queries"
            ]:

                st.write(
                    f"• {query}"
                )

        # -----------------------
        # Retrieved Documents
        # -----------------------

        if "retrieved_docs" in debug_info:

            st.subheader(
                "Retrieved Docs"
            )

            for idx, doc in enumerate(
                debug_info["retrieved_docs"]
            ):

                with st.expander(
                    f"Retrieved {idx+1}"
                ):

                    st.write(doc)

        # -----------------------
        # Reranked Documents
        # -----------------------

        if "reranked_docs" in debug_info:

            st.subheader(
                "Reranked Docs"
            )

            for idx, doc in enumerate(
                debug_info["reranked_docs"]
            ):

                with st.expander(
                    f"Reranked {idx+1}"
                ):

                    st.write(doc)