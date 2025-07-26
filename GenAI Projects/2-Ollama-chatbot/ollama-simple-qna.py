import os

LANGCHAIN_API_KEY ="***********"

os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LANGCHAIN_PROJECT"

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question : {question}")
    ]
)

## Streamlit Framework
st.title("Langchain Demo with Gemma 2 Model")
input_text = st.text_input("What Question you have in mind?")

## Ollama Llama2 Model
llm = Ollama(model= "gemma:2b")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))



