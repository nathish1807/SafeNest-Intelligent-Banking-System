import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from agents.coordinator import process_transaction, process_loan
from agents.chat_agent import ask_bank_ai

st.set_page_config(page_title="SafeNest AI Banking", layout="wide")

st.title("🏦 SafeNest AI Banking System")

menu = st.sidebar.selectbox(
    "Select Service",
    ["Fraud Detection", "Loan Eligibility", "AI Banking Assistant", "Analytics Dashboard"]
)

# ---------------- FRAUD DETECTION ----------------
if menu == "Fraud Detection":

    st.header("Transaction Fraud Detection")

    amount = st.number_input("Enter Transaction Amount", min_value=0)

    if st.button("Check Transaction"):
        result = process_transaction(amount)
        st.success(result)

# ---------------- LOAN ELIGIBILITY ----------------
elif menu == "Loan Eligibility":

    st.header("Loan Eligibility Check")

    income = st.number_input("Monthly Income", min_value=0)
    credit = st.number_input("Credit Score", min_value=0)

    if st.button("Check Loan"):
        result = process_loan(income, credit)
        st.success(result)

# ---------------- AI CHATBOT ----------------
elif menu == "AI Banking Assistant":

    st.header("🤖 AI Banking Assistant")

    question = st.text_input("Ask your banking question")

    if st.button("Ask AI"):
        response = ask_bank_ai(question)
        st.success(response)

# ---------------- ANALYTICS DASHBOARD ----------------
elif menu == "Analytics Dashboard":

    st.header("📊 Transaction Analytics")

    import os

    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", "transactions.csv")

    df = pd.read_csv(file_path)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Fraud vs Safe Transactions")

    fig, ax = plt.subplots()
    sns.countplot(x="fraud", data=df, ax=ax)

    ax.set_xticklabels(["Safe", "Fraud"])
    ax.set_title("Fraud Detection Distribution")

    st.pyplot(fig)

    st.subheader("Transaction Amount Distribution")

    fig2, ax2 = plt.subplots()
    sns.histplot(df["amount"], bins=20, ax=ax2)

    ax2.set_title("Transaction Amount Distribution")

    st.pyplot(fig2)