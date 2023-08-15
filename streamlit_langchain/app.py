import streamlit as st
import openai
import json

# Set OpenAI API key
with open('credentials.json') as f:
    data = json.load(f)
    open_ai_api_key = data['OPEN_AI_API_KEY']
openai.api_key = open_ai_api_key


### OPTION 3
def get_bard_response(question):
    """Gets an AI-generated response from Bard."""
    client = openai.ChatCompletion()
    response = client.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    )
    return response['choices'][0]['message']['content']


st.title("Ask Bard a question")

question = st.text_input("Enter your question:")

if question:
    response = get_bard_response(question)
    st.write(f"Question: {question}")
    st.write(f"Answer: {response}")
