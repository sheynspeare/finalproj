from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## loads Gemini and get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question, stream=True)

##initialize streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Ask Dialogosaur!")

##initialize sesh state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input = st.text_input("Input: ", key="input")
submit=st.button("Send")

if submit and input:
    response=get_gemini_response(input)

    ## add user query and response to sesh chat history
    st.session_state['chat_history'].append(("You: ", input))
    st.subheader("The response: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Dialogosaur: ", chunk.text))
st.subheader("/n-------------------/n  The Chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
