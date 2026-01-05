# Resume loading and chunking logic
import os
import re
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.schema.output_parser import StrOutputParser
from langchain_classic.schema.runnable import RunnablePassthrough


from dotenv import load_dotenv
from src.load_doc import load_resumes
from src.vector_store import create_vector_store
from src.prompts import load_tempate
from src.load_llm import load_llm



def main():
    print("Hello from llmops-chatbot-2!")
    
    load_dotenv()  # Loads .env into environment
    api_key = os.getenv("MISTRAL_API_KEY")

    docs = load_resumes(r"C:\Users\hp\Desktop\MLops\LLMOPS_RESUME_CHATBOT\LLMOPS_CHATBOT\data\resumes")
    
    print("Stage 1 : Complete - Documents loaded properly....")
    #print("Cleaned Docs : --> ",docs)
    print("Length of total documents: ",len(docs))
    

    vector_store = create_vector_store(docs)
    print("Stage 2 : Complete- Converted Chunks to Embeddings....")
    print("Vector store : ",vector_store)
    
    retriever=vector_store.as_retriever()
    print("Stage 3 : Complete- Created Retriver to retrive data from Embeddings....")
    
    template = load_tempate()
    prompt=ChatPromptTemplate.from_template(template)
    print("Stage 4 : Complete- Created a template for our bot....")
    print("Checking the prompt :", prompt)
    
    
    llm = load_llm(api_key)
    print("Stage 5 : Complete-Loaded the Mistral-LLM ....")
    print("Checking the llm :", llm)


    print("Stage 6 : Complete- Creating an output paser....")
    output_parser=StrOutputParser()
    
    rag_chain = (
    {"context": retriever,  "question": RunnablePassthrough()}
    | prompt
    | llm
    | output_parser
    )

    print("Stage 7 : Complete- Created a Chain....")
    
    print("Stage 8 : Final Question Answer....")
    print(rag_chain.invoke("Tell me about the Candidates ?"))
    

if __name__ == "__main__":
    main()
