a=str(input("enter string"))
def count(a):
   s=0
   for i in a:
      s=s+1
   print(s)
count(a)

#reverse a list using function
list=[1,2,3,4,5,6]
def rev(list):
   list.reverse()
   print(list)
rev(list)
#function return data type of list
list=[1,2,3,45]
def typ(list):
   return type(list)
print(typ(list))