a=list()
n=int(input("enter the length of the list"))
for i in range(n):
   x=int(input("enter the number"))
   a.append(x)

print(a)
a.insert(1,"hello")
a.insert(2,8)#insert at given position like 2 index start from 0
a.insert(-1,3)#insert at end
a.insert(0,10)#insert at start
print(a)
b=[1,2,3,4]
print(a+b)#addd only elelment 
a.append(b)#add hole list as is it
print(a)
p=a.pop(1)#remove element from top
print(p)
print(a)