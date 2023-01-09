from collections import deque

MAX=10**4
n,m= map(int,input().split())

v=[[MAX]*n for _ in range(m)]
v[0][0]=0
r= [ list(map(int, input())) for _ in range(m)]

def bfs():
    q=deque()
    q.append((0,0))
    
    while q:
        x,y=q.popleft()
        for (nx,ny) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=nx<n and 0<=ny<m and v[ny][nx]==MAX:
                if r[ny][nx]==1:
                    v[ny][nx]=v[y][x]+1
                    q.append((nx,ny))
                else:
                    v[ny][nx]=v[y][x]
                    q.appendleft((nx,ny))
                    
                
bfs()
print(v[m-1][n-1])
                
    
    