import math

a = (0,0)
b = (5, 10)
w = b[0] - a[0]
h = b[1] - a[1]
print(math.atan(w/h))

rad_v = math.atan(w/h)
deg_v = rad_v * 180/math.pi
print(deg_v)

math.at