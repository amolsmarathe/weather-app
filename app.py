from flask import Flask, request
from weather_program import greet, get_ip
import os

app = Flask(__name__)

DEPLOY = os.environ.get('DEPLOY')

@app.route('/')
def main():
    if DEPLOY == 'heroku':
        ip = request.headers['X-Forwarded-For']
    else:
        ip = get_ip()
    
    return greet(ip)


@app.route('/bye')
def bye():
    return 'Bye!'


@app.route('/ask')
def ask():
    return 'How are you doing?'


if __name__ == '__main__':
    app.run()