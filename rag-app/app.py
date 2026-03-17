import streamlit as st
from query import ask

st.set_page_config(page_title="RAG App with Endee", page_icon="🔍")

st.title("RAG Q&A using Endee Vector Database")
st.caption("Ask questions about your documents — powered by Endee")

st.markdown("---")

question = st.text_input("Enter your question:", placeholder="What is machine learning?")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching Endee vector database..."):
            answer, sources = ask(question)
        st.markdown("### Answer")
        st.success(answer)
        if sources:
            st.markdown("### Sources")
            for s in sources:
                st.info(f"Source: {s['metadata']['source']}\n\n{s['metadata']['text'][:200]}...")

st.markdown("---")
st.caption("Built with Endee Vector DB + Sentence Transformers")
