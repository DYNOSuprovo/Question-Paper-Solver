# DYNO AI Question Paper Solver

## Overview
DYNO AI is an AI-powered tool designed to extract and solve questions from a PDF question paper. The application is built using Streamlit and leverages Google's Gemini AI to process and generate solutions.

## Features
- **Upload PDF Question Papers**: Users can upload a PDF file containing exam questions.
- **Automatic Question Extraction**: The AI extracts questions from the PDF without additional text.
- **AI-Powered Solutions**: The extracted questions are processed, and AI-generated answers are provided.
- **Java-Specific Solutions**: If a question is related to Object-Oriented Programming in Java (OOPJ), the solution is generated in Java.
- **Error Handling & Retries**: Implements a retry mechanism to ensure stable responses.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Front-end framework for building interactive web applications.
- **Google Gemini AI**: Used for both question extraction and solution generation.
- **dotenv**: Manages API keys securely.
- **pathlib**: Handles file operations.

## Installation
### Prerequisites
Ensure you have Python installed (>=3.8). Then, install the required dependencies:

```bash
pip install streamlit google-generativeai python-dotenv pathlib
```

### Environment Setup
Create a `.env` file in the project directory and add your API keys:

```
SOLVER_API_KEY=your_gemini_solver_api_key
EXTRACTOR_API_KEY=your_gemini_extractor_api_key
```

## Usage
### Running the Application
Run the Streamlit app using the following command:

```bash
streamlit run app.py
```

### How It Works
1. Upload a PDF question paper.
2. The AI extracts the questions.
3. Click "Solve Questions" to generate AI-powered solutions.
4. View and copy the answers for reference.

## File Structure
```
├── app.py                 # Main Streamlit application
├── solver.py              # AI-based solution generator
├── extractor.py           # AI-based question extractor
├── .env                   # Environment variables (API Keys)
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## Future Improvements
- Enhance PDF text extraction for better accuracy.
- Improve AI-generated solutions with context-aware explanations.
- Add support for more programming languages.

## License
This project is open-source and available for modification. Feel free to contribute!

---

Developed with ❤️ by DYNO AI Team.

