import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.chat_agent import ask_bank_ai

st.title("🤖 SafeNest AI Banking Assistant")

user_input = st.text_input("Ask your banking question")

if st.button("Ask AI"):

    response = ask_bank_ai(user_input)

    st.success(response)