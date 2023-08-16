from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_text(url):
    """
    Extracts all the visible text from the body of the webpage specified by the URL using browser automation.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The extracted text from the webpage.
    """
    # Set Chrome options to run headless (without GUI)
    options = Options()
    options.add_argument('--headless') # Use this line instead of options.headless = True
    
    # Create a new Chrome browser instance
    with webdriver.Chrome(options=options) as driver:
        # Open the specified URL
        driver.get(url)
        
        # Wait for the page to load completely
        driver.implicitly_wait(10)
        
        # Get the page source (HTML content)
        page_source = driver.page_source
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract all the text within the page's <body> tag
    body = soup.find('body')
    text = body.get_text(separator="\n", strip=True)

    return text


if __name__ == "__main__":
    #url = "https://www.kdnuggets.com/2023/08/5-ways-chatgpt-code-interpreter-data-science.html"
    #url = "https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten"
    url = "https://www.immowelt.de/liste/muenchen/wohnungen/mieten?sort=relevanz"
    text = scrape_text(url)
    if text:
        print(text)



