import streamlit as st
import pathlib
from extractor import extract_questions
from solver import solve_questions

st.title("DYNO AI Question Paper Solver")
st.write("Upload a PDF question paper, and the AI will solve it with explanations.")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    filepath = pathlib.Path("temp.pdf")

    with st.spinner("Extracting questions..."):
        extracted_questions = extract_questions(filepath)

    st.subheader("Extracted Questions:")
    st.write(extracted_questions)

    if st.button("Solve Questions"):
        with st.spinner("Generating solutions..."):
            solutions = solve_questions(extracted_questions)
        
        st.subheader("AI-Generated Solutions:")
        st.write(solutions)
