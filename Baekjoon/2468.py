import sys
sys.setrecursionlimit(10**4)

n=int(input())

v=[[0]*n for _ in range(n)]

f=[]
for _ in range(n):
    f.append(list(map(int,input().split())))

r=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if f[i][j]:
            r[i].append(j)
            
            
def dfs(x,y):
    v[y][x]=1
    
    for nx in r[x]:
        if not v[y][nx]:
            dfs(nx,y)
            
for i in range(n):
    for j in r[i]:
        if not v[i][j]:
            dfs(j,i)
                
for i in v:
    for j in i:
        print(j,end=' ')
    print()