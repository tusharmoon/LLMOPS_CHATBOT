📄 Resume Analyzer – RAG-Based AI Chatbot

Resume Analyzer is an intelligent, Retrieval-Augmented Generation (RAG) based chatbot designed to analyze and interact with multiple resumes using natural language. The application enables recruiters, hiring managers, and analysts to ask contextual questions about candidate profiles and receive accurate, resume-grounded responses in a conversational format.

The system processes resumes (PDF/DOCX), converts them into semantic embeddings, and stores them in a vector database for efficient similarity search. When a user asks a question, the chatbot retrieves the most relevant resume chunks and leverages a Large Language Model (LLM) to generate precise, explainable answers strictly based on the retrieved content.

The application features a chat-style Streamlit frontend, offering a seamless user experience similar to modern AI assistants, while the backend is built using LangChain, Mistral LLM, and vector search techniques.

🚀 Key Features

        💬 Chatbot Interface – Interactive, conversational UI built with Streamlit

        📂 Multi-Resume Analysis – Supports querying across multiple candidate resumes

        🔍 Context-Aware Answers – Uses RAG to ensure responses are grounded in resume data

        🧠 Semantic Search – Embedding-based retrieval for accurate context matching

        📄 Multiple File Formats – Supports PDF and DOCX resumes

        ⚡ Efficient & Scalable – Embeddings and retriever cached for faster responses

        🔐 Configurable LLM Backend – Easily switch or extend LLM providers

🧩 Tech Stack

        Frontend: Streamlit

        Backend: Python, LangChain

        LLM: Mistral

        Vector Store: Embedding-based vector database

        Document Processing: PDF & DOCX loaders

        Environment Management: Python .env configuration

🎯 Use Cases

        Resume screening and shortlisting

        Skill and experience comparison

        Candidate profiling

        Interview preparation support

        HR analytics and talent insights

🏗️ Architecture Overview

        Resumes are loaded and preprocessed

        Documents are chunked and embedded

        Embeddings are stored in a vector database

        User queries retrieve relevant resume context

        LLM generates grounded, contextual responses

        Answers are displayed via a chat-based UI

Folder Structure:

        ├── app.py              # Streamlit UI
        ├── src/                # Backend logic
        │   ├── load_doc.py
        │   ├── vector_store.py
        │   ├── prompts.py
        │   └── load_llm.py
        ├── data/resumes/       # Resume files
        ├── requirements.txt
        └── README.md

