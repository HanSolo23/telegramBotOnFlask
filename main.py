from flask import Flask
from flask_sslify import SSLify
import requests

#app = Flask(__name__)
#sslify = SSLify(app)
#@app.route('/')
#def index():
    #return '<h1>Hi</h1>'

URL = 'https://api.telegram.org/bot1050128789:AAGO5PeFQ8DNdpTHLf_p37_aQWy505JhIF8/'

def main():
    r = requests.get(URL + 'getMe')
    print(r.json())


if __name__ == '__main__':
    main()
