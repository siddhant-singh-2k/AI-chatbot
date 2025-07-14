from os import system

import streamlit as st
from langchain_community.callbacks.fiddler_callback import MODEL_NAME


st.set_page_config(page_title="AI agent", layout="centered")
st.title("AI Chatbot agents")
st.write("Create and Interact with the AI agent")

system_prompt = st.text_area("Define your AI agent:", height=70,placeholder="Type your system prompt here..")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq","OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Groq Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("OpenAI Model",MODEL_NAMES_OPENAI)


allowed_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query", height= 150,placeholder="Ask anything!")

API_URL ="http://127.0.0.1:9999/chat"



if st.button("Ask Agent"):
    if user_query.strip():
        import  requests

        payload = {
        "model_name" : selected_model,
        "model_provider" : provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allowed_web_search}


        response = requests.post(API_URL,json=payload)

        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"The final response: {response_data}")







