from flask import Flask, request, jsonify
from flask_sslify import SSLify
import requests
import json
import re

app = Flask(__name__)
sslify = SSLify(app)


URL = 'https://api.telegram.org/bot1050128789:AAGO5PeFQ8DNdpTHLf_p37_aQWy505JhIF8/'


def write_json(data, filename='answer.json'):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):
    url = 'https://api.coincap.io/v2/assets/{}'.format(crypto)
    r = requests.get(url).json()
    price = r['data']['priceUsd']
    return price


def send_message(chat_id, text='я робот!'):
    url = URL + 'sendMessage'
    message = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=message)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        textMessage = r['message']['text']
        pattern = r'/\w+'
        if re.search(pattern, textMessage):
            price = get_price(parse_text(textMessage))
            send_message(chat_id, text=price)
        # write_json(r)
        return jsonify(r)
    return '<h1>Hi</h1>'


if __name__ == '__main__':
    app.run()
