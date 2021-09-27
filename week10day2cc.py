#maimum path sum
mat=[[348,391],[618,193]]
m=2
n=2
ans=0
r=0
c=0
def path(mat):
   global m,n,r,c
   global ans
   if r>m or c>n:
      return  0
   if r==m-1 and c==n-1:
      return mat[r][c]
   else:
      ans+=max(path(mat[r+1][c]),max(path(mat[r+1][c-1]),path(mat[r+1][c+1])))
k=path(mat[0][0])
print(k)