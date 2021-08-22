#space comlexity of the following code"""
"""n =int(input())
for i in range (n):
   for j in range (n):
      print("space comlexity")

space complexity=O(1)"""



#leetcode  roblem solution




a=[0,0,0,0,0,1]
for i in range(6):
   for j in range(6):
      if a[j]==0:
         continue
      elif i==5:
         val=a[i]
         val=val+1
         a[i]=val
print(a)
#reverse of an aarray
l=[1,2,3,4,5,7,8]
s=len(l)
for i in range(int(s/2)):
   a=l[i]
   b=l[s-i-1]
   a=a+b
   b=a-b
   a=a-b
   l[i]=a
   l[s-i-1]=b
print (l)      
   

