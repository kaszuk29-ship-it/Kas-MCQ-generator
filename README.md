# Kas AI - MCQ Generator

Kas AI is an AI-powered Multiple Choice Question generator built with Streamlit and Hugging Face.

## Features

* Generate MCQs from any topic
* Choose the number of questions
* Select difficulty level
* Four options for each question
* Correct answer and explanation
* Simple and colorful user interface
* Powered by Hugging Face AI

## Technologies Used

* Python
* Streamlit
* Hugging Face Hub
* Llama 3.1

## Project Structure

```text
kas-mcq-generator/
│
├── app.py
├── requirements.txt
└── .streamlit/
    └── secrets.toml
```

## Installation

Install the required packages:

```bash
pip install streamlit huggingface_hub
```

## Hugging Face API Token

Create a Hugging Face access token and add it to:

```text
.streamlit/secrets.toml
```

```toml
token = "YOUR_HUGGING_FACE_TOKEN"
```

Do not upload `secrets.toml` to GitHub.

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## How to Use

1. Enter a topic.
2. Select the number of questions.
3. Select the difficulty level.
4. Click **Generate MCQs**.
5. Kas AI generates the questions, options, answers, and explanations.

## Deployment

The application can be deployed using Streamlit Community Cloud.

Make sure `requirements.txt` contains:

```text
streamlit
huggingface_hub
```

Add the Hugging Face token through the Streamlit Cloud **Secrets** settings.

## Link
https://kas-mcq-generator-yeca3k8opuwgrjuwmp3s7q.streamlit.app/

## License

This project is created for educational purposes.

