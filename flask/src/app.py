from flask import Flask,request,flash,redirect
import os
import pymongo
from pymongo import MongoClient as mc
import parse as p

app = Flask(__name__)
app.secret_key = os.urandom(24)
client = mc('mongo',27017,username='admin',password='admin') #ip and host here
db = client.celery

## We insert one file in dict formation (parsed via pandas parse module)
@app.route('/api/data/',methods=['POST','GET'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    else:
        posts = db.posts
        print('wtf is this')
        posts.insert_one(p.parse(file))
        return 'success'

## Test route db.posts.find() returns cursor object from bd
## indexes of cursor is apparantly posts from db
@app.route('/test',methods=['POST','GET'])
def test():
    show = db.posts.find()
    return str(show[1])

def proc(arr,args):
    for i in args:
        arr = i(arr)
if __name__ == '__main__':
    app.debug = True
    app.run()
