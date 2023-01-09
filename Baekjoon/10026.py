import sys
sys.setrecursionlimit(10**4)

res=0
res2=0

n=int(input())
v=[[0]*n for _ in range(n)]

f=[]
for _ in range(n):
    f.append(input())


def dfs(x,y,c):
    v[y][x]=1
    
    for (nx,ny) in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        if 0<=nx<n and 0<=ny<n and not v[ny][nx] and f[ny][nx]==c:
            dfs(nx,ny,c)
                
            
            
for i in range(n):
    for j in range(n):
        for k in ('R','G','B'):
            if not v[j][i] and f[j][i]==k:
                dfs(i,j,k)
                res+=1
                
                
v=[[0]*n for _ in range(n)]

for i in range(len(f)):
    f[i]=f[i].replace('R','G')


for i in range(n):
    for j in range(n):
        for k in ('G','B'):
            if not v[j][i] and f[j][i]==k:
                dfs(i,j,k)
                res2+=1

print(res,res2)