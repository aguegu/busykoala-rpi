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
sensorid = '538147497943f70bcf756146'
url = 'http://115.29.223.207:5000/api/sensor/%s' % sensorid

if __name__ == '__main__':
    try:
        while True:
            t = getTemperature()
            if t != t_last:
                try:
                    r = requests.post(url, headers=headers, data=json.dumps({'val': t}))
                except requests.exceptions.ConnectionError:
                    print 'request failed, retry later.'
                    pass
                else:
                    print datetime.now().isoformat(), t, r.status_code
                    t_last = t

            time.sleep(10)
          
    except KeyboardInterrupt:
        exit(0)
