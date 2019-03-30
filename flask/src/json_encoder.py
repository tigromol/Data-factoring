import numpy
from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, numpy.int64):
                return int(obj)
        except TypeError:
            pass
        return JSONEncoder.default(self, obj)