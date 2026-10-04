import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="GPT Study Assistant", page_icon="🤖")

st.title("🤖 GPT Study Assistant")
st.write("A simple Generative AI application built with Python and the OpenAI Responses API.")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY is not set. Add your API key as an environment variable before running the app.")
    st.stop()

client = OpenAI(api_key=api_key)

question = st.text_area(
    "Enter your question:",
    placeholder="Example: Explain artificial intelligence in simple words."
)

if st.button("Generate Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = client.responses.create(
                    model=os.getenv("OPENAI_MODEL", "gpt-6-luna"),
                    instructions=(
                        "You are a helpful study assistant. "
                        "Give clear, accurate and beginner-friendly answers. "
                        "Use short examples when useful."
                    ),
                    input=question
                )
                st.subheader("GPT Response")
                st.write(response.output_text)
            except Exception as e:
                st.error(f"API error: {e}")
