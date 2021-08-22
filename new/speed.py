#from count import *
class Speed:
   def __init__(self,speed):
      self.s=speed
   def convert(self):
      meter_per_second=self.s*0.28
      print("speed in meter per second is ",meter_per_second)
n=int(input("enter the speed in km/h"))
obj1=Speed(n)
obj1.convert()
