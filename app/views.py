from app import app
from flask import json

@app.route('/', methods=['GET'])
def index():
  return 'Hello, world.'

@app.route('/api/sensors', methods=['GET'])
@app.route('/api/sensors/<int:id>', methods=['GET'])
def getSensor(id=1):
  return json.dumps({"sensor": id})
