import requests
from bs4 import BeautifulSoup


def scrape_text(url):
    """
    Extracts all the visible text from the body of the webpage specified by the URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The extracted text from the webpage.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.google.com/'  # Set the Referer header to mimic a typical browser request
    }
    
    # Create a session to handle cookies and session data automatically
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all the text within the page's <body> tag
    body = soup.find('body')
    text = body.get_text(separator="\n", strip=True)

    return text



if __name__ == "__main__":
    url = "https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten"  # Replace with the URL of the website you want to scrape
    text = scrape_text(url)
    if text:
        print(text)



