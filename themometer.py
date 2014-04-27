# -*- coding: utf-8 -*-

from config import THERMOMETER_PATH

f = open(THERMOMETER_PATH)

t = int(''.join(f.read().split(' ')[:2][::-1]), 16)
if t & 0x8000:
  t -= 0x10000
print t

f.close()
