import streamlit as st
import os
from google import generativeai as genai
from dotenv import load_dotenv
import time
import re

# Load API Key for Solver AI
load_dotenv()
solver_api_key = os.getenv("SOLVER_API_KEY")

if not solver_api_key:
    st.error("Solver API Key not found.")
else:
    genai.configure(api_key=solver_api_key)

def split_questions(text):
    """Splits text into individual questions based on numbering patterns."""
    questions = re.split(r'(?=\n\d+\.)', text.strip())
    return [q.strip() for q in questions if q.strip()]

def solve_questions(questions_text):
    """Solve questions one by one to ensure full responses."""
    questions = split_questions(questions_text)
    solutions = []
    
    for i, question in enumerate(questions):
        prompt = f"Solve the following question with a detailed explanation. If it's related to OOPJ, provide the answer in Java:\n\n{question}"
        
        for attempt in range(3):  # Retry up to 3 times
            try:
                model = genai.GenerativeModel("gemini-1.5-pro")
                response = model.generate_content(prompt)
                full_response = response.text if response and hasattr(response, 'text') else "[No response received]"
                solutions.append(f"**Question {i+1} Solution:**\n{full_response}\n\n")
                break  # Exit retry loop if successful
            except Exception as e:
                if attempt < 2:
                    time.sleep(2)  # Wait before retrying
                else:
                    solutions.append(f"Error processing question {i+1}: {str(e)}")
    
    return "\n".join(solutions)

# Streamlit UI
def main():
    st.title("Exam Paper Solver")
    questions_text = st.text_area("Enter the question paper:")
    
    if st.button("Solve Questions"):
        if questions_text.strip():
            solutions = solve_questions(questions_text)
            st.text_area("Solutions:", solutions, height=500)
        else:
            st.error("Please enter the question paper.")

if __name__ == "__main__":
    main()
