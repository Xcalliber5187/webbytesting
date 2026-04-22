from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

@app.route('/renewable')
def renewable():
    url = "https://www.smartgriddashboard.com/roi/generation/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    pattern = r"RENEWABLE GENERATION\s*([\d.]+)\s*%"

    match = re.search(pattern, soup.get_text())

    if match:
        renewable_generation = match.group(1)
        return f"Renewable Generation: {renewable_generation}%"
    else:
        return "Renewable Generation data not found."
