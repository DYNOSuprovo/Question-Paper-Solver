import streamlit as st
import os
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()
extractor_api_key = os.getenv("EXTRACTOR_API_KEY")

if not extractor_api_key:
    st.error("Extractor API Key not found. Please set EXTRACTOR_API_KEY in .env file.")
    st.stop()

genai.configure(api_key=extractor_api_key)

def extract_questions(pdf_file):
    prompt = """NO NEED TO SOLVE THE QUESTION JUST GIVE THE EXTRACTED QUESTION FROM THE QUESTION PAPER
NO SOLUTION JUST THE QUESTION PAPER 
JUST GIVE THE TEXT FROM THE QUESTION PAPER IN A USER-READABLE FORMAT"""

    try:
        uploaded_file = genai.upload_file(pdf_file)

        model = genai.GenerativeModel("gemini-2.0-flash")

        # Pass list: first file ref, then prompt string
        response = model.generate_content([
            uploaded_file,
            prompt
        ])

        return response.text

    except Exception as e:
        st.error(f"Error during extraction: {e}")
        return None

def main():
    st.title("DYNO AI Question Paper Solver")
    st.write("Upload a PDF question paper, and the AI will extract questions from it.")

    uploaded_pdf = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_pdf is not None:
        with st.spinner("Extracting questions..."):
            questions_text = extract_questions(uploaded_pdf)

            if questions_text:
                st.subheader("Extracted Questions:")
                st.write(questions_text)

if __name__ == "__main__":
    main()
