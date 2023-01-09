import sys
sys.setrecursionlimit(10**5)

def dfs(x,y):
    v[y][x]=1
    for (nx,ny) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0<=nx<m and 0<=ny<n and not v[ny][nx] and f[ny][nx]:
            dfs(nx,ny)
        



t=int(input())

for _ in range(t):
    m,n,k=map(int,input().split())
    result=0
    
    v=[[0]*m for _ in range(n)]
    f=[[0]*m for _ in range(n)]
    
    for _ in range(k):
        x,y=map(int,input().split())
        f[y][x]=1
        
    for y in range(n):
        for x in range(m):
            if not v[y][x] and f[y][x]:
                dfs(x,y)
                result+=1
    
    print(result)
            