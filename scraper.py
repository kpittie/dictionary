import requests
from bs4 import BeautifulSoup

from parser import Meaning


URL = "https://www.lexico.com/en/definition/{}"


def fetch_content_from_web(word):
    """
    Method to make the request call and fetch content from URL
    :param word: Word whose meaning needs to be fetched
    """
    # TODO: Implement error handling here
    url_to_call = URL.format(word)
    response = requests.get(url_to_call)
    if response.status_code == 200:
        return response.text
    return {}

def fetch_meaning(entity):
    """
    Method to fetch the acttual meaning from the DOM tree
    """
    meaning = Meaning(entity)
    return {
        "word": meaning.word,
        "phonetic": meaning.phonetic,
        "audio_link": meaning.audio_link,
        "definitions": meaning.definitions
    }

def parse_html_content(raw_html_response):
    """
    Method to parse the HTML response received from GET call
    and fetch the meaning of the word from the response received
    :param raw_html_response: HTML response from GET call
    """
    soup = BeautifulSoup(raw_html_response, 'lxml')
    primary_container = soup.find("div", class_="entryWrapper")
    if not primary_container:
        print("No results from LEXICO")
        return
    return fetch_meaning(primary_container)

def scrape_meaning(word):
    """
    Method to scrape the meaning of a word from google search
    """
    # TODO: Add validation checks on the word passed
    raw_html_response = fetch_content_from_web(word)
    response = parse_html_content(raw_html_response)
    return response

if __name__ == "__main__":
    print(scrape_meaning("wasted"))
    print(scrape_meaning("discombobulated"))
    print(scrape_meaning("miscreant"))
