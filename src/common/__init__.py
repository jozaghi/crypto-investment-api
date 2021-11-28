import json
from flask import Response


def json_response(data):
    return Response(json.dumps(data),  mimetype='application/json')
