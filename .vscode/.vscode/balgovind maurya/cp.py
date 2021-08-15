import datetime
now=datetime.datetime.now()
print("current data and time: ")
print(now.strftime("%y-%m-%d %H:%M:%S"))
from math import pi
r=float(input("input the radius of circuls;:"))
print("the area of the circle with radius"+str(r)+"is :" +str(pi*r**2))