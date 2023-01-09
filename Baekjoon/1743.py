import sys
sys.setrecursionlimit(10**4)

n,m,k=map(int,input().split())

v=[[0]*(n+1) for _ in range(m+1)]
g=[[0]*(n+1) for _ in range(m+1)]
result=0

for _ in range(k):
    x,y=map(int,input().split())
    g[y][x]=1

def dfs(x,y):
    v[y][x]=1
    cnt=1
    for (nx,ny) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0<nx<=n and  0<ny<=m and g[ny][nx]==1 and v[ny][nx]==0:
            cnt+=dfs(nx,ny)

    return cnt

for i in range(1,n+1):
    for j in range(1,m+1):
        if  g[j][i]==1 and v[j][i]==0:
            result = max(result,dfs(i,j))
            
print(result)
            