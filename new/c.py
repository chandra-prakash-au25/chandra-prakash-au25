a=[1,2,3,4,5]
for i in range(5):
   if i==4:
      val=a[i]
      val+=1
      a[i]=val
   
print(a)