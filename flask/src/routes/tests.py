from flask import Blueprint, make_response, request
from models import Post
from utils.make_celery import celery

tests = Blueprint('tests', __name__)

@tests.route('/', methods=['POST'])
def post():
    post = Post(data = 'raw_data')
    post.save()
    return post.json(), 201

@tests.route('/', methods=['GET'])
def get():
    posts = Post.objects()
    return posts.json(), 200

@tests.route('/<id>', methods=['GET'])
def get_id(id):
    post = Post.objects(id = id)
    if post:
        return post.json(), 200
    else:
        return 'Not found', 404

@tests.route('/', methods=['DELETE'])
def delete():
    for post in Post.objects:
        post.delete()
    return make_response('Ok', 204)

@tests.route('/process', methods=['POST'])
def create_task():
    args = request.get_json()
    task = celery.send_task('tasks.add', args=(args["x"], args["y"]))
    return make_response(f"{task.id}", 200)

@tests.route('/process/<id>', methods=['GET'])
def get_task(id):
    result = celery.AsyncResult(id, app=celery)
    if result.ready():
        return make_response(f"{result.get()}", 200)
    return make_response(f"{result.state}", 200)
