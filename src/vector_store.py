# FAISS / Chroma vector store logic
from langchain_community.vectorstores import FAISS
#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_mistralai import MistralAIEmbeddings

def create_vector_store(docs):
    
    embeddings = MistralAIEmbeddings(
        model="mistral-embed"
    )
    return FAISS.from_documents(docs, embeddings)
