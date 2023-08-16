# Streamlit and Langchain Experiments Series: The Real Estate Summarizer!
A Streamlit app which allows you to quickly and easily extract summarized insights from real estate listings on various platforms. All you need to do is provide the URL of a search results page, and the app will take care of the rest.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
1. Ensure you have Python 3.11.4 or higher installed.
2. Clone this repository: `git clone https://github.com/SebStoll/streamlit_langchain.git`
3. Navigate to the project directory: `cd streamlit_langchain`
4. Install the dependencies: `pip install -r requirements.txt`
5. Get an OpenAI API key from https://platform.openai.com/.
6. Create file `credentials.json` in the project root:
    ```
    {
    "OPEN_AI_API_KEY": "<YOUR_OPENAI_API_KEY>"
    }
    ```

## Usage
1. From the project root, run the Streamlit app: `streamlit run src/app/app.py`
2. The app should open in the browser. Follow the instructions there.
