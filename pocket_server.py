
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pocketIndex.html")

@app.route("/dictionary", methods=["POST"])
def return_search():
    search_word = request.form['word']
    file = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{search_word}")
    data = file.json()
    try:
        word = data[0]['word']
    except:
        return render_template("pocketError.html")
    try:
        phonetics = data[0]['phonetics'][0]['text']
    except:
        phonetics = ''
    meaning = data[0]['meanings'][0]['definitions'][0]['definition']
    try:
        pronunciation = data[0]['phonetics'][0]['audio']
    except:
        pronunciation = ''

    return render_template("pocketSearch.html",
                            data = data,
                            word = word,
                            phonetics = phonetics,
                            pronunciation = pronunciation,
                            meaning = meaning)

if __name__ == "__main__":
    app.run(debug=True)
