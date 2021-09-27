def tilling(m,n):
    if m==0 or n==0:
        global dp
        return 0
    if m==n:
        return 1
    if dp[m][n]!=-1:
        return dp[m][n]
    if m>n:
        dp[m][n]= tilling(m-n,n)+1
        return dp[m][n]
    if m<n:
        return tilling(n,m)
dp=[[-1 for _ in range(100)]for _ in range(100)]
ans=tilling(13,4)
print(ans)