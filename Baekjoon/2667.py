n=int(input())
v=[[0]*(n) for _ in range(n)]
f=[]
results=[]

for _ in range(n):
    f.append(list(input()))
    
def dfs(x,y):
    v[y][x]=1
    cnt=1
    for (nx,ny) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0<=nx<n and 0<=ny<n and v[ny][nx]==0 and f[ny][nx]=='1':
            cnt+=dfs(nx,ny)
    return cnt

for i in range(n):
    for j in range(n):
        if v[i][j]==0 and f[i][j]=='1':
            results.append(dfs(j,i))
            
print(len(results))
results.sort() 
for result in results:
    print(result)