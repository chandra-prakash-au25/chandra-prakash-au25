a=list()
a=list(map(int,input().split()))
n=len(a)
min=float("inf")
for i in range(n):
   if min>a[i]:
      min=a[i]
      k=i
max=min
for j in range(k,n):
   if a[j]>min and a[j]>max:
      max=a[j]
      m=j
if max==min:
   print("0")
if max>min:
   print(m+1,"th day")
#pascal triangle
dp=[-1]*1000
def fact(n):
   global dp
   if n==0:
      return 1
   if n==1:
      return 1
   if dp[n]!=-1:
      return dp[n]
   dp[n]=fact(n-1)+fact(n-2)
   return dp[n]
n=int(input())
for i in range(n):
   for j in range(n-i+1):
      print(end=" ")
   for j in range(i+1):
      print(fact(i)//(fact(j)*fact(i-j)),end=" ")
   print()
#  pascal2
dp=[-1]*1000
def fact(n):
   global dp
   if n==0:
      return 1
   if n==1:
      return 1
   if dp[n]!=-1:
      return dp[n]
   dp[n]=fact(n-1)+fact(n-2)
   return dp[n]
n=int(input())
k=n
for i in range(n):
   if i==(k-1): 
      for j in range(n-i+1):
            pass
      for j in range(i+1):
            print(fact(i)//(fact(j)*fact(i-j)),end=" ")
   