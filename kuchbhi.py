n=5
gp=[[0 for _ in range(n+1)]for _ in range(n+1)]
def addedge(u,v,wt,dir):
   gp[u][v]=wt
   if  not dir:
      gp[u][v]=wt
addedge(1,2,1,True)
addedge(0,3,1,True)
addedge(2,3,1,True)
addedge(3,2,1,True)
addedge(2,5,1,True)
for i in range(n+1):
   for j in range(n+1):
      print(gp[i][j],end=" ")
   print()
graph=dict()
def addedge1(u,v,wt,dir):
   if u  not in graph:
      graph[u]=[]
      graph[u].append((v,wt))
   if not dir:
      if v not  in graph:
         graph[v]=[]
         graph[v].append((u,v))
addedge1(1,2,1,True)
addedge1(0,3,1,True)
addedge1(2,3,1,True)
addedge1(3,2,1,True)
addedge1(2,5,1,True)
print(graph)

