from setuptools import setup, find_packages

setup(
    name="streamlit_langchain",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "openai",
    ],
)