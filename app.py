import streamlit as st
from groq import Groq
import os

# ==========================
# API KEY (ENV VARIABLE)
# ==========================
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Groq Chatbot")

# ==========================
# SESSION MEMORY
# ==========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# USER INPUT
# ==========================
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

# ==========================
# DISPLAY CHAT
# ==========================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
