from collections import deque

n,k=map(int,input().split())
MAX=10**5
v=[-1]*(MAX+1)

def bfs():
    q=deque()
    q.append(n)
    v[n]=0
    while q:
        x=q.popleft()
        
        if x == k:
            print(v[x])
            return
        
        nx=x*2
        if 0<=nx<=MAX and  (v[nx]==-1 or v[nx]>v[x]):
            v[nx]=v[x]
            q.append(nx)
        
        for nx in (x+1,x-1):
            if 0<=nx<=MAX and  (v[nx]==-1 or v[nx]>v[x]):
                v[nx]=v[x]+1
                q.append(nx)

bfs()