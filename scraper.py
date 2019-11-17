import requests
from bs4 import BeautifulSoup

from parser import Meaning


URL = "https://www.google.com/search?q={}"


def fetch_content_from_web(word):
    """
    Method to make the request call and fetch content from URL
    :param word: Word whose meaning needs to be fetched
    """
    # TODO: Implement error handling here
    url_to_call = URL.format(word)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    response = requests.get(url_to_call, headers=headers)
    if response.status_code == 200:
        return response.text
    return {}

def fetch_meaning(entity):
    """
    Method to fetch the acttual meaning from the DOM tree
    """
    response = []
    for container in entity.find_all("div", class_="VpH2eb vmod XpoqFe"):
        meaning = Meaning(container)
        response.append({
            "word": meaning.word,
            "phonetic": meaning.phonetic,
            "audio_link": meaning.audio_link,
            "definitions": meaning.definitions
        })
    return response

def parse_html_content(raw_html_response):
    """
    Method to parse the HTML response received from GET call
    and fetch the meaning of the word from the response received
    :param raw_html_response: HTML response from GET call
    """
    soup = BeautifulSoup(raw_html_response, 'lxml')
    top_level_entity = soup.find("div", class_="lr_container mod yc7KLc")
    if not top_level_entity:
        print("No Results from GOOGLE")
        return {}
    return fetch_meaning(top_level_entity)

def scrape_meaning(word):
    """
    Method to scrape the meaning of a word from google search
    """
    # TODO: Add validation checks on the word passed
    raw_html_response = fetch_content_from_web(word)
    response = parse_html_content(raw_html_response)
    print(response)
    return response

if __name__ == "__main__":
    scrape_meaning("wasted")
