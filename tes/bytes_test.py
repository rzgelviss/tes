import socket
import time
import random
import struct
import json
import base64

a = []
floatList = [random.random() for _ in range(3)]
print(floatList)
buf = struct.pack('%sf' % len(floatList), *floatList)
print(buf)
code = base64.b64encode(buf)
print(code)
code = code.decode()
print(code)
a.append(code)
a.append(code)
print(a)
# js = json.dumps(str(code))
# print(js)
# js = json.loads(js)
# print(js)
# print(type(js))
decode = base64.b64decode(code)
decode = decode
print(decode)
# json.dumps(ssdir)

float_list = struct.unpack('%sf' % int(len(decode)/4), decode)
float_list = list(float_list)
print(float_list)


print('\n\n')
# buf = bytes()
# for val in floatlist:
#     buf += struct.pack('f', val)
# print(buf)
ls = [i for i in buf]
print(ls)
import numpy as np
ss=ls
tt=np.array(ss)
yy=tt.reshape(3,4)
print(yy)


for i in range(3):
    y=struct.unpack('<f', struct.pack('4B',*yy[i]))[0]
    # y = struct.unpack('<f', struct.pack('4B', *yy))
    print(y)



