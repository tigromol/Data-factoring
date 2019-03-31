from mongoengine import *
from bson.objectid import ObjectId

class ConvertableDocument(Document):
    meta = {'allow_inheritance': True, 'abstract': True}
    
    def dict(self):
        res = self.to_mongo()
        for k, v in res.items():
            if isinstance(v, ObjectId):
                res[k] = str(v)
        res["id"] = res.pop("_id")
        res.pop("_cls")
        return res

# For tests
class Post(ConvertableDocument):
    data = StringField()

class Column(EmbeddedDocument):
    name = StringField(requied=True)
    data = ListField(DynamicField(), required=True)

class Data(ConvertableDocument):
    file = FileField(required=True)
    email = EmailField()
    columns = ListField(EmbeddedDocumentField(Column), required=True)
    created = DateTimeField(required=True)

class Function(ConvertableDocument):
    name = StringField(required=True, unique=True)
    display_name = StringField(required=True)
    args = ListField(StringField())