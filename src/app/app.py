import sys
sys.path.append('C:\\projects\\streamlit_langchain')
import streamlit as st
import openai
import json
from src.data_processing.processor import process_data
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate


# Set OpenAI API key
with open('credentials.json') as f:
    data = json.load(f)
    open_ai_api_key = data['OPEN_AI_API_KEY']
openai.api_key = open_ai_api_key


### OPTION 3
def get_openai_response(processed_text):
    # Define prompt

    template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=(
                    "You are a helpful assistant that re-writes the user's text to "
                    "Nimm an, dass du ein deutscher Immobilienexperte bist."
                    "Du erhältst gescrapten Text von einer Website."
                    "Du erhältst gescrapten Text von einer Website."
                    "Deine Aufgabe ist es, die auf dieser Website aufgeführten Immobilienangebote zusammenzufassen."
                    "Fasse dich dabei kurz, aber stelle für jede Immobilie die wichtigsten Punkte heraus."
                    "Die Ausgabe deiner Antwort sollte übersichtlich sein."
                    "Starte deine Antwort mit einer kurzen Zusammenfassung dazu, wieviele Objekte es gibt."
                    "Sollte es sich bei der Website nicht um ein Immobilienportal handeln, sage das dem User"
                    "und fasse sehr kurz zusammen, was es stattdessen ist."
                )
            ),
            HumanMessagePromptTemplate.from_template(
                "Fasse die folgenden Immobilienangebote kurz und prägnant zusammen: {text}"
            ),
        ]
    )

    messages = template.format_messages(text=processed_text)

    # Define LLM chain
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", openai_api_key=openai.api_key)
    response = llm(messages)


    #llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Get response from OpenAI
    #response = llm_chain.generate()

    return response


st.title("Web Scraping and Summarization")

description = """
**🥁 Drum roll, please... Introducing: The Real Estate Summarizer! 🥁**

This app allows you to quickly and easily extract summarized insights from real estate listings on various platforms. All you need to do is provide the URL of a search results page, and the app will take care of the rest!

👉 Try it out with this example URL: [https://www.immowelt.de/liste/muenchen-altstadt-lehel/immobilien](https://www.immowelt.de/liste/muenchen-altstadt-lehel/immobilien)

Please note that this app works well with, for example, immowelt.de. However, due to protection mechanisms, it is unable to get content from immobilienscout24.de.
"""
st.markdown(description)

url = st.text_input("Enter the URL of a real estate platforms:")

if url:
    st.write(f"URL: {url}")

    with st.spinner('Scraping and summarizing the content...'):
        processed_text = process_data(url)
        summary = get_openai_response(processed_text)
    
    st.write(f"Answer: {summary.content}")
