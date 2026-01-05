from langchain_mistralai import ChatMistralAI


def load_llm(api_key):
    
    llm = ChatMistralAI(
        model="mistral-small",
        api_key=api_key
    )
    
    return llm