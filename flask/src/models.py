from mongoengine import *
from flask import jsonify

class JsonQuerySet(QuerySet):

    def json(self):
        return jsonify([post.dict() for post in self])

class ConvertableDocument(Document):
    meta = {'queryset_class': JsonQuerySet, 'allow_inheritance': True}

    def json(self):
        return jsonify(self.dict())
    
    def dict(self):
        res = self.to_mongo()
        res["id"] = str(res.pop("_id"))
        res.pop("_cls")
        return res
        
class Post(ConvertableDocument):
    data = StringField()