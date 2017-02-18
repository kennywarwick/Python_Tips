#coding:UTF-8
import time

import geocoder

g = geocoder.google("No.13 Zhongxin New Village")
time.sleep(1)
print g.latlng
