from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from langchain_core.messages import HumanMessage, SystemMessage

import os

OPENAI_API_KEY= "sk-*******************************"
LANGCHAIN_API_KEY ="*********"
GROQ_API_KEY= "*******************************"

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LANGCHAIN_PROJECT"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# HumanMessage --> messages provided by the human being/user
# SystemMessage --> instruction to the LLM --> how the LLM model should work like

# 1. Create model
model = ChatGroq(model="gemma2-9b-it")
model

# 2. Create Prompt template
system_template = "Translate the following into {language}:"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("human","{text}")
    ]
)

# 3. Create Parser
parser = StrOutputParser()

# 4. Create Chain
chain = prompt | model | parser

# chain.invoke({"language": "French", "text": "hello"})

# 5. App definition
app= FastAPI(title = "Langchain server",
             version="1.0",
             description="A simple API server using langchain runnable interfaces")

# 6. Adding Chain routes
add_routes(
    app,
    chain,
    path="/chain"
)
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



