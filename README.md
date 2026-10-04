# Exploring Generative AI Using GPT

## Project Overview
This project demonstrates a simple Generative AI application built with Python and GPT. The application accepts a user's question and generates a natural-language answer using the OpenAI Responses API.

## Objectives
- Understand the basic idea of Generative AI.
- Explore GPT as a Generative AI model.
- Use Python to interact with an AI API.
- Demonstrate a practical use case through a simple study assistant.
- Understand the role of prompts/instructions in generating useful responses.

## Generative AI Model
The project uses a GPT model through the OpenAI API. GPT is a generative language model that can produce human-like text from user input.

## Use Cases of GPT
GPT-based systems can be used for:
- Question answering
- Summarization
- Content generation
- Study assistance
- Text rewriting
- Customer support
- Brainstorming and idea generation

## Application
### GPT Study Assistant
The application is a simple web interface where a student enters a question. The Python application sends the input to the GPT model and displays the generated response.

### Workflow
1. User enters a question.
2. The application sends the question to the GPT model through the API.
3. GPT processes the input.
4. The generated answer is returned.
5. The answer is displayed in the Streamlit interface.

## Technologies Used
- Python
- OpenAI API
- Streamlit
- GPT
- GitHub

## Prompt / Instructions
The application instructs the model to act as a helpful study assistant and provide clear, accurate and beginner-friendly answers.

## Setup

1. Install Python.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the API key as an environment variable.

Windows PowerShell:
```powershell
$env:OPENAI_API_KEY="YOUR_API_KEY"
```

Optional model setting:
```powershell
$env:OPENAI_MODEL="gpt-6-luna"
```

4. Run the application:

```bash
streamlit run app.py
```

## Important Security Note
Never upload an API key to GitHub. Keep the key in an environment variable or a local secrets file that is excluded by `.gitignore`.

## Conclusion
This project demonstrates how Generative AI can be integrated into a simple Python application. It shows the connection between user prompts, an AI model, an API and a user interface.
