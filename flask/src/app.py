import os

from flask import Flask
# Configure database
from mongoengine import connect

connect('datafactoring', host='mongo', port=27017, username='admin', password='admin')

# Configure main application
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)

# Register routes
from routes.data import data
from routes.functions import functions
from routes.tests import tests

app.register_blueprint(data, url_prefix='/api/data/') 
app.register_blueprint(functions, url_prefix='/api/functions/') 
app.register_blueprint(tests, url_prefix='/api/tests/')

def proc(arr,args):
    for i in args:
        arr = i(arr)

if __name__ == '__main__':
    app.run()
