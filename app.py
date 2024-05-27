import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
# load groq API key
groq_api_key=os.environ['GROQ_API_KEY']



prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an helpful assistant. Please response to user queries"),
        ("user", "Question:{question}")
    ]
)

##Steamlit framework

st.title("Groq Demo using LangChain")
input_text=st.text_input("Enter your prompt")

#llm
llm=ChatGroq(groq_proxy=groq_api_key,
             model_name="llama3-70b-8192")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))