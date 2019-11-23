from flask import Flask

from backend.scraper import scrape_meaning
app = Flask(__name__)

@app.route("/fetch_meaning/<string:word>")
def fetch_meaning(word):
    meaning = scrape_meaning(word)
    return meaning

if __name__ == "__main__":
    app.run()
