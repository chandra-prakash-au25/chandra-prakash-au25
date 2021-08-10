# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it
a=[ ]
n=int(input("enter number of element in list"))
for i in range(0,n):
   ele=int(input())
   a.append(ele)
print(a)
#convert list into touples
print(tuple(a))
# remove last 4th element and put a string in 2nd pos in the list
c=[1,2,3,4,5,6,7,8,9]
print(c)
c.pop(len(c)-4)
print(c)
