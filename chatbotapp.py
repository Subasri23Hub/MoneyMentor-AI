import streamlit as st
import google.generativeai as genai
from prompts import get_prompt
import pandas as pd
import plotly.express as px

# GEMINI CONFIG
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# PAGE CONFIG 
st.set_page_config(
    page_title="MoneyMentor AI",
    page_icon=" $ ",
    layout="wide"
)

# BACKGROUND STYLE 
st.markdown("""
<style>

/* Brighter background image */
.stApp {
    background: linear-gradient(rgba(255,255,255,0.15), rgba(255,255,255,0.10)),
    url("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main content container */
.block-container {
    background: rgba(255,255,255,0.85);
    padding: 2rem;
    border-radius: 15px;
}

/* Headings */
h1, h2, h3 {
    color: #1f2c56;
}

</style>
""", unsafe_allow_html=True)

#  HEADER
st.title("MoneyMentor AI!")
st.write("Your AI-powered financial advisor for smarter budgeting, saving, and investing.")

st.divider()

st.subheader("Enter Your Financial Details!")

col1, col2, col3 = st.columns(3)

with col1:
    income = st.number_input("Monthly Income (₹)", min_value=0)

with col2:
    expenses = st.number_input("Monthly Expenses (₹)", min_value=0)

with col3:
    goal = st.text_input("Savings Goal")

# DASHBOARD 
if income > 0:

    savings = income - expenses

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Income", f"₹{income}")

    with m2:
        st.metric("Expenses", f"₹{expenses}")

    with m3:
        st.metric("Potential Savings", f"₹{savings}")

    # Pie chart
    data = pd.DataFrame({
        "Category": ["Expenses", "Savings"],
        "Amount": [expenses, savings]
    })

    fig = px.pie(
        data,
        names="Category",
        values="Amount",
        title="Budget Overview"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

#  CHATBOT 
st.subheader("Ask Your AI Financial Advisor!")

user_input = st.text_input("Ask a question about budgeting, saving, or investing")

if st.button("Get Advice!!"):

    if user_input == "":
        st.warning("Please enter a question.")
    else:

        prompt = get_prompt(user_input, income, expenses, goal)

        with st.spinner("Thinking... 🤔"):
            response = model.generate_content(prompt)

        st.success("Here is your personalized financial advice")

        st.write(response.text)
