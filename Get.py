import requests
from flask import Flask, render_template
import json

app = Flask(__name__)

# Haal de data op van de API (je JSON-bestand op GitHub)
def get_data_from_api():
    url = 'https://raw.githubusercontent.com/JarneRaes1710/Weapon-API/master/db.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['game_items']  # Haal de lijst van game items op
    return None

@app.route('/')
def home():
    items = get_data_from_api()
    if items:
        return render_template('index.html', items=items)
    return "Er is een probleem met het ophalen van de data."

@app.route('/weapon/<int:id>')
def weapon(id):
    items = get_data_from_api()
    item = next((i for i in items if i['id'] == id), None)
    if item:
        return render_template('weapon.html', item=item)
    return "Wapen niet gevonden."

if __name__ == '__main__':
    app.run(debug=True)
