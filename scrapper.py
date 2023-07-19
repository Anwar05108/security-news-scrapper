import os
import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = '\n'.join(paragraph.get_text() for paragraph in paragraphs)

        return text
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data from {url}: {e}")
        return None
    except Exception as e:
        print(f"Error occurred while processing {url}: {e}")
        return None

def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    # Assuming you have a text file named "urls.txt" containing one URL per line
    input_file = "urls.txt"
    output_folder = "output_texts"
    i = 0

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, 'r') as file:
        for line in file:
            url = line.strip()
            if not url:
                continue

            try:
                # Extract the last part of the URL to use as the filename
                i += 1
                filename = os.path.join(output_folder, str(i)) + ".txt"
                

                text = extract_text_from_url(url)
                if text:
                    save_text_to_file(text, filename)
                    print(f"Text extracted from {url} and saved to {filename}")
                else:
                    print(f"Failed to extract text from {url}")
            except Exception as e:
                print(f"Error occurred while processing {url}: {e}")
