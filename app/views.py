from app import app, db
from flask import json, request, abort
from models import Sensor, Measure
from datetime import datetime

@app.route('/', methods=['GET'])
def index():
  return 'Hello, world.'

@app.route('/api/sensors', methods=['GET'])
@app.route('/api/sensors/<int:id>', methods=['GET'])
def getSensor(id=1):
  sensor = Sensor.query.get(id)
  print [{"val": m.val, "update_on": m.update_on.isoformat()} for m in sensor.measures]
  return json.dumps({"sensor": id})
  
@app.route('/api/sensors/<int:id>', methods=['POST'])
def postSensor(id):
  sensor = Sensor.query.get(id)
  data = request.json
  if sensor:
    data['sensor_id'] = id
    data['update_on'] = datetime.now()
    m = Measure(**data)
    db.session.add(m)
    db.session.commit()
  else:
    abort(404)

  return json.dumps({"result": "OK"})

