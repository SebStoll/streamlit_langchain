from src.data_extraction.scraper import scrape_text


def process_data(url):
    text = scrape_text(url)
    # Your data processing code here
    with open("data/raw/scraped_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    # Processing...
    processed_data = text
    return processed_data


if __name__ == "__main__":
    url = "https://www.kdnuggets.com/2023/08/5-ways-chatgpt-code-interpreter-data-science.html"
    text = process_data(url)
    if text:
        print(text)