import streamlit as st



st.set_page_config(page_title="AI agent", layout="wide")
st.title("🤖 AI Chatbot Agents")
st.write("Create and Interact with the AI agent")

st.markdown("---")
st.subheader("🧠 Define Your AI Agent")
system_prompt = st.text_area("System Prompt", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

st.markdown("---")
st.subheader("🌐 Select Model Provider")
provider = st.radio("Provider", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Groq Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("OpenAI Model", MODEL_NAMES_OPENAI)

allowed_web_search = st.checkbox("Allow Web Search")

st.markdown("---")
st.subheader("📝 Ask Your Question")
user_query = st.text_area("Your Query", height=150, placeholder="Ask anything!")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("🚀 Ask Agent"):
    if user_query.strip():
        import requests

        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allowed_web_search
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("🧾 Agent Response")
                st.markdown(f"**The final response:** {response_data}")







