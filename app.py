from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = '14f4c639'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    title = request.form['title']
    url = f'http://www.omdbapi.com/?t={title}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)
    return render_template('result.html', movie=data)

if __name__ == '__main__':
    app.run(debug=True)
