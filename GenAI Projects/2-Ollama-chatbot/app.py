import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os

LANGCHAIN_API_KEY ="***************"

os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LANGCHAIN_PROJECT"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",""),
        ("user","Question:{question}")
    ]
)

def generate_response(question, engine, temperature, max_tokens):
    """
    question- user question
    api_key- openai api key
    engine- ollama model
    temperature -  creativity measure
    max_tokens - llm parameter to set max tokens
    """
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})

    return answer

## Title of the app
st.title("Enhanced Q&A Chatbot with Ollama")

## sidebar for settings
st.sidebar.title("Settings")

## Dropdown to create various LLm models
engine= st.sidebar.selectbox("Select you OpenAI Model", ["gemma:2b","mistral"])

## Adjust response parameter-- Temperature & max_tokens setting
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for "User Input"
st.write("Go ahead and ask any Question")
user_input = st.text_input("You:")

if user_input:
    response= generate_response(user_input, engine, temperature, max_tokens)
    st.write(response)
else :
    st.write("Please provide the query.")
