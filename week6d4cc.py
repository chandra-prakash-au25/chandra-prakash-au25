#Q-1 ) Select the appropriate code that performs selection sort.

for j in range(n):
   min = j
   for k in range(j+1,n):
      if(arr[k] < arr[min]):
        min = k
        temp = arr[min]
         arr[min] = arr[j]
         arr[j] = temp

"""
Q-2 ) What is the worst case complexity of selection sort? (5 marks)
a) O(nlogn)
b) O(logn)
c) O(n)
d) O(n)
answer=O(n**2)


"""
#selection sort bethought using second array
arr=[1,4,3,2,5,76,6,9,0]
n=len(arr)
for j in range(n):
   min = j
   for k in range(j+1,n):
      if(arr[k] < arr[min]):
         min = k
         temp = arr[min]
         arr[min] = arr[j]
         arr[j] = temp
print(arr)

#selection sort using while loop
arr=[1,4,3,2,5,76,6,9,0]
n=len(arr)
l=0
while l<n:
   min = l
   for k in range(l+1,n):
      if(arr[k] < arr[min]):
         min = k
         temp = arr[min]
         arr[min] = arr[l]
         arr[l] = temp
   l+=1      
print(arr)
