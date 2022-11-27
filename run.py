
import requests
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dictionary', methods=['POST'])
def return_search():
    search_word = request.form['word']
    file = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{search_word}')
    data = file.json()
    try:
        word = data[0]['word']
    except:
        return redirect(url_for('word_not_found'))
    try:
        phonetics = data[0]['phonetics'][0]['text']
    except:
        phonetics = ''
    try:
        pronunciation = data[0]['phonetics'][0]['audio']
    except:
        pronunciation = ''

    meaning = data[0]['meanings'][0]['definitions'][0]['definition']

    return render_template('search.html',
                            data = data,
                            word = word,
                            phonetics = phonetics,
                            pronunciation = pronunciation,
                            meaning = meaning)

@app.route('/not_found', methods=['GET', 'POST'])
def word_not_found():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
