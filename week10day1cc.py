# fibonacci number
def fib(n):
   if n==0:
      return 0
   if n==1:
      return 1
   else:
      return fib(n-1)+fib(n-2)
print(fib(5))
#fibnacci number using recuirence
def fibn(n,a):
   if n==0:
      return 0
   if n==1:
      return 1
   if a[n]!=-1:
      return a[n]
   ans=fibn(n-1,a)+fibn(n-2,a)
   a[n]=ans
   return ans
a=[-1]*1000
print(fibn(5,a))
#find the power of x
def pow(x,n,a):
   if n==0:
      return 1
   if n==1:
      return x
   if a[n]!=-1:
      return a[n]
   else:
      if n%2==0:
         ans= pow(x,n//2,a)*pow(x,n//2,a)
         a[n]=ans
         return ans
      else:
         ans= x*pow(x,n//2,a)*pow(x,n//2,a)
         a[n]=ans
         return ans
a=[-1]*1000
print(pow(4,5,a))