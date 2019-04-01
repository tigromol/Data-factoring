import os

from flask import Flask
from json_encoder import CustomJSONEncoder
# Configure database
from mongoengine import connect

connect('datafactoring', host='mongo', port=27017, username='admin', password='admin')

# Configure main application
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)
app.json_encoder = CustomJSONEncoder

# Register routes
from routes.data import data
from routes.functions import functions
from routes.tests import tests

app.register_blueprint(data, url_prefix='/api/data/')
app.register_blueprint(functions, url_prefix='/api/functions/')
app.register_blueprint(tests, url_prefix='/api/tests/')

if __name__ == '__main__':
    app.run()
