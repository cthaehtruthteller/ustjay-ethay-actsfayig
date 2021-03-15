import os
import re

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def display_url(fact):
    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    payload = {'input_text': fact}

    redirection = requests.post(url, data=payload, allow_redirects=False)

    return redirection.headers['Location']

@app.route('/')
def home():
    fact = get_fact().strip()
    body = display_url(fact)

    return Response(response=body, mimetype="text/html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

