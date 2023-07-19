import requests
from bs4 import BeautifulSoup

def scrape_articles(input_file):
    with open(input_file, 'r') as file:
        urls = file.read().splitlines()

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            article_text = extract_article_text(soup)
            save_article_text(url, article_text)
        else:
            print(f"Failed to retrieve content from {url}")

def extract_article_text(soup):
    # Add your code here to extract the article text from the BeautifulSoup object.
    # This will depend on the structure of the webpage and how the text is stored.

def save_article_text(url, article_text):
    # Add your code here to save the article text.
    # You can save it to a file, a database, or perform any other desired operation.

# Example usage
input_file = 'urls.txt'
scrape_articles(input_file)

