from langchain_core.prompts import ChatPromptTemplate


def load_tempate():
    template="""You are an assistant for question-answering tasks.
    Use the following pieces of retrieved context to answer the question.
    If you don't know the answer, just say that you don't know.
    Use ten sentences maximum and keep the answer concise.
    Question: {question}
    Context: {context}
    Answer:
    """
    
    return template