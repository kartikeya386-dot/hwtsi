import streamlit as st
import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = "Generate {number} tweets on {topic}. Include only the tweet(s) in your response."

tweet_prompt = PromptTemplate.from_template(template)

tweet_chain = tweet_prompt|llm 



#print(response.content)

st.header("Tweet Generator Yeah!")
st.subheader("Generate Tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of Tweets",min_value=1,max_value=10,value=1,step=1)

if st.button("Generate"):
    response = tweet_chain.invoke({"number":number,"topic":topic})
    st.write(response.content)