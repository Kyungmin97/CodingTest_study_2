import sys
sys.setrecursionlimit(10**4)

n,m=map(int,input().split())

v=[0]*(n+1)
r=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    r[x].append(y)
    r[y].append(x)
    

def dfs(x):
    v[x]=1
    
    for nx in r[x]: 
        if not v[nx]:
            dfs(nx)
        
result=0
for i in range(1,n+1):
    if not v[i]:
        dfs(i)
        result+=1
print(result)