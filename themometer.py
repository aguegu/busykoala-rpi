# -*- coding: utf-8 -*-
from config import THERMOMETER_PATH
import time
import requests
import json
from datetime import datetime

def getTemperature():
  f = open(THERMOMETER_PATH)
  t = int(''.join(f.read().split(' ')[:2][::-1]), 16)
  if t & 0x8000:
    t -= 0x10000
  f.close()
  return t

headers = {'content-type': 'application/json'}
t_last = 0

if __name__ == '__main__':
  try:
    while True:
      t = getTemperature()
      if t != t_last:
        r = requests.post('http://localhost:5000/api/sensors/1', headers=headers, data=json.dumps({'val': t}))
        print datetime.now().isoformat(), t, r.status_code
        t_last = t

      time.sleep(10)
      
  except KeyboardInterrupt:
    exit(0)
