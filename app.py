import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.schema.output_parser import StrOutputParser
from langchain_classic.schema.runnable import RunnablePassthrough

from src.load_doc import load_resumes
from src.vector_store import create_vector_store
from src.prompts import load_tempate
from src.load_llm import load_llm

# ---------------------------------------------------
# Page config
# ---------------------------------------------------
st.set_page_config(
    page_title="Resume Analyzer Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer – AI Chatbot")
st.caption("Ask questions about uploaded candidate resumes")

# ---------------------------------------------------
# Load environment variables
# ---------------------------------------------------
load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

# ---------------------------------------------------
# Cache RAG pipeline (runs only once)
# ---------------------------------------------------
@st.cache_resource(show_spinner=True)
def load_rag_chain():
    with st.spinner("🔄 Loading resumes and building RAG pipeline..."):
        docs = load_resumes(
            r"C:\Users\hp\Desktop\MLops\LLMOPS_RESUME_CHATBOT\LLMOPS_CHATBOT\data\resumes"
        )

        vector_store = create_vector_store(docs)
        retriever = vector_store.as_retriever()

        template = load_tempate()
        prompt = ChatPromptTemplate.from_template(template)

        llm = load_llm(API_KEY)
        output_parser = StrOutputParser()

        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | output_parser
        )

        return rag_chain


rag_chain = load_rag_chain()

# ---------------------------------------------------
# Chat session state
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello 👋 I can analyze resumes and answer questions about candidates. Ask me anything!"
        }
    ]

# ---------------------------------------------------
# Display chat history
# ---------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------------------------
# Chat input
# ---------------------------------------------------
user_query = st.chat_input("Ask about skills, experience, education, best candidate, etc...")

if user_query:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Analyzing resumes..."):
            response = rag_chain.invoke(user_query)
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
