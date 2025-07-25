import os

OPENAI_API_KEY= "sk********"
LANGCHAIN_API_KEY ="******"

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LANGCHAIN_PROJECT"

import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Prompt Teamplate
prompt = ChatPromptTemplate(
    [
        ("system", "You are an helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    """
    question- user question
    api_key- openai api key
    llm- model
    temperature -  creativity measure
    max_tokens - llm parameter to set max tokens
    """
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm)
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})

    return answer

## Title of the app
st.title("Enhanced Q&A Chatbot with OpenAI")

## sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your own OpenAI API key:", type="password")

## Dropdown to create various LLm models
llm= st.sidebar.selectbox("Select you OpenAI Model", ["gpt-4o","gpt-4-turbo","gpt-4"])

## Adjust response parameter-- Temperature & max_tokens setting
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for "User Input"
st.write("Go ahead and ask any Question")
user_input = st.text_input("You:")

if user_input:
    response= generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(response)
else :
    st.write("Please provide the query.")


