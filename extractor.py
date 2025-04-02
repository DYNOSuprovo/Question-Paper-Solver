import streamlit as st
import os
from google import generativeai as genai
import pathlib
from dotenv import load_dotenv

# Load API Key for Extractor AI
load_dotenv()
extractor_api_key = os.getenv("EXTRACTOR_API_KEY")

if not extractor_api_key:
    st.error("Extractor API Key not found.")
else:
    genai.configure(api_key=extractor_api_key)

def extract_questions(pdf_path):
    prompt = """NO NEED TO SOLVE THE QUESTION JUST GIVE THE EXTRACTED QUESTION FROM THE QUESTION PAPER
    NO SOLUTION JUST THE QUESTION PAPER 
    JUST GIVE THE TEXT FROM THE QUESTION PAPER IN A USER-READABLE FORMAT"""
    
    # Upload PDF to Gemini API
    uploaded_file = genai.upload_file(pdf_path)
    
    # Generate response
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content([uploaded_file, prompt])
    
    return response.text  # Return extracted questions
