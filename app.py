#Bring in Deps
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

apikey = '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'


os.environ['OPENAI_API_KEY'] = apikey

#App user Interface/framework
st.title('🦜️🔗 Youtube GPT Creator')
prompt = st.text_input('Plug in your prompt here')


#Prompt Template
title_template = PromptTemplate (
    input_variables = ['topic'],
    template = 'Write me a list of YouTube video titles about {topic}'
)

#llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm = llm, prompt = title_template, verbose= True)



if prompt:
    response = title_chain.run(topic = prompt)
    st.write(response)
    