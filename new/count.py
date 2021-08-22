class Count:
   def __init__ (self,s):
       self.str=s
   def count(self):
      
      a=input("enter word that you want to count")
      c=0
      d=self.str.split(" ")
      for i in range(len(d)):
         if (a==d[i]):
            c+=1   
      print("no of word",c)
s=input("enter a sting")
class Max(Count):
   def __init__(self):
      s=input("enter a sting")
   super(). __init__(s)
   def Quan(self):
      n=int(input('enter the no element'))
      for i in range(n):
         key=input("enter item name")
         val=int(input("enter item quantity"))
         d[key]=val
      for i in d.keys():
         if d[i] > d[i+1]:
            max=d[i]
            k=i
         else:
            max=d[i+1]
            k=i+1
      print(max)       
obj=Max()
obj.count()
obj.Quan()