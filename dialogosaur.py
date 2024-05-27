from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create generative model and chat session
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
  """Fetches response from Gemini model"""
  response = chat.send_message(question, stream=True)
  return response

# Streamlit App Interface
st.set_page_config(page_title="Chatbot Demo")
st.header("ASK DIALAGOSAUR!")
st.header4("Submitted by: Shayne B. Yanson BSCS 3B")

user_input = st.text_input("Enter your query: ")
submit_button = st.button("Ask")

if submit_button and user_input:
  response = get_gemini_response(user_input)
  
  st.subheader("Dialogosaur:")
  for chunk in response:
    st.write(chunk.text)
    st.session_state['chat_history'].append(("Dialogosaur: ", chunk.text))

# (Optional) Chat history display (requires session state)
if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []

st.subheader("Response History:")
for role, text in st.session_state['chat_history']:
  st.write(f"{role}:{text}")

# Run Streamlit app
if __name__ == "__main__":
  st.run()
