import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.secret_key = 'some_secret'

@app.route('/')
def hello():
    return 'Hello World... again'
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)