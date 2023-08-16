import sys
sys.path.append('C:\\projects\\streamlit_langchain')
import streamlit as st
import openai
import json
from src.data_processing.processor import process_data

# Set OpenAI API key
with open('credentials.json') as f:
    data = json.load(f)
    open_ai_api_key = data['OPEN_AI_API_KEY']
openai.api_key = open_ai_api_key


### OPTION 3
def get_openai_response(prompt):
    """Gets an AI-generated response from Bard."""
    client = openai.ChatCompletion()
    response = client.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response['choices'][0]['message']['content']


st.title("Web Scraping and Summarization")

url = st.text_input("Enter the URL you want to scrape:")

if url:
    processed_text = process_data(url)

    prompt = f"Summarize the following text:\n{processed_text}"

    summary = get_openai_response(prompt)
    st.write(f"URL: {url}")
    st.write(f"Answer: {summary}")
