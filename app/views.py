from app import app, db
from flask import json, request, abort, render_template
from models import Sensor, Measure
from datetime import datetime
import time

@app.route('/', methods=['GET'])
def index():
  return 'Hello, world.'

@app.route('/api/sensors', methods=['GET'])
@app.route('/api/sensors/<int:id>', methods=['GET'])
def getSensor(id=1):
  sensor = Sensor.query.get(id)
  measures = [{"y": m.val / 16.0, "x": int(time.mktime(m.update_on.timetuple()) * 1000)} for m in sensor.measures.order_by("update_on desc").limit(10)]

  return json.dumps({"sensor": id, "measures": measures })
  
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

@app.route('/chart')
def showChart():
  return render_template('chart.html')
