import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st


os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.header("How would they say it?")
st.subheader("How would emotional personalities say something?")

emotions= ["Happy", "Sad" , "Angry", "Fearful", "Surprised" , "Disgusted" , "Loving" , "Guilty" , "Ashamed" , "Proud"]
roles = ["Architect" , "Cricketer" , "Commentator" , "News Reader" , "Business Manager" , "Policeman" , "Gangster" , "Ninja" , "Masterchef" , "Ghost" , "Commando", "Poet"]

emotion = st.selectbox("Choose an emotion :",emotions)
role = st.selectbox("Choose a personality :",roles)

input = st.text_input("Enter your message")

template = "Assume the role of a {emotion}{role}. How would you say the following - {input}. The response must have language and vocbulary used by a typical {role}. Make the response atlease 10 words, exagerrate if the input is very simple. Just return the answer in your response, do not add any explanations or fluff from your end. "

hwtsi_prompt = PromptTemplate.from_template(template)

hwtsi_chain = hwtsi_prompt|llm

if st.button("HOW WOULD THEY SAY IT?"):
    response = hwtsi_chain.invoke({"emotion":emotion,"role":role,"input":input})
    st.write(response.content)
