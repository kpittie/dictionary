from flask import Flask, render_template, request

from backend.scraper import scrape_meaning
app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/fetch_meaning", methods=["POST"])
def fetch_meaning():
    word = request.form["word"]
    meaning = scrape_meaning(word)
    return render_template("index.html", response=meaning)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
