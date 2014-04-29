from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(128))

class Sensor(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  measures = db.relationship('Measure', backref = 'snsor', lazy = 'dynamic')

class Measure(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  val = db.Column(db.Integer, nullable = False)
  sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

