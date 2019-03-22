from flask import Blueprint, request, make_response
from utils.parse import parse

data = Blueprint('data', __name__)

## We insert one file in dict formation (parsed via pandas parse module)
@data.route('/', methods=['POST','GET'])
def upload():
    if 'file' not in request.files:
        return make_response('No file', 400)

    file = request.files['file']

    if file.filename == '':
        return make_response('No file', 400)
    else:
        #posts = db.posts
        #posts.insert_one(parse(file))
        return 'success'