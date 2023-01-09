import sys
sys.setrecursionlimit(10**4)


m,n,k=map(int,input().split())
res=[]

v=[[0]*n for _ in range(m)]
s=[[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            s[j][i]+=1
            
def dfs(x,y):
    v[y][x]=1
    cnt=1
    for (nx,ny) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0<=nx<n and 0<=ny<m and not s[ny][nx] and not v[ny][nx]:
            cnt+=dfs(nx,ny)
    return cnt

for i in range(n):
    for j in range(m):
        if not v[j][i] and not s[j][i]:
            res.append(dfs(i,j))

print(len(res))
res.sort()
for r in res:
    print(r,end=' ')